from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Dict, Any, Tuple
import copy

app = FastAPI(title="Game Recommendation System - Bayesian")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class BayesianGameRecommendationSystem:
    def __init__(self):
        # База знаний: гипотезы (игры) и свидетельства (признаки)
        self.hypotheses = [
            # RPG игры
            {"id": 1, "title": "The Witcher 3: Wild Hunt", "prior_prob": 0.01},
            {"id": 2, "title": "Cyberpunk 2077", "prior_prob": 0.01},
            {"id": 3, "title": "Elden Ring", "prior_prob": 0.01},
            {"id": 4, "title": "Skyrim", "prior_prob": 0.01},
            {"id": 5, "title": "Mass Effect: Legendary Edition", "prior_prob": 0.01},
            {"id": 6, "title": "Disco Elysium", "prior_prob": 0.01},
            {"id": 7, "title": "Baldur's Gate 3", "prior_prob": 0.01},
            {"id": 8, "title": "Divinity: Original Sin 2", "prior_prob": 0.01},
            {"id": 9, "title": "Persona 5 Royal", "prior_prob": 0.01},
            {"id": 10, "title": "Final Fantasy XIV", "prior_prob": 0.01},

            # Экшен игры
            {"id": 11, "title": "Counter-Strike 2", "prior_prob": 0.01},
            {"id": 12, "title": "The Last of Us Part I", "prior_prob": 0.01},
            {"id": 13, "title": "Fortnite", "prior_prob": 0.01},
            {"id": 14, "title": "DOOM Eternal", "prior_prob": 0.01},
            {"id": 15, "title": "Grand Theft Auto V", "prior_prob": 0.01},
            {"id": 16, "title": "Red Dead Redemption 2", "prior_prob": 0.01},
            {"id": 17, "title": "God of War", "prior_prob": 0.01},
            {"id": 18, "title": "Hades", "prior_prob": 0.01},

            # Стратегии
            {"id": 19, "title": "Civilization VI", "prior_prob": 0.01},
            {"id": 20, "title": "Crusader Kings III", "prior_prob": 0.01},
            {"id": 21, "title": "Stellaris", "prior_prob": 0.01},
            {"id": 22, "title": "XCOM 2", "prior_prob": 0.01},
            {"id": 23, "title": "Total War: Warhammer III", "prior_prob": 0.01},
            {"id": 24, "title": "Age of Empires IV", "prior_prob": 0.01},

            # Приключенческие игры и квесты
            {"id": 25, "title": "Life is Strange: True Colors", "prior_prob": 0.01},
            {"id": 26, "title": "The Walking Dead: The Telltale Series", "prior_prob": 0.01},
            {"id": 27, "title": "Firewatch", "prior_prob": 0.01},
            {"id": 28, "title": "What Remains of Edith Finch", "prior_prob": 0.01},
            {"id": 29, "title": "Gone Home", "prior_prob": 0.01},
            {"id": 30, "title": "Oxenfree", "prior_prob": 0.01},

            # Пазлы и логические игры
            {"id": 31, "title": "Portal 2", "prior_prob": 0.01},
            {"id": 32, "title": "The Talos Principle", "prior_prob": 0.01},
            {"id": 33, "title": "The Witness", "prior_prob": 0.01},
            {"id": 34, "title": "Baba Is You", "prior_prob": 0.01},
            {"id": 35, "title": "Return of the Obra Dinn", "prior_prob": 0.01},

            # Симуляторы
            {"id": 36, "title": "The Sims 4", "prior_prob": 0.01},
            {"id": 37, "title": "Microsoft Flight Simulator", "prior_prob": 0.01},
            {"id": 38, "title": "Euro Truck Simulator 2", "prior_prob": 0.01},
            {"id": 39, "title": "Stardew Valley", "prior_prob": 0.01},
            {"id": 40, "title": "Cities: Skylines", "prior_prob": 0.01},
            {"id": 41, "title": "Farming Simulator 22", "prior_prob": 0.01},
            {"id": 42, "title": "Planet Zoo", "prior_prob": 0.01},

            # Хорроры
            {"id": 43, "title": "Resident Evil Village", "prior_prob": 0.01},
            {"id": 44, "title": "Alien: Isolation", "prior_prob": 0.01},
            {"id": 45, "title": "Outlast", "prior_prob": 0.01},
            {"id": 46, "title": "Amnesia: The Dark Descent", "prior_prob": 0.01},
            {"id": 47, "title": "Phasmophobia", "prior_prob": 0.01},

            # Инди игры
            {"id": 48, "title": "Hollow Knight", "prior_prob": 0.01},
            {"id": 49, "title": "Celeste", "prior_prob": 0.01},
            {"id": 50, "title": "Undertale", "prior_prob": 0.01},
            {"id": 51, "title": "Cuphead", "prior_prob": 0.01},
            {"id": 52, "title": "Ori and the Will of the Wisps", "prior_prob": 0.01},
            {"id": 53, "title": "Dead Cells", "prior_prob": 0.01},

            # Спортивные и гонки
            {"id": 54, "title": "FIFA 23", "prior_prob": 0.01},
            {"id": 55, "title": "NBA 2K23", "prior_prob": 0.01},
            {"id": 56, "title": "Forza Horizon 5", "prior_prob": 0.01},
            {"id": 57, "title": "Rocket League", "prior_prob": 0.01},
            {"id": 58, "title": "F1 22", "prior_prob": 0.01},

            # ММО
            {"id": 59, "title": "World of Warcraft", "prior_prob": 0.01},
            {"id": 60, "title": "Guild Wars 2", "prior_prob": 0.01},
            {"id": 61, "title": "Elder Scrolls Online", "prior_prob": 0.01},
            {"id": 62, "title": "Star Wars: The Old Republic", "prior_prob": 0.01},
        ]

        # Свидетельства (признаки игр)
        self.evidences = {
            # Платформы
            1: {"description": "Играете на PC?", "type": "platform"},
            2: {"description": "Играете на игровой консоли?", "type": "platform"},
            3: {"description": "Играете на мобильных устройствах?", "type": "platform"},

            # Жанры
            4: {"description": "Вам нравятся динамичные игры со сражениями?", "type": "genre"},
            5: {"description": "Вам нравятся исследования и решение загадок?", "type": "genre"},
            6: {"description": "Вам нравятся развитие персонажей и интересные сюжеты?", "type": "genre"},
            7: {"description": "Вам нравятся планирование и тактические решения?", "type": "genre"},
            22: {"description": "Вам нравятся сложные головоломки?", "type": "genre"},
            23: {"description": "Вам нравятся симуляторы реальной жизни?", "type": "genre"},
            24: {"description": "Вам нравятся страшные игры с напряженной атмосферой?", "type": "genre"},

            # Сеттинги
            8: {"description": "Вам нравятся рыцари, магия и древние замки?", "type": "setting"},
            9: {"description": "Вам нравятся космос, технологии и будущее?", "type": "setting"},
            10: {"description": "Вам нравятся неоновые города, кибернетика и высокие технологии?", "type": "setting"},
            11: {"description": "Вам нравятся выживание в разрушенном мире?", "type": "setting"},
            25: {"description": "Вам нравятся современные реалистичные миры?", "type": "setting"},
            26: {"description": "Вам нравятся мистические и сверхъестественные истории?", "type": "setting"},

            # Типы игры
            12: {"description": "Вам нравятся игры, где можно играть в одиночку?", "type": "game_type"},
            13: {"description": "Вам нравятся игры с другими игроками онлайн?", "type": "game_type"},
            27: {"description": "Вам нравятся кооперативные игры с друзьями?", "type": "game_type"},

            # Графика
            14: {"description": "Вам нравится реалистичная графика, как в кино?", "type": "graphics"},
            15: {"description": "Вам нравится художественный стиль и уникальный визуал?", "type": "graphics"},
            28: {"description": "Вам нравится пиксельная или ретро-графика?", "type": "graphics"},

            # Цена
            16: {"description": "Предпочитаете бесплатные игры?", "type": "price"},
            17: {"description": "Готовы платить инди-цену (до 1000 рублей)?", "type": "price"},
            18: {"description": "Готовы платить AAA-цену (более 2000 рублей)?", "type": "price"},

            # Продолжительность
            19: {"description": "Предпочитаете короткие игры (менее 10 часов)?", "type": "duration"},
            20: {"description": "Предпочитаете средние игры (10-30 часов)?", "type": "duration"},
            21: {"description": "Предпочитаете долгие игры (30-60 часов)?", "type": "duration"},
            29: {"description": "Предпочитаете бесконечные игры (100+ часов)?", "type": "duration"},

            # Сложность
            30: {"description": "Предпочитаете простые и расслабляющие игры?", "type": "difficulty"},
            31: {"description": "Нравится средний уровень сложности?", "type": "difficulty"},
            32: {"description": "Любите сложные игры, требующие мастерства?", "type": "difficulty"},

            # Эмоции
            33: {"description": "Любите игры, которые вызывают сильные эмоции?", "type": "emotion"},
            34: {"description": "Предпочитаете веселые и юмористические игры?", "type": "emotion"},
            35: {"description": "Нравится мрачная и серьезная атмосфера?", "type": "emotion"},
        }

        # Матрица вероятностей P(E|H) и P(E|not H)
        self.probability_matrix = {
            # PC
            1: self._create_platform_probabilities(
                [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                 57, 58, 59, 60, 61, 62], 0.9, 0.3),

            # Консоль
            2: self._create_platform_probabilities(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 25, 26, 27, 28, 29, 30, 31, 32, 36, 39,
                 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], 0.8, 0.4),

            # Мобильные
            3: self._create_platform_probabilities([13, 36, 39, 54, 55], 0.9, 0.1),

            # Экшен жанр
            4: self._create_genre_probabilities(
                [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 22, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                 54, 55, 56, 57, 58], 0.8, 0.3),

            # Приключенческий жанр
            5: self._create_genre_probabilities(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 39, 43, 44, 45,
                 46, 48, 49, 50, 52], 0.8, 0.3),

            # RPG жанр
            6: self._create_genre_probabilities(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 39, 59, 60, 61, 62], 0.9, 0.2),

            # Стратегии и тактика
            7: self._create_genre_probabilities([7, 8, 19, 20, 21, 22, 23, 24, 40, 41, 42], 0.9, 0.2),

            # Фэнтези сеттинг
            8: self._create_setting_probabilities([1, 3, 4, 6, 7, 8, 9, 10, 19, 23, 59, 60, 61], 0.8, 0.3),

            # Научная фантастика сеттинг
            9: self._create_setting_probabilities([2, 5, 7, 20, 21, 24, 31, 32, 37, 44, 62], 0.8, 0.3),

            # Киберпанк сеттинг
            10: self._create_setting_probabilities([2, 48], 0.9, 0.2),

            # Постапокалипсис
            11: self._create_setting_probabilities([4, 14, 16, 26, 43], 0.8, 0.3),

            # Одиночная игра
            12: self._create_game_type_probabilities(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53], 0.9, 0.2),

            # Многопользовательская
            13: self._create_game_type_probabilities(
                [10, 11, 13, 19, 23, 24, 36, 39, 47, 54, 55, 56, 57, 58, 59, 60, 61, 62], 0.8, 0.3),

            # Кооператив
            27: self._create_game_type_probabilities([7, 8, 13, 22, 23, 24, 27, 36, 39, 47, 57, 59, 60, 61, 62], 0.7,
                                                     0.4),

            # Реалистичная графика
            14: self._create_graphics_probabilities(
                [1, 2, 4, 5, 6, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 36, 37, 38, 40, 41, 42, 43, 44, 54, 55,
                 56, 57, 58, 59, 60, 61, 62], 0.8, 0.3),

            # Художественный стиль
            15: self._create_graphics_probabilities(
                [3, 7, 8, 9, 10, 18, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 45, 46, 48, 49, 50, 51, 52, 53],
                0.9, 0.2),

            # Пазлы и логика
            22: self._create_genre_probabilities([31, 32, 33, 34, 35], 0.9, 0.1),

            # Симуляторы
            23: self._create_genre_probabilities([36, 37, 38, 39, 40, 41, 42, 54, 55, 56, 57, 58], 0.8, 0.3),

            # Хорроры
            24: self._create_genre_probabilities([43, 44, 45, 46, 47], 0.9, 0.1),

            # Современный сеттинг
            25: self._create_setting_probabilities([11, 12, 15, 25, 26, 27, 28, 29, 36, 54, 55, 56, 57, 58], 0.8, 0.3),

            # Мистика
            26: self._create_setting_probabilities([6, 25, 26, 27, 28, 29, 30, 45, 46], 0.8, 0.3),

            # Короткие игры
            19: self._create_duration_probabilities([25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 45, 46, 50], 0.7, 0.4),

            # Долгие игры
            21: self._create_duration_probabilities(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 19, 20, 21, 22, 23, 24, 39, 59, 60, 61, 62], 0.8, 0.3),

            # Бесконечные игры
            29: self._create_duration_probabilities(
                [13, 19, 20, 21, 23, 36, 37, 38, 39, 40, 41, 54, 55, 56, 57, 58, 59, 60, 61, 62], 0.8, 0.3),

            # Простая сложность
            30: self._create_difficulty_probabilities(
                [25, 26, 27, 28, 29, 30, 36, 37, 38, 39, 40, 41, 42, 54, 55, 56, 57, 58], 0.7, 0.4),

            # Высокая сложность
            32: self._create_difficulty_probabilities(
                [3, 7, 8, 18, 19, 20, 21, 22, 23, 31, 32, 33, 34, 35, 48, 49, 51, 53], 0.8, 0.3),

            # Эмоциональные игры
            33: self._create_emotion_probabilities(
                [1, 2, 5, 6, 9, 10, 15, 16, 17, 25, 26, 27, 28, 29, 30, 39, 43, 44, 45, 46, 50], 0.8, 0.3),

            # Веселые игры
            34: self._create_emotion_probabilities([13, 18, 36, 39, 50, 51, 57], 0.8, 0.3),

            # Мрачные игры
            35: self._create_emotion_probabilities([1, 2, 3, 4, 11, 14, 16, 26, 43, 44, 45, 46], 0.8, 0.3),
        }

        # Пороги для правил останова
        self.M1 = 0.4  # Порог для правдоподобной гипотезы
        self.M2 = 0.2  # Порог для невозможности выбора

    def _create_platform_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для платформ"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def _create_genre_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для жанров"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def _create_setting_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для сеттингов"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def _create_game_type_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для типов игры"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def _create_graphics_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для графики"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def _create_duration_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для продолжительности"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def _create_difficulty_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для сложности"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def _create_emotion_probabilities(self, game_ids: List[int], p_plus: float, p_minus: float) -> Dict[
        int, Tuple[float, float]]:
        """Создает вероятности для эмоций"""
        return {i - 1: (p_plus, p_minus) for i in game_ids}

    def calculate_evidence_cost(self, current_probs: List[float], evidence_id: int) -> float:
        """Рассчитывает цену свидетельства C(E) = sum |P(H|E) - P(H|not E)|"""
        total_cost = 0.0

        for i, hyp_prob in enumerate(current_probs):
            if evidence_id in self.probability_matrix and i in self.probability_matrix[evidence_id]:
                p_plus, p_minus = self.probability_matrix[evidence_id][i]

                # P(H|E) и P(H|not E) по формуле Байеса
                p_h_given_e = (p_plus * hyp_prob) / (p_plus * hyp_prob + p_minus * (1 - hyp_prob))
                p_h_given_not_e = ((1 - p_plus) * hyp_prob) / ((1 - p_plus) * hyp_prob + (1 - p_minus) * (1 - hyp_prob))

                total_cost += abs(p_h_given_e - p_h_given_not_e)

        return total_cost

    def update_probabilities(self, current_probs: List[float], evidence_id: int, answer: int) -> List[float]:
        """Обновляет вероятности гипотез на основе ответа пользователя"""
        new_probs = []

        for i, hyp_prob in enumerate(current_probs):
            if evidence_id in self.probability_matrix and i in self.probability_matrix[evidence_id]:
                p_plus, p_minus = self.probability_matrix[evidence_id][i]

                # Преобразуем ответ по 5-балльной шкале в вероятность [0, 1]
                user_prob = (answer - 1) / 4.0  # 1->0, 2->0.25, 3->0.5, 4->0.75, 5->1

                # Взвешенное обновление вероятности
                likelihood = user_prob * p_plus + (1 - user_prob) * p_minus

                # Применяем формулу Байеса
                numerator = likelihood * hyp_prob
                denominator = numerator + (user_prob * p_minus + (1 - user_prob) * p_plus) * (1 - hyp_prob)

                if denominator > 0:
                    new_prob = numerator / denominator
                else:
                    new_prob = hyp_prob  # fallback

                new_probs.append(new_prob)
            else:
                new_probs.append(hyp_prob)

        # Нормализация
        total = sum(new_probs)
        if total > 0:
            new_probs = [p / total for p in new_probs]

        return new_probs

    def check_stopping_conditions(self, probabilities: List[float]) -> Tuple[bool, int]:
        """Проверяет условия останова и возвращает (should_stop, best_hypothesis)"""
        max_prob = max(probabilities)
        best_hyp = probabilities.index(max_prob)

        # 1. Останов по наиболее вероятной гипотезе
        if max_prob > self.M1:
            return True, best_hyp

        # 2. Проверка других условий (например, слишком много вопросов)
        return False, best_hyp

    def get_next_question(self, current_probs: List[float], asked_questions: Dict[int, int]) -> Dict[str, Any]:
        """Получает следующий вопрос на основе текущих вероятностей"""
        available_evidences = [eid for eid in self.evidences if eid not in asked_questions]

        if not available_evidences:
            return None

        # Выбираем свидетельство с максимальной ценой
        best_evidence = None
        best_cost = -1

        for evidence_id in available_evidences:
            cost = self.calculate_evidence_cost(current_probs, evidence_id)
            if cost > best_cost:
                best_cost = cost
                best_evidence = evidence_id

        if best_evidence is None:
            return None

        return {
            "id": best_evidence,
            "text": self.evidences[best_evidence]["description"],
            "type": self.evidences[best_evidence]["type"]
        }

    def get_recommendation(self, current_probs: List[float], user_answers: Dict[int, int]) -> Dict[str, Any]:
        """Основной алгоритм рекомендации с использованием текущих вероятностей"""
        asked_questions = set(user_answers.keys())

        # Проверяем условия останова
        should_stop, best_hyp = self.check_stopping_conditions(current_probs)

        if should_stop or len(asked_questions) >= 15:  # Максимум 15 вопросов
            # Формирование результатов
            best_game = self.hypotheses[best_hyp]

            # Сортировка всех игр по вероятности
            ranked_games = []
            for i, prob in enumerate(current_probs):
                ranked_games.append({
                    "game": self.hypotheses[i],
                    "probability": prob,
                    "score": int(prob * 100)
                })

            ranked_games.sort(key=lambda x: x["probability"], reverse=True)

            return {
                "recommendation": best_game,
                "confidence": current_probs[best_hyp],
                "all_recommendations": ranked_games[:10],  # Показываем топ-10
                "asked_questions": list(asked_questions),
                "finished": True
            }
        else:
            # Получаем следующий вопрос
            next_question = self.get_next_question(current_probs, user_answers)
            if next_question:
                return {
                    "next_question": next_question,
                    "current_probs": current_probs,
                    "asked_questions": list(asked_questions),
                    "finished": False
                }
            else:
                # Если вопросов больше нет, возвращаем результаты
                return self.get_recommendation(current_probs, user_answers)


# Создаем экземпляр системы рекомендаций
bayesian_system = BayesianGameRecommendationSystem()

# Глобальная переменная для хранения состояния сессии
user_sessions = {}


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/start", response_class=HTMLResponse)
async def start_survey(request: Request):
    """Начало опроса"""
    session_id = str(hash(str(request.client)))
    initial_probs = [hyp["prior_prob"] for hyp in bayesian_system.hypotheses]

    user_sessions[session_id] = {
        "asked_questions": {},
        "current_probs": initial_probs
    }

    # Получаем первый вопрос
    result = bayesian_system.get_recommendation(initial_probs, {})

    return templates.TemplateResponse("question.html", {
        "request": request,
        "question": result["next_question"],
        "session_id": session_id,
        "progress": 1
    })


@app.post("/answer")
async def process_answer(request: Request):
    """Обработка ответа пользователя"""
    form = await request.form()
    session_id = form.get("session_id")
    question_id = int(form.get("question_id"))
    answer = int(form.get("answer"))

    if session_id not in user_sessions:
        return {"error": "Сессия не найдена"}

    # Получаем текущее состояние сессии
    session = user_sessions[session_id]
    current_probs = session["current_probs"]
    asked_questions = session["asked_questions"]

    # ОБНОВЛЯЕМ вероятности на основе ответа
    updated_probs = bayesian_system.update_probabilities(current_probs, question_id, answer)

    # Обновляем сессию
    asked_questions[question_id] = answer
    session["current_probs"] = updated_probs
    session["asked_questions"] = asked_questions

    # Получаем следующую рекомендацию с ОБНОВЛЕННЫМИ вероятностями
    result = bayesian_system.get_recommendation(updated_probs, asked_questions)

    if result.get("finished"):
        # Показываем результаты
        return templates.TemplateResponse("results.html", {
            "request": request,
            "recommendation": result["recommendation"],
            "confidence": result["confidence"],
            "all_recommendations": result["all_recommendations"],
            "asked_questions_count": len(result["asked_questions"])
        })
    else:
        # Показываем следующий вопрос
        return templates.TemplateResponse("question.html", {
            "request": request,
            "question": result["next_question"],
            "session_id": session_id,
            "progress": len(asked_questions) + 1
        })


@app.get("/restart")
async def restart(request: Request):
    """Перезапуск опроса"""
    session_id = str(hash(str(request.client)))
    initial_probs = [hyp["prior_prob"] for hyp in bayesian_system.hypotheses]

    user_sessions[session_id] = {
        "asked_questions": {},
        "current_probs": initial_probs
    }

    result = bayesian_system.get_recommendation(initial_probs, {})

    return templates.TemplateResponse("question.html", {
        "request": request,
        "question": result["next_question"],
        "session_id": session_id,
        "progress": 1
    })


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)