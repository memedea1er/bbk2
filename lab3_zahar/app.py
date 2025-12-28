from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv
from pathlib import Path
import json

from models import Hypothesis, AnswerDto
from engine import NeilerDecisionEngine

app = FastAPI(title="Vacation Advisor API")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Глобальный экземпляр движка
_engine: Optional[NeilerDecisionEngine] = None


def load_hypotheses() -> List[Hypothesis]:
    """Загрузка гипотез из CSV файла"""
    hypotheses = []

    try:
        csv_path = Path("data/knowledge_base.csv")

        if csv_path.exists():
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=';')
                next(reader)  # Пропускаем заголовок

                for row in reader:
                    if len(row) < 4:
                        continue

                    name = row[0]
                    prior = float(row[1])
                    evidence_str = row[3].strip('"')

                    evidence_map = {}
                    if evidence_str:
                        pairs = evidence_str.split("),(")
                        for pair in pairs:
                            clean = pair.strip("()")
                            tokens = clean.split(';')
                            if len(tokens) >= 3:
                                j = int(tokens[0])
                                p_plus = float(tokens[1])
                                p_minus = float(tokens[2])
                                evidence_map[j] = (p_plus, p_minus)

                    hypotheses.append(Hypothesis(
                        name=name,
                        prior=prior,
                        evidence_map=evidence_map
                    ))

    except Exception as e:
        print(f"Ошибка загрузки гипотез: {e}")

    return hypotheses


@app.get("/api/decision/start")
def start_session():
    """Начало новой сессии"""
    global _engine
    hypotheses = load_hypotheses()
    _engine = NeilerDecisionEngine(hypotheses)
    return {"message": "Сессия начата"}


@app.get("/api/decision/next")
def get_next_question():
    """Получить следующий вопрос"""
    if _engine is None:
        raise HTTPException(status_code=400, detail="Сессия не начата")

    evidence_id, question = _engine.get_next_question()
    if question is None:
        should_stop, conclusion = _engine.check_stopping_condition()
        return {"finished": True, "conclusion": conclusion}

    return {"evidenceId": evidence_id, "question": question}


@app.post("/api/decision/answer")
def submit_answer(answer: AnswerDto):
    """Отправить ответ на вопрос"""
    if _engine is None:
        raise HTTPException(status_code=400, detail="Сессия не начата")

    if answer.rating < 1 or answer.rating > 5:
        raise HTTPException(status_code=400, detail="Рейтинг должен быть от 1 до 5")

    _engine.update_probabilities(answer.evidence_id, answer.rating)

    should_stop, conclusion = _engine.check_stopping_condition()
    if should_stop:
        return {"finished": True, "conclusion": conclusion}

    evidence_id, question = _engine.get_next_question()
    if question is None:
        final_stop, final_conclusion = _engine.check_stopping_condition()
        return {"finished": True, "conclusion": final_conclusion}

    return {"evidenceId": evidence_id, "question": question}


# Для отладки: эндпоинт для проверки состояния
@app.get("/api/debug/state")
def debug_state():
    """Отладочная информация о текущем состоянии"""
    if _engine is None:
        return {"status": "engine_not_initialized"}

    return {
        "probabilities": _engine.probabilities,
        "observed_evidence": _engine.observed_evidence,
        "hypotheses": [h.name for h in _engine.hypotheses]
    }


# Статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Главная страница"""
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Выбор места отдыха</title>
        <link rel="stylesheet" href="/static/style.css" />
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Куда поехать отдыхать?</h1>
                <p class="subtitle">Ответьте на несколько вопросов — и мы подберём идеальное место</p>
            </header>

            <main>
                <div class="question-box" id="questionBox">
                    <p id="question" class="question-text">Загрузка...</p>
                    <div class="scale" id="scale"></div>
                </div>

                <div class="result-box" id="resultBox" style="display: none;">
                    <div class="result-icon">✨</div>
                    <h2>Ваш идеальный отдых:</h2>
                    <p id="resultText" class="result-text"></p>
                    <button class="restart-btn" onclick="restartSession()">Начать заново</button>
                </div>
            </main>

            <footer>
                <p>Нейлеровская система поддержки решений</p>
            </footer>
        </div>

        <script src="/static/script.js"></script>
    </body>
    </html>
    """


# Для разработки: отдаём статические файлы напрямую
@app.get("/style.css")
async def get_css():
    return FileResponse("static/style.css")


@app.get("/script.js")
async def get_js():
    return FileResponse("static/script.js")