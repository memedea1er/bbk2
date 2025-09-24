from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Dict, Any

app = FastAPI(title="Game Recommendation System")

# Mount static files and templates
app.mount("static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class GameRecommendationSystem:
    def __init__(self):
        # Полная база данных игр
        self.games_db = [
            # RPG игры
            {"id": 1, "title": "The Witcher 3: Wild Hunt", "platform": ["PC", "игровая консоль"],
             "genre": "Ролевая игра", "setting": "Фэнтези", "rating": "M", "price": "AAA-цена",
             "game_type": ["Одиночная"], "duration": "океан контента", "graphics": "Фотореализм"},
            {"id": 2, "title": "Cyberpunk 2077", "platform": ["PC", "игровая консоль"],
             "genre": "Ролевая игра", "setting": "Киберпанк", "rating": "M", "price": "AAA-цена",
             "game_type": ["Одиночная"], "duration": "долгая", "graphics": "Фотореализм"},
            {"id": 3, "title": "Elden Ring", "platform": ["PC", "игровая консоль"],
             "genre": "Ролевая игра", "setting": "Фэнтези", "rating": "M", "price": "AAA-цена",
             "game_type": ["Одиночная", "Многопользовательская"], "duration": "океан контента", "graphics": "Фотореализм"},
            {"id": 4, "title": "Skyrim", "platform": ["PC", "игровая консоль"],
             "genre": "Ролевая игра", "setting": "Фэнтези", "rating": "M", "price": "AAA-цена",
             "game_type": ["Одиночная"], "duration": "океан контента", "graphics": "стилизованная графика"},
            {"id": 5, "title": "Mass Effect: Legendary Edition", "platform": ["PC", "игровая консоль"],
             "genre": "Ролевая игра", "setting": "Научная фантастика", "rating": "M", "price": "AAA-цена",
             "game_type": ["Одиночная"], "duration": "океан контента", "graphics": "Фотореализм"},
            {"id": 6, "title": "Disco Elysium", "platform": ["PC", "игровая консоль"],
             "genre": "RPG", "setting": "Современный", "rating": "M", "price": "инди-цена",
             "game_type": ["Одиночная"], "duration": "средняя", "graphics": "стилизованная графика"},
            # Экшен игры
            {"id": 7, "title": "Counter-Strike 2", "platform": ["PC"], "genre": "Экшен",
             "setting": "Современный", "rating": "M", "price": "Бесплатная",
             "game_type": ["Многопользовательская", "Соревновательный"], "duration": "океан контента", "graphics": "Фотореализм"},
            {"id": 8, "title": "The Last of Us Part I", "platform": ["PC", "игровая консоль"], "genre": "Экшен",
             "setting": "Постапокалипсис", "rating": "M", "price": "AAA-цена",
             "game_type": ["Одиночная"], "duration": "средняя", "graphics": "Фотореализм"},
            {"id": 9, "title": "Fortnite", "platform": ["PC", "игровая консоль", "мобильные устройства"], "genre": "Экшен",
             "setting": "Современный", "rating": "T", "price": "Бесплатная",
             "game_type": ["Многопользовательская", "Соревновательный"], "duration": "океан контента", "graphics": "стилизованная графика"},
            {"id": 10, "title": "DOOM Eternal", "platform": ["PC", "игровая консоль"], "genre": "Экшен",
             "setting": "Научная фантастика", "rating": "M", "price": "AAA-цена",
             "game_type": ["Одиночная", "Многопользовательская"], "duration": "средняя", "graphics": "Фотореализм"},
            # ... добавь остальные игры (11–40) сюда по той же структуре
        ]

        # Ассоциации вопросов
        self.genre_associations = {
            'Экшен': "Вам нравятся динамичные игры со сражениями?",
            'Приключения': "Вам нравятся исследования и решение загадок?",
            'Ролевая игра': "Вам нравятся развитие персонажей и интересные сюжеты?",
            'Стратегии': "Вам нравятся планирование и тактические решения?",
            'Симуляторы': "Вам нравятся реалистичные симуляции жизни или деятельности?",
            'Гонки': "Вам нравятся скоростные соревнования и автомобили?",
            'Спортивные': "Вам нравятся спортивные соревнования и турниры?"
        }

        self.setting_associations = {
            'Фэнтези': "Вам нравятся рыцари, магия и древние замки?",
            'Научная фантастика': "Вам нравятся космос, технологии и будущее?",
            'Киберпанк': "Вам нравятся неоновые города, кибернетика и высокие технологии?",
            'Стимпанк': "Вам нравятся паровые машины, шестерёнки и викторианская эпоха?",
            'Постапокалипсис': "Вам нравятся выживание в разрушенном мире?",
            'Исторический': "Вам нравятся древние цивилизации и исторические события?",
            'Современный': "Вам нравятся современные города и реалистичные истории?",
            'Хоррор': "Вам нравятся ужасы и пугающая атмосфера?"
        }

        self.type_associations = {
            'Одиночная': "Вам нравятся игры, где можно играть в одиночку?",
            'Многопользовательская': "Вам нравятся игры с другими игроками онлайн?",
            'Кооператив': "Вам нравятся игры, где можно играть с друзьями вместе?",
            'Соревновательный': "Вам нравятся соревнования против других игроков?"
        }

        self.graphics_associations = {
            'Фотореализм': "Вам нравится реалистичная графика, как в кино?",
            'стилизованная графика': "Вам нравится художественный стиль и уникальный визуал?",
            'пиксель-арт': "Вам нравится ретро-стиль и пиксельная графика?"
        }

        self.rating_names = {
            'E': 'Для всех (E)',
            'E10+': 'Для всех от 10+ (E10+)',
            'T': 'Для подростков (T)',
            'M': 'Для взрослых (M/A)'
        }

        self.price_names = {
            'Бесплатная': 'Бесплатная',
            'инди-цена': 'инди-цена (до 1000 рублей)',
            'AAA-цена': 'AAA-цена (более 2000 рублей)',
        }

        self.duration_names = {
            'Короткая': 'Короткая (менее 10 часов)',
            'средняя': 'Средняя (10-30 часов)',
            'долгая': 'Долгая (30-60 часов)',
            'океан контента': 'Океан контента (60+ часов)'
        }

    def find_matching_games(self, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Поиск игр с системой баллов"""
        scored_games = []

        for game in self.games_db:
            score = 0
            reasons = []

            # Платформа (важный критерий - 10 баллов)
            if preferences.get('platform'):
                platform_match = any(platform in game['platform'] for platform in preferences['platform'])
                if platform_match:
                    score += 10
                    reasons.append("✓ Подходит по платформе")
                else:
                    reasons.append("✗ Не подходит по платформе")
                    continue  # Платформа - обязательный критерий

            # Жанр (очень важный - 8 баллов)
            if preferences.get('genre'):
                if game['genre'] in preferences['genre']:
                    score += 8
                    reasons.append("✓ Идеально по жанру")
                else:
                    reasons.append("✗ Не подходит по жанру")

            # Сеттинг (важный - 6 баллов)
            if preferences.get('setting'):
                if game['setting'] in preferences['setting']:
                    score += 6
                    reasons.append("✓ Идеально по сеттингу")
                else:
                    reasons.append("~ Другой сеттинг")

            # Цена (важный - 7 баллов)
            if preferences.get('price'):
                if game['price'] == preferences['price']:
                    score += 7
                    reasons.append("✓ Подходит по цене")
                else:
                    reasons.append("~ Другая ценовая категория")

            # Тип игры (важный - 7 баллов)
            if preferences.get('game_type'):
                type_match = any(game_type in game['game_type'] for game_type in preferences['game_type'])
                if type_match:
                    score += 7
                    reasons.append("✓ Подходит по типу игры")
                else:
                    reasons.append("~ Не совсем подходит по типу игры")

            # Продолжительность (менее важный - 3 балла)
            if preferences.get('duration') and game['duration'] == preferences['duration']:
                score += 3
                reasons.append("✓ Подходит по продолжительности")

            # Графика (менее важный - 3 балла)
            if preferences.get('graphics'):
                if game['graphics'] in preferences['graphics']:
                    score += 3
                    reasons.append("✓ Подходит по графике")
                else:
                    reasons.append("~ Другой стиль графики")

            # Добавляем игру с баллом, если прошла обязательные критерии
            scored_games.append({
                'game': game,
                'score': score,
                'reasons': reasons
            })

        # Сортируем по убыванию баллов
        scored_games.sort(key=lambda x: x['score'], reverse=True)
        return scored_games


# Создаем экземпляр системы рекомендаций
recommendation_system = GameRecommendationSystem()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница с формой"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "rating_names": recommendation_system.rating_names,
        "price_names": recommendation_system.price_names,
        "duration_names": recommendation_system.duration_names,
        "genre_associations": recommendation_system.genre_associations,
        "setting_associations": recommendation_system.setting_associations,
        "type_associations": recommendation_system.type_associations,
        "graphics_associations": recommendation_system.graphics_associations
    })


@app.post("/recommend")
async def recommend(request: Request):
    form = await request.form()

    # чекбоксы
    platform = form.getlist("platform")

    # радиокнопки да/нет → берём только те, где "yes"
    genre = [key.replace("genre_", "") for key, val in form.items() if key.startswith("genre_") and val == "yes"]
    setting = [key.replace("setting_", "") for key, val in form.items() if key.startswith("setting_") and val == "yes"]
    game_type = [key.replace("game_type_", "") for key, val in form.items() if key.startswith("game_type_") and val == "yes"]
    graphics = [key.replace("graphics_", "") for key, val in form.items() if key.startswith("graphics_") and val == "yes"]

    # обычные radio
    rating = form.get("rating")
    price = form.get("price")
    duration = form.get("duration")

    # собираем предпочтения
    preferences = {
        "platform": platform,
        "genre": genre,
        "setting": setting,
        "rating": rating,
        "price": price,
        "game_type": game_type,
        "duration": duration,
        "graphics": graphics,
    }

    results = recommendation_system.find_matching_games(preferences)

    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "results": results[:10]
        }
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)