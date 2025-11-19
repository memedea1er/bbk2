from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Dict, Any, Tuple

app = FastAPI(title="Game Recommendation System - Bayesian")

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class BayesianGameRecommendationSystem:
    def __init__(self):
        # База знаний: гипотезы (игры) и свидетельства (признаки)
        self.hypotheses = [
            # RPG игры (6)
            {"id": 1, "title": "The Witcher 3: Wild Hunt", "prior_prob": 0.05},
            {"id": 2, "title": "Cyberpunk 2077", "prior_prob": 0.05},
            {"id": 3, "title": "Elden Ring", "prior_prob": 0.05},
            {"id": 4, "title": "Skyrim", "prior_prob": 0.05},
            {"id": 5, "title": "Mass Effect: Legendary Edition", "prior_prob": 0.05},
            {"id": 6, "title": "Disco Elysium", "prior_prob": 0.05},

            # Экшен игры (6)
            {"id": 7, "title": "Counter-Strike 2", "prior_prob": 0.05},
            {"id": 8, "title": "The Last of Us Part I", "prior_prob": 0.05},
            {"id": 9, "title": "Fortnite", "prior_prob": 0.05},
            {"id": 10, "title": "DOOM Eternal", "prior_prob": 0.05},
            {"id": 11, "title": "Grand Theft Auto V", "prior_prob": 0.05},
            {"id": 12, "title": "Call of Duty: Warzone", "prior_prob": 0.05},

            # Стратегии (5)
            {"id": 13, "title": "Civilization VI", "prior_prob": 0.05},
            {"id": 14, "title": "StarCraft II", "prior_prob": 0.05},
            {"id": 15, "title": "XCOM 2", "prior_prob": 0.05},
            {"id": 16, "title": "Crusader Kings III", "prior_prob": 0.05},
            {"id": 17, "title": "Total War: Warhammer III", "prior_prob": 0.05},

            # Приключенческие игры (5)
            {"id": 18, "title": "The Legend of Zelda: Breath of the Wild", "prior_prob": 0.05},
            {"id": 19, "title": "Red Dead Redemption 2", "prior_prob": 0.05},
            {"id": 20, "title": "God of War (2018)", "prior_prob": 0.05},
            {"id": 21, "title": "Uncharted 4: A Thief's End", "prior_prob": 0.05},
            {"id": 22, "title": "Horizon Zero Dawn", "prior_prob": 0.05},

            # Инди игры (5)
            {"id": 23, "title": "Hades", "prior_prob": 0.05},
            {"id": 24, "title": "Stardew Valley", "prior_prob": 0.05},
            {"id": 25, "title": "Celeste", "prior_prob": 0.05},
            {"id": 26, "title": "Hollow Knight", "prior_prob": 0.05},
            {"id": 27, "title": "Undertale", "prior_prob": 0.05},

            # Симуляторы (5)
            {"id": 28, "title": "The Sims 4", "prior_prob": 0.05},
            {"id": 29, "title": "Microsoft Flight Simulator", "prior_prob": 0.05},
            {"id": 30, "title": "Euro Truck Simulator 2", "prior_prob": 0.05},
            {"id": 31, "title": "Cities: Skylines", "prior_prob": 0.05},
            {"id": 32, "title": "Farming Simulator 22", "prior_prob": 0.05},

            # Хоррор игры (4)
            {"id": 33, "title": "Resident Evil Village", "prior_prob": 0.05},
            {"id": 34, "title": "Silent Hill 2", "prior_prob": 0.05},
            {"id": 35, "title": "Outlast", "prior_prob": 0.05},
            {"id": 36, "title": "Alien: Isolation", "prior_prob": 0.05},

            # Гонки (4)
            {"id": 37, "title": "Forza Horizon 5", "prior_prob": 0.05},
            {"id": 38, "title": "Gran Turismo 7", "prior_prob": 0.05},
            {"id": 39, "title": "Mario Kart 8 Deluxe", "prior_prob": 0.05},
            {"id": 40, "title": "Need for Speed: Heat", "prior_prob": 0.05},

            # Спортивные (4)
            {"id": 41, "title": "FIFA 23", "prior_prob": 0.05},
            {"id": 42, "title": "NBA 2K23", "prior_prob": 0.05},
            {"id": 43, "title": "Rocket League", "prior_prob": 0.05},
            {"id": 44, "title": "Tony Hawk's Pro Skater 1+2", "prior_prob": 0.05},

            # ММО (3)
            {"id": 45, "title": "World of Warcraft", "prior_prob": 0.05},
            {"id": 46, "title": "Final Fantasy XIV", "prior_prob": 0.05},
            {"id": 47, "title": "Guild Wars 2", "prior_prob": 0.05},

            # Выживание (3)
            {"id": 48, "title": "Minecraft", "prior_prob": 0.05},
            {"id": 49, "title": "Rust", "prior_prob": 0.05},
            {"id": 50, "title": "Valheim", "prior_prob": 0.05},
        ]

        # Свидетельства (признаки игр) с группировкой по категориям
        self.probability_matrix = {
            # PC (1)
            1: {**{i: (0.9, 0.2) for i in
                   [1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 14, 15, 16, 17, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35, 37, 40,
                    45, 46, 47, 48, 49, 50]},
                **{8: (0.7, 0.4), 9: (0.8, 0.3), 12: (0.8, 0.3), 18: (0.3, 0.7), 19: (0.8, 0.3),
                   20: (0.3, 0.7), 21: (0.3, 0.7), 22: (0.8, 0.3), 33: (0.8, 0.3), 34: (0.3, 0.7),
                   36: (0.8, 0.3), 38: (0.2, 0.8), 39: (0.1, 0.9), 41: (0.7, 0.4), 42: (0.7, 0.4),
                   43: (0.9, 0.2), 44: (0.8, 0.3)}},

            # Консоль (2)
            2: {**{i: (0.8, 0.3) for i in
                   [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 33, 34, 36, 37, 38, 39, 41, 42, 44]},
                **{6: (0.7, 0.4), 7: (0.1, 0.9), 13: (0.6, 0.5), 14: (0.2, 0.8), 15: (0.7, 0.4),
                   16: (0.3, 0.7), 17: (0.7, 0.4), 23: (0.8, 0.3), 24: (0.7, 0.4), 25: (0.7, 0.4),
                   26: (0.7, 0.4), 27: (0.5, 0.6), 28: (0.4, 0.7), 29: (0.2, 0.8), 30: (0.3, 0.7),
                   31: (0.4, 0.7), 32: (0.3, 0.7), 35: (0.7, 0.4), 40: (0.8, 0.3), 43: (0.8, 0.3),
                   45: (0.1, 0.9), 46: (0.8, 0.3), 47: (0.3, 0.7), 48: (0.8, 0.3), 49: (0.7, 0.4),
                   50: (0.8, 0.3)}},

            # Мобильные (3)
            3: {**{i: (0.9, 0.2) for i in [9, 12, 24, 39, 41, 42, 43, 48]},
                **{i: (0.1, 0.9) for i in
                   [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30,
                    31, 32, 33, 34, 35, 36, 37, 38, 40, 44, 45, 46, 47, 49, 50]}},

            # Экшен жанр (4)
            4: {**{i: (0.9, 0.2) for i in
                   [7, 8, 9, 10, 11, 12, 18, 19, 20, 21, 22, 23, 33, 34, 35, 36, 37, 38, 39, 40, 43]},
                **{1: (0.7, 0.4), 2: (0.8, 0.3), 3: (0.9, 0.2), 4: (0.6, 0.5), 5: (0.7, 0.4),
                   6: (0.2, 0.8), 13: (0.3, 0.7), 14: (0.4, 0.6), 15: (0.6, 0.5), 16: (0.2, 0.8),
                   17: (0.7, 0.4), 24: (0.1, 0.9), 25: (0.5, 0.6), 26: (0.7, 0.4), 27: (0.2, 0.8),
                   28: (0.1, 0.9), 29: (0.2, 0.8), 30: (0.1, 0.9), 31: (0.1, 0.9), 32: (0.1, 0.9),
                   41: (0.8, 0.3), 42: (0.8, 0.3), 44: (0.9, 0.2), 45: (0.5, 0.6), 46: (0.6, 0.5),
                   47: (0.5, 0.6), 48: (0.4, 0.7), 49: (0.7, 0.4), 50: (0.6, 0.5)}},

            # Приключенческий жанр (5)
            5: {**{i: (0.9, 0.2) for i in [1, 4, 6, 18, 19, 20, 21, 22, 25, 26, 27, 34, 36]},
                **{2: (0.7, 0.4), 3: (0.8, 0.3), 5: (0.8, 0.3), 7: (0.1, 0.9), 8: (0.9, 0.2),
                   9: (0.2, 0.8), 10: (0.3, 0.7), 11: (0.7, 0.4), 12: (0.1, 0.9), 13: (0.4, 0.6),
                   14: (0.2, 0.8), 15: (0.5, 0.6), 16: (0.6, 0.5), 17: (0.4, 0.6), 23: (0.8, 0.3),
                   24: (0.3, 0.7), 28: (0.4, 0.7), 29: (0.6, 0.5), 30: (0.5, 0.6), 31: (0.4, 0.7),
                   32: (0.3, 0.7), 33: (0.7, 0.4), 35: (0.6, 0.5), 37: (0.5, 0.6), 38: (0.4, 0.7),
                   39: (0.6, 0.5), 40: (0.5, 0.6), 41: (0.2, 0.8), 42: (0.2, 0.8), 43: (0.1, 0.9),
                   44: (0.7, 0.4), 45: (0.8, 0.3), 46: (0.9, 0.2), 47: (0.8, 0.3), 48: (0.8, 0.3),
                   49: (0.5, 0.6), 50: (0.8, 0.3)}},

            # RPG жанр (6)
            6: {**{i: (0.9, 0.2) for i in [1, 2, 3, 4, 5, 6, 45, 46, 47]},
                **{7: (0.1, 0.9), 8: (0.6, 0.5), 9: (0.1, 0.9), 10: (0.2, 0.8), 11: (0.5, 0.6),
                   12: (0.1, 0.9), 13: (0.3, 0.7), 14: (0.2, 0.8), 15: (0.4, 0.6), 16: (0.8, 0.3),
                   17: (0.5, 0.6), 18: (0.7, 0.4), 19: (0.6, 0.5), 20: (0.7, 0.4), 21: (0.4, 0.7),
                   22: (0.6, 0.5), 23: (0.9, 0.2), 24: (0.4, 0.7), 25: (0.2, 0.8), 26: (0.3, 0.7),
                   27: (0.8, 0.3), 28: (0.3, 0.7), 29: (0.1, 0.9), 30: (0.1, 0.9), 31: (0.1, 0.9),
                   32: (0.1, 0.9), 33: (0.3, 0.7), 34: (0.4, 0.7), 35: (0.2, 0.8), 36: (0.3, 0.7),
                   37: (0.1, 0.9), 38: (0.1, 0.9), 39: (0.1, 0.9), 40: (0.1, 0.9), 41: (0.1, 0.9),
                   42: (0.1, 0.9), 43: (0.1, 0.9), 44: (0.1, 0.9), 48: (0.4, 0.7), 49: (0.3, 0.7),
                   50: (0.7, 0.4)}},

            # Стратегии жанр (7)
            7: {**{i: (0.9, 0.2) for i in [13, 14, 15, 16, 17, 31]},
                **{1: (0.2, 0.8), 2: (0.1, 0.9), 3: (0.1, 0.9), 4: (0.1, 0.9), 5: (0.1, 0.9),
                   6: (0.1, 0.9), 7: (0.3, 0.7), 8: (0.1, 0.9), 9: (0.2, 0.8), 10: (0.1, 0.9),
                   11: (0.1, 0.9), 12: (0.3, 0.7), 18: (0.1, 0.9), 19: (0.1, 0.9), 20: (0.1, 0.9),
                   21: (0.1, 0.9), 22: (0.1, 0.9), 23: (0.1, 0.9), 24: (0.4, 0.7), 25: (0.1, 0.9),
                   26: (0.1, 0.9), 27: (0.1, 0.9), 28: (0.6, 0.5), 29: (0.5, 0.6), 30: (0.4, 0.7),
                   32: (0.7, 0.4), 33: (0.1, 0.9), 34: (0.1, 0.9), 35: (0.1, 0.9), 36: (0.1, 0.9),
                   37: (0.1, 0.9), 38: (0.1, 0.9), 39: (0.1, 0.9), 40: (0.1, 0.9), 41: (0.3, 0.7),
                   42: (0.3, 0.7), 43: (0.2, 0.8), 44: (0.1, 0.9), 45: (0.4, 0.7), 46: (0.3, 0.7),
                   47: (0.4, 0.7), 48: (0.5, 0.6), 49: (0.4, 0.7), 50: (0.6, 0.5)}},

            # Фэнтези сеттинг (8)
            8: {**{i: (0.9, 0.2) for i in [1, 3, 4, 6, 17, 23, 26, 45, 47]},
                **{2: (0.1, 0.9), 5: (0.2, 0.8), 7: (0.1, 0.9), 8: (0.1, 0.9), 9: (0.1, 0.9),
                   10: (0.1, 0.9), 11: (0.1, 0.9), 12: (0.1, 0.9), 13: (0.3, 0.7), 14: (0.1, 0.9),
                   15: (0.1, 0.9), 16: (0.8, 0.3), 18: (0.9, 0.2), 19: (0.1, 0.9), 20: (0.9, 0.2),
                   21: (0.1, 0.9), 22: (0.1, 0.9), 24: (0.3, 0.7), 25: (0.1, 0.9), 27: (0.8, 0.3),
                   28: (0.1, 0.9), 29: (0.1, 0.9), 30: (0.1, 0.9), 31: (0.1, 0.9), 32: (0.1, 0.9),
                   33: (0.1, 0.9), 34: (0.1, 0.9), 35: (0.1, 0.9), 36: (0.1, 0.9), 37: (0.1, 0.9),
                   38: (0.1, 0.9), 39: (0.8, 0.3), 40: (0.1, 0.9), 41: (0.1, 0.9), 42: (0.1, 0.9),
                   43: (0.1, 0.9), 44: (0.1, 0.9), 46: (0.9, 0.2), 48: (0.8, 0.3), 49: (0.1, 0.9),
                   50: (0.9, 0.2)}},

            # Научная фантастика сеттинг (9)
            9: {**{i: (0.9, 0.2) for i in [2, 5, 14, 15, 29, 36, 46]},
                **{1: (0.1, 0.9), 3: (0.1, 0.9), 4: (0.1, 0.9), 6: (0.1, 0.9), 7: (0.1, 0.9),
                   8: (0.1, 0.9), 9: (0.1, 0.9), 10: (0.9, 0.2), 11: (0.7, 0.4), 12: (0.1, 0.9),
                   13: (0.4, 0.7), 16: (0.1, 0.9), 17: (0.3, 0.7), 18: (0.1, 0.9), 19: (0.1, 0.9),
                   20: (0.1, 0.9), 21: (0.1, 0.9), 22: (0.9, 0.2), 23: (0.1, 0.9), 24: (0.1, 0.9),
                   25: (0.1, 0.9), 26: (0.1, 0.9), 27: (0.1, 0.9), 28: (0.8, 0.3), 30: (0.1, 0.9),
                   31: (0.7, 0.4), 32: (0.1, 0.9), 33: (0.1, 0.9), 34: (0.1, 0.9), 35: (0.1, 0.9),
                   37: (0.8, 0.3), 38: (0.8, 0.3), 39: (0.1, 0.9), 40: (0.8, 0.3), 41: (0.1, 0.9),
                   42: (0.1, 0.9), 43: (0.9, 0.2), 44: (0.1, 0.9), 45: (0.9, 0.2), 47: (0.1, 0.9),
                   48: (0.1, 0.9), 49: (0.1, 0.9), 50: (0.1, 0.9)}},

            # Киберпанк сеттинг (10)
            10: {**{i: (0.9, 0.2) for i in [2, 6]},
                 **{i: (0.1, 0.9) for i in range(1, 51) if i not in [2, 6]}},

            # Постапокалипсис сеттинг (11)
            11: {**{i: (0.9, 0.2) for i in [8, 33, 35, 48]},
                 **{1: (0.1, 0.9), 2: (0.1, 0.9), 3: (0.1, 0.9), 4: (0.1, 0.9), 5: (0.1, 0.9),
                    6: (0.1, 0.9), 7: (0.1, 0.9), 9: (0.1, 0.9), 10: (0.1, 0.9), 11: (0.7, 0.4),
                    12: (0.1, 0.9), 13: (0.1, 0.9), 14: (0.1, 0.9), 15: (0.1, 0.9), 16: (0.1, 0.9),
                    17: (0.1, 0.9), 18: (0.1, 0.9), 19: (0.7, 0.4), 20: (0.1, 0.9), 21: (0.1, 0.9),
                    22: (0.1, 0.9), 23: (0.1, 0.9), 24: (0.1, 0.9), 25: (0.1, 0.9), 26: (0.1, 0.9),
                    27: (0.1, 0.9), 28: (0.1, 0.9), 29: (0.1, 0.9), 30: (0.1, 0.9), 31: (0.1, 0.9),
                    32: (0.1, 0.9), 34: (0.1, 0.9), 36: (0.9, 0.2), 37: (0.1, 0.9), 38: (0.1, 0.9),
                    39: (0.1, 0.9), 40: (0.1, 0.9), 41: (0.1, 0.9), 42: (0.1, 0.9), 43: (0.1, 0.9),
                    44: (0.1, 0.9), 45: (0.1, 0.9), 46: (0.1, 0.9), 47: (0.1, 0.9), 49: (0.9, 0.2),
                    50: (0.8, 0.3)}},

            # Одиночная игра (12)
            12: {**{i: (0.9, 0.2) for i in
                    [1, 2, 3, 4, 5, 6, 8, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                     34, 35, 36, 48, 50]},
                 **{7: (0.1, 0.9), 9: (0.2, 0.8), 10: (0.8, 0.3), 11: (0.8, 0.3), 12: (0.1, 0.9),
                    14: (0.3, 0.7), 17: (0.8, 0.3), 37: (0.8, 0.3), 38: (0.8, 0.3), 39: (0.7, 0.4),
                    40: (0.8, 0.3), 41: (0.4, 0.7), 42: (0.4, 0.7), 43: (0.2, 0.8), 44: (0.8, 0.3),
                    45: (0.3, 0.7), 46: (0.4, 0.7), 47: (0.3, 0.7), 49: (0.2, 0.8)}},

            # Многопользовательская (13)
            13: {**{i: (0.9, 0.2) for i in [7, 9, 12, 14, 41, 42, 43, 45, 46, 47, 49]},
                 **{1: (0.3, 0.7), 2: (0.3, 0.7), 3: (0.8, 0.3), 4: (0.2, 0.8), 5: (0.2, 0.8),
                    6: (0.0, 0.95), 8: (0.1, 0.9), 10: (0.6, 0.5), 11: (0.7, 0.4), 13: (0.4, 0.7),
                    15: (0.3, 0.7), 16: (0.2, 0.8), 17: (0.7, 0.4), 18: (0.1, 0.9), 19: (0.3, 0.7),
                    20: (0.1, 0.9), 21: (0.1, 0.9), 22: (0.1, 0.9), 23: (0.1, 0.9), 24: (0.4, 0.7),
                    25: (0.1, 0.9), 26: (0.1, 0.9), 27: (0.1, 0.9), 28: (0.6, 0.5), 29: (0.3, 0.7),
                    30: (0.4, 0.7), 31: (0.2, 0.8), 32: (0.5, 0.6), 33: (0.1, 0.9), 34: (0.1, 0.9),
                    35: (0.1, 0.9), 36: (0.1, 0.9), 37: (0.8, 0.3), 38: (0.8, 0.3), 39: (0.9, 0.2),
                    40: (0.8, 0.3), 44: (0.2, 0.8), 48: (0.8, 0.3), 50: (0.7, 0.4)}},

            # Фотореалистичная графика (14)
            14: {**{i: (0.9, 0.2) for i in
                    [1, 2, 3, 4, 5, 8, 10, 11, 13, 15, 17, 19, 20, 21, 22, 29, 33, 36, 37, 38, 40, 41, 42]},
                 **{6: (0.3, 0.7), 7: (0.9, 0.2), 9: (0.8, 0.3), 12: (0.9, 0.2), 14: (0.8, 0.3),
                    16: (0.7, 0.4), 18: (0.8, 0.3), 23: (0.4, 0.7), 24: (0.2, 0.8), 25: (0.1, 0.9),
                    26: (0.3, 0.7), 27: (0.1, 0.9), 28: (0.8, 0.3), 30: (0.8, 0.3), 31: (0.7, 0.4),
                    32: (0.8, 0.3), 34: (0.7, 0.4), 35: (0.8, 0.3), 39: (0.6, 0.5), 43: (0.8, 0.3),
                    44: (0.8, 0.3), 45: (0.5, 0.6), 46: (0.8, 0.3), 47: (0.6, 0.5), 48: (0.1, 0.9),
                    49: (0.8, 0.3), 50: (0.4, 0.7)}},

            # Стилизованная графика (15)
            15: {**{i: (0.9, 0.2) for i in [6, 9, 18, 23, 24, 25, 26, 27, 39, 43, 48]},
                 **{1: (0.3, 0.7), 2: (0.3, 0.7), 3: (0.4, 0.6), 4: (0.7, 0.3), 5: (0.2, 0.8),
                    7: (0.2, 0.8), 8: (0.3, 0.7), 10: (0.3, 0.7), 11: (0.2, 0.8), 12: (0.2, 0.8),
                    13: (0.4, 0.7), 14: (0.3, 0.7), 15: (0.5, 0.6), 16: (0.6, 0.5), 17: (0.6, 0.5),
                    19: (0.2, 0.8), 20: (0.3, 0.7), 21: (0.3, 0.7), 22: (0.2, 0.8), 28: (0.3, 0.7),
                    29: (0.2, 0.8), 30: (0.3, 0.7), 31: (0.4, 0.7), 32: (0.3, 0.7), 33: (0.3, 0.7),
                    34: (0.4, 0.7), 35: (0.3, 0.7), 36: (0.3, 0.7), 37: (0.2, 0.8), 38: (0.2, 0.8),
                    40: (0.2, 0.8), 41: (0.3, 0.7), 42: (0.3, 0.7), 44: (0.7, 0.4), 45: (0.7, 0.4),
                    46: (0.3, 0.7), 47: (0.5, 0.6), 49: (0.3, 0.7), 50: (0.8, 0.3)}},
        }

        # Группы с взаимоисключающими вопросами
        self.exclusive_groups = {
            "platform", "setting", "graphics", "price", "duration"
        }

        # Матрица вероятностей P(E|H) и P(E|not H) - усиленные значения
        self.probability_matrix = {
            # PC
            1: {
                1: (0.95, 0.1), 2: (0.9, 0.2), 3: (0.9, 0.2), 4: (0.8, 0.3),
                5: (0.8, 0.2), 6: (0.9, 0.1), 7: (1.0, 0.05), 8: (0.7, 0.3),
                9: (0.8, 0.2), 10: (0.9, 0.1)
            },
            # Консоль
            2: {
                1: (0.8, 0.3), 2: (0.9, 0.1), 3: (0.8, 0.2), 4: (0.9, 0.1),
                5: (0.8, 0.2), 6: (0.7, 0.3), 7: (0.1, 0.9), 8: (0.9, 0.1),
                9: (0.9, 0.1), 10: (0.8, 0.2)
            },
            # Мобильные
            3: {
                1: (0.1, 0.9), 2: (0.1, 0.9), 3: (0.1, 0.9), 4: (0.2, 0.8),
                5: (0.1, 0.9), 6: (0.1, 0.9), 7: (0.0, 0.95), 8: (0.1, 0.9),
                9: (0.95, 0.05), 10: (0.1, 0.9)
            },
            # Экшен жанр
            4: {
                1: (0.8, 0.3), 2: (0.9, 0.2), 3: (0.95, 0.1), 4: (0.7, 0.4),
                5: (0.8, 0.3), 6: (0.2, 0.8), 7: (1.0, 0.05), 8: (0.95, 0.1),
                9: (1.0, 0.05), 10: (1.0, 0.05)
            },
            # Приключенческий жанр
            5: {
                1: (0.9, 0.2), 2: (0.8, 0.3), 3: (0.9, 0.2), 4: (0.95, 0.1),
                5: (0.9, 0.2), 6: (0.95, 0.1), 7: (0.1, 0.9), 8: (0.9, 0.2),
                9: (0.3, 0.7), 10: (0.2, 0.8)
            },
            # RPG жанр
            6: {
                1: (0.95, 0.05), 2: (0.95, 0.05), 3: (0.9, 0.1), 4: (0.95, 0.05),
                5: (0.95, 0.05), 6: (1.0, 0.01), 7: (0.1, 0.9), 8: (0.8, 0.3),
                9: (0.1, 0.9), 10: (0.4, 0.6)
            },
            # Фэнтези сеттинг
            8: {
                1: (0.95, 0.1), 2: (0.1, 0.9), 3: (0.95, 0.1), 4: (0.95, 0.1),
                5: (0.2, 0.8), 6: (0.1, 0.9), 7: (0.1, 0.9), 8: (0.3, 0.7),
                9: (0.1, 0.9), 10: (0.2, 0.8)
            },
            # Научная фантастика сеттинг
            9: {
                1: (0.1, 0.9), 2: (0.95, 0.1), 3: (0.1, 0.9), 4: (0.1, 0.9),
                5: (0.95, 0.1), 6: (0.1, 0.9), 7: (0.1, 0.9), 8: (0.2, 0.8),
                9: (0.1, 0.9), 10: (0.95, 0.1)
            },
            # Киберпанк сеттинг
            10: {
                1: (0.1, 0.8), 2: (0.95, 0.1), 3: (0.1, 0.8), 4: (0.1, 0.8),
                5: (0.1, 0.8), 6: (0.8, 0.2), 7: (0.1, 0.8), 8: (0.1, 0.8),
                9: (0.1, 0.8), 10: (0.1, 0.8)
            },
            # Постапокалипсис сеттинг
            11: {
                1: (0.1, 0.8), 2: (0.1, 0.8), 3: (0.1, 0.8), 4: (0.1, 0.8),
                5: (0.1, 0.8), 6: (0.1, 0.8), 7: (0.1, 0.8), 8: (0.95, 0.1),
                9: (0.1, 0.8), 10: (0.1, 0.8)
            },
            # Одиночная игра
            12: {
                1: (0.95, 0.1), 2: (0.95, 0.1), 3: (0.9, 0.2), 4: (0.95, 0.1),
                5: (0.95, 0.1), 6: (1.0, 0.05), 7: (0.1, 0.9), 8: (0.95, 0.1),
                9: (0.2, 0.8), 10: (0.9, 0.2)
            },
            # Многопользовательская
            13: {
                1: (0.3, 0.7), 2: (0.3, 0.7), 3: (0.8, 0.3), 4: (0.2, 0.8),
                5: (0.2, 0.8), 6: (0.0, 0.95), 7: (1.0, 0.05), 8: (0.1, 0.9),
                9: (1.0, 0.05), 10: (0.7, 0.4)
            },
            # Фотореалистичная графика
            14: {
                1: (0.95, 0.1), 2: (0.95, 0.1), 3: (0.95, 0.1), 4: (0.8, 0.3),
                5: (0.95, 0.1), 6: (0.3, 0.7), 7: (0.95, 0.1), 8: (0.95, 0.1),
                9: (0.8, 0.3), 10: (0.95, 0.1)
            },
            # Стилизованная графика
            15: {
                1: (0.3, 0.7), 2: (0.3, 0.7), 3: (0.4, 0.6), 4: (0.7, 0.3),
                5: (0.2, 0.8), 6: (0.95, 0.1), 7: (0.2, 0.8), 8: (0.3, 0.7),
                9: (0.6, 0.4), 10: (0.3, 0.7)
            },
        }

        # Пороги для правил останова
        self.M1 = 0.5  # Понижен порог для более быстрого останова
        self.M2 = 0.1

    def calculate_evidence_cost(self, current_probs: List[float], evidence_id: int) -> float:
        """Рассчитывает цену свидетельства C(E) = sum |P(H|E) - P(H|not E)|"""
        total_cost = 0.0

        for i, hyp_prob in enumerate(current_probs):
            if evidence_id in self.probability_matrix and i in self.probability_matrix[evidence_id]:
                p_plus, p_minus = self.probability_matrix[evidence_id][i]

                # P(H|E) и P(H|not E) по формуле Байеса
                p_h_given_e = (p_plus * hyp_prob) / (p_plus * hyp_prob + p_minus * (1 - hyp_prob) + 1e-10)
                p_h_given_not_e = ((1 - p_plus) * hyp_prob) / ((1 - p_plus) * hyp_prob + (1 - p_minus) * (1 - hyp_prob) + 1e-10)

                total_cost += abs(p_h_given_e - p_h_given_not_e)

        return total_cost

    def update_probabilities(self, current_probs: List[float], evidence_id: int, answer: int) -> List[float]:
        """Обновляет вероятности гипотез на основе ответа пользователя"""
        new_probs = []
        total = 0.0

        # Преобразуем ответ по 5-балльной шкале в вес [0, 1]
        # Более агрессивное преобразование для усиления эффекта
        if answer == 1:  # Совсем не нравится
            user_weight = 0.1
        elif answer == 2:  # Скорее не нравится
            user_weight = 0.3
        elif answer == 3:  # Нейтрально
            user_weight = 0.5
        elif answer == 4:  # Скорее нравится
            user_weight = 0.8
        else:  # Очень нравится (5)
            user_weight = 0.95

        for i, hyp_prob in enumerate(current_probs):
            if evidence_id in self.probability_matrix and i in self.probability_matrix[evidence_id]:
                p_plus, p_minus = self.probability_matrix[evidence_id][i]

                # Интерполируем между P(E|H) и P(not E|H)
                likelihood = user_weight * p_plus + (1 - user_weight) * (1 - p_plus)

                # Байесовское обновление с усилением
                new_prob = hyp_prob * likelihood
                new_probs.append(new_prob)
                total += new_prob
            else:
                # Если свидетельство не относится к гипотезе, немного уменьшаем вероятность
                new_probs.append(hyp_prob * 0.95)
                total += hyp_prob * 0.95

        # Нормализация
        if total > 0:
            new_probs = [p / total for p in new_probs]

        return new_probs

    def check_stopping_conditions(self, probabilities: List[float]) -> Tuple[bool, int]:
        """Проверяет условия останова"""
        if not probabilities:
            return True, 0

        max_prob = max(probabilities)
        best_hyp = probabilities.index(max_prob)

        # Останов если максимальная вероятность превышает порог
        if max_prob > self.M1:
            return True, best_hyp

        return False, best_hyp

    def get_available_evidences(self, asked_questions: Dict[int, int]) -> List[int]:
        """Получает доступные свидетельства с учетом взаимоисключающих групп"""
        available = []
        answered_groups = set()

        # Собираем группы, на которые уже ответили
        for q_id, answer in asked_questions.items():
            if q_id in self.evidences:
                group = self.evidences[q_id].get("group")
                if group in self.exclusive_groups and answer >= 4:  # Если ответ "нравится"
                    answered_groups.add(group)

        # Фильтруем доступные вопросы
        for evidence_id, evidence_info in self.evidences.items():
            if evidence_id not in asked_questions:
                group = evidence_info.get("group")
                # Если группа взаимоисключающая и уже есть положительный ответ в этой группе - пропускаем
                if group in self.exclusive_groups and group in answered_groups:
                    continue
                available.append(evidence_id)

        return available

    def get_next_question(self, current_probs: List[float], asked_questions: Dict[int, int]) -> Dict[str, Any]:
        """Получает следующий вопрос на основе текущих вероятностей"""
        available_evidences = self.get_available_evidences(asked_questions)

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
            "type": self.evidences[best_evidence]["type"],
            "group": self.evidences[best_evidence].get("group", "general")
        }

    def get_recommendation(self, current_probs: List[float], user_answers: Dict[int, int]) -> Dict[str, Any]:
        """Основной алгоритм рекомендации"""
        asked_questions = user_answers.copy()

        # Проверяем условия останова
        should_stop, best_hyp = self.check_stopping_conditions(current_probs)

        # Максимум 8 вопросов для более быстрого результата
        max_questions = 8
        if should_stop or len(asked_questions) >= max_questions:
            # Формирование результатов
            best_hyp_index = current_probs.index(max(current_probs))
            best_game = self.hypotheses[best_hyp_index]

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
                "confidence": current_probs[best_hyp_index],
                "all_recommendations": ranked_games[:5],
                "asked_questions": list(asked_questions.keys()),
                "finished": True
            }
        else:
            # Получаем следующий вопрос
            next_question = self.get_next_question(current_probs, asked_questions)
            if next_question:
                return {
                    "next_question": next_question,
                    "current_probs": current_probs,
                    "asked_questions": list(asked_questions.keys()),
                    "finished": False
                }
            else:
                # Если вопросов больше нет, возвращаем результаты
                return self.get_recommendation(current_probs, asked_questions)


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