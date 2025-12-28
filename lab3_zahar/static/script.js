const API = '/api/decision';

async function startSession() {
    try {
        await fetch(`${API}/start`);
        document.getElementById('resultBox').style.display = 'none';
        document.getElementById('questionBox').style.display = 'block';
        getNextQuestion();
    } catch (e) {
        alert('Ошибка запуска сессии: ' + e.message);
    }
}

async function getNextQuestion() {
    try {
        const res = await fetch(`${API}/next`);
        const data = await res.json();

        console.log('Next question response:', data);

        if (data.finished) {
            showResult(data.conclusion);
            return;
        }

        document.getElementById('question').textContent = data.question;
        renderScale(data.evidenceId);
    } catch (e) {
        alert('Ошибка получения вопроса: ' + e.message);
    }
}

function renderScale(evidenceId) {
    const scale = document.getElementById('scale');
    scale.innerHTML = '';
    for (let i = 1; i <= 5; i++) {
        const btn = document.createElement('button');
        btn.className = 'scale-btn';
        btn.textContent = i;
        btn.onclick = () => submitAnswer(evidenceId, i);
        scale.appendChild(btn);
    }
}

async function submitAnswer(evidenceId, rating) {
    try {
        console.log('Submitting answer:', { evidenceId, rating });

        const response = await fetch(`${API}/answer`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                evidence_id: evidenceId,  // Используем evidence_id (с подчеркиванием)
                rating: rating
            })
        });

        console.log('Response status:', response.status);

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Error response:', errorText);

            try {
                const errorData = JSON.parse(errorText);
                throw new Error(errorData.detail || 'Ошибка сервера');
            } catch {
                throw new Error(`HTTP ${response.status}: ${errorText}`);
            }
        }

        const data = await response.json();
        console.log('Answer response:', data);

        if (data.finished) {
            showResult(data.conclusion);
        } else {
            document.getElementById('question').textContent = data.question;
            renderScale(data.evidenceId);
        }
    } catch (e) {
        console.error('Submit error:', e);
        alert('Ошибка отправки ответа: ' + e.message);
    }
}

function showResult(conclusion) {
    document.getElementById('questionBox').style.display = 'none';
    document.getElementById('resultText').textContent = conclusion;
    document.getElementById('resultBox').style.display = 'block';
}

function restartSession() {
    startSession();
}

// Запуск при загрузке
document.addEventListener('DOMContentLoaded', startSession);

// Добавляем консоль для отладки
console.log('Script loaded');