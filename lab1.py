# -*- coding: utf-8 -*-
class GameRecommendationSystem:
    def __init__(self):
        # Расширенная база данных видеоигр
        self.games_db = [
            # RPG игры
            {
                "id": 1,
                "title": "The Witcher 3: Wild Hunt",
                "platform": ["PC", "игровая консоль"],
                "genre": "Ролевая игра",
                "setting": "Фэнтези",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 2,
                "title": "Cyberpunk 2077",
                "platform": ["PC", "игровая консоль"],
                "genre": "Ролевая игра",
                "setting": "Киберпанк",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "долгая",
                "graphics": "Фотореализм"
            },
            {
                "id": 3,
                "title": "Elden Ring",
                "platform": ["PC", "игровая консоль"],
                "genre": "Ролевая игра",
                "setting": "Фэнтези",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 4,
                "title": "Skyrim",
                "platform": ["PC", "игровая консоль"],
                "genre": "Ролевая игра",
                "setting": "Фэнтези",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 5,
                "title": "Mass Effect: Legendary Edition",
                "platform": ["PC", "игровая консоль"],
                "genre": "Ролевая игра",
                "setting": "Научная фантастика",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 6,
                "title": "Disco Elysium",
                "platform": ["PC", "игровая консоль"],
                "genre": "RPG",
                "setting": "Современный",
                "rating": "M",
                "price": "инди-цена",
                "game_type": ["Одиночная"],
                "duration": "средняя",
                "graphics": "стилизованная графика"
            },

            # Экшен игры
            {
                "id": 7,
                "title": "Counter-Strike 2",
                "platform": ["PC"],
                "genre": "Экшен",
                "setting": "Современный",
                "rating": "M",
                "price": "Бесплатная",
                "game_type": ["Многопользовательская", "Соревновательный"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 8,
                "title": "The Last of Us Part I",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Постапокалипсис",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "средняя",
                "graphics": "Фотореализм"
            },
            {
                "id": 9,
                "title": "Fortnite",
                "platform": ["PC", "игровая консоль", "мобильные устройства"],
                "genre": "Экшен",
                "setting": "Современный",
                "rating": "T",
                "price": "Бесплатная",
                "game_type": ["Многопользовательская", "Соревновательный"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 10,
                "title": "DOOM Eternal",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Научная фантастика",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "средняя",
                "graphics": "Фотореализм"
            },
            {
                "id": 11,
                "title": "Grand Theft Auto V",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Современный",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 12,
                "title": "Red Dead Redemption 2",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Исторический",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },

            # Приключения
            {
                "id": 13,
                "title": "Hollow Knight",
                "platform": ["PC", "игровая консоль"],
                "genre": "Приключения",
                "setting": "Фэнтези",
                "rating": "E10+",
                "price": "инди-цена",
                "game_type": ["Одиночная"],
                "duration": "долгая",
                "graphics": "стилизованная графика"
            },
            {
                "id": 14,
                "title": "The Legend of Zelda: Breath of the Wild",
                "platform": ["игровая консоль"],
                "genre": "Приключения",
                "setting": "Фэнтези",
                "rating": "E10+",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 15,
                "title": "God of War (2018)",
                "platform": ["PC", "игровая консоль"],
                "genre": "Приключения",
                "setting": "Фэнтези",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "долгая",
                "graphics": "Фотореализм"
            },
            {
                "id": 16,
                "title": "Uncharted 4: A Thief's End",
                "platform": ["PC", "игровая консоль"],
                "genre": "Приключения",
                "setting": "Современный",
                "rating": "T",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "средняя",
                "graphics": "Фотореализм"
            },
            {
                "id": 17,
                "title": "Ori and the Will of the Wisps",
                "platform": ["PC", "игровая консоль"],
                "genre": "Приключения",
                "setting": "Фэнтези",
                "rating": "E10+",
                "price": "инди-цена",
                "game_type": ["Одиночная"],
                "duration": "средняя",
                "graphics": "стилизованная графика"
            },

            # Стратегии
            {
                "id": 18,
                "title": "Civilization VI",
                "platform": ["PC", "игровая консоль"],
                "genre": "Стратегии",
                "setting": "Исторический",
                "rating": "E10+",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 19,
                "title": "StarCraft II",
                "platform": ["PC"],
                "genre": "Стратегии",
                "setting": "Научная фантастика",
                "rating": "T",
                "price": "Бесплатная",
                "game_type": ["Одиночная", "Многопользовательская", "Соревновательный"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 20,
                "title": "XCOM 2",
                "platform": ["PC", "игровая консоль"],
                "genre": "Стратегии",
                "setting": "Научная фантастика",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "долгая",
                "graphics": "стилизованная графика"
            },
            {
                "id": 21,
                "title": "Crusader Kings III",
                "platform": ["PC", "игровая консоль"],
                "genre": "Стратегии",
                "setting": "Исторический",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 22,
                "title": "Age of Empires IV",
                "platform": ["PC", "игровая консоль"],
                "genre": "Стратегии",
                "setting": "Исторический",
                "rating": "T",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "долгая",
                "graphics": "стилизованная графика"
            },

            # Симуляторы
            {
                "id": 23,
                "title": "Stardew Valley",
                "platform": ["PC", "игровая консоль", "мобильные устройства"],
                "genre": "Симуляторы",
                "setting": "Современный",
                "rating": "E",
                "price": "инди-цена",
                "game_type": ["Одиночная", "Кооператив"],
                "duration": "океан контента",
                "graphics": "пиксель-арт"
            },
            {
                "id": 24,
                "title": "The Sims 4",
                "platform": ["PC", "игровая консоль"],
                "genre": "Симуляторы",
                "setting": "Современный",
                "rating": "T",
                "price": "Бесплатная",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 25,
                "title": "Microsoft Flight Simulator",
                "platform": ["PC", "игровая консоль"],
                "genre": "Симуляторы",
                "setting": "Современный",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 26,
                "title": "Cities: Skylines",
                "platform": ["PC", "игровая консоль"],
                "genre": "Симуляторы",
                "setting": "Современный",
                "rating": "E",
                "price": "инди-цена",
                "game_type": ["Одиночная"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 27,
                "title": "Farming Simulator 22",
                "platform": ["PC", "игровая консоль"],
                "genre": "Симуляторы",
                "setting": "Современный",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },

            # Гонки
            {
                "id": 28,
                "title": "Forza Horizon 5",
                "platform": ["PC", "игровая консоль"],
                "genre": "Гонки",
                "setting": "Современный",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 29,
                "title": "Gran Turismo 7",
                "platform": ["игровая консоль"],
                "genre": "Гонки",
                "setting": "Современный",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 30,
                "title": "Mario Kart 8 Deluxe",
                "platform": ["игровая консоль"],
                "genre": "Гонки",
                "setting": "Фэнтези",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская", "Кооператив"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 31,
                "title": "F1 2023",
                "platform": ["PC", "игровая консоль"],
                "genre": "Гонки",
                "setting": "Современный",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },

            # Спортивные
            {
                "id": 32,
                "title": "FIFA 23",
                "platform": ["PC", "игровая консоль"],
                "genre": "Спортивные",
                "setting": "Современный",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 33,
                "title": "NBA 2K23",
                "platform": ["PC", "игровая консоль"],
                "genre": "Спортивные",
                "setting": "Современный",
                "rating": "E",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "океан контента",
                "graphics": "Фотореализм"
            },
            {
                "id": 34,
                "title": "Rocket League",
                "platform": ["PC", "игровая консоль"],
                "genre": "Спортивные",
                "setting": "Современный",
                "rating": "E",
                "price": "Бесплатная",
                "game_type": ["Многопользовательская", "Соревновательный"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 35,
                "title": "Tony Hawk's Pro Skater 1+2",
                "platform": ["PC", "игровая консоль"],
                "genre": "Спортивные",
                "setting": "Современный",
                "rating": "T",
                "price": "AAA-цена",
                "game_type": ["Одиночная", "Многопользовательская"],
                "duration": "средняя",
                "graphics": "Фотореализм"
            },

            # Хоррор игры
            {
                "id": 36,
                "title": "Resident Evil 4 Remake",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Хоррор",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "средняя",
                "graphics": "Фотореализм"
            },
            {
                "id": 37,
                "title": "Dead by Daylight",
                "platform": ["PC", "игровая консоль", "мобильные устройства"],
                "genre": "Экшен",
                "setting": "Хоррор",
                "rating": "M",
                "price": "инди-цена",
                "game_type": ["Многопользовательская"],
                "duration": "океан контента",
                "graphics": "стилизованная графика"
            },
            {
                "id": 38,
                "title": "The Evil Within 2",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Хоррор",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "средняя",
                "graphics": "Фотореализм"
            },

            # Стимпанк и другие сеттинги
            {
                "id": 39,
                "title": "Bioshock Infinite",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Стимпанк",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "средняя",
                "graphics": "стилизованная графика"
            },
            {
                "id": 40,
                "title": "Dishonored 2",
                "platform": ["PC", "игровая консоль"],
                "genre": "Экшен",
                "setting": "Стимпанк",
                "rating": "M",
                "price": "AAA-цена",
                "game_type": ["Одиночная"],
                "duration": "средняя",
                "graphics": "стилизованная графика"
            }
        ]

        # Доступные варианты для каждого критерия
        self.criteria_options = {
            'platform': ['PC', 'игровая консоль', 'мобильные устройства'],
            'genre': ['Экшен', 'Приключения', 'Ролевая игра', 'Стратегии', 'Симуляторы', 'Гонки', 'Спортивные'],
            'setting': ['Фэнтези', 'Научная фантастика', 'Киберпанк', 'Стимпанк', 'Постапокалипсис', 'Исторический',
                        'Современный', 'Хоррор'],
            'rating': ['E', 'E10+', 'T', 'M'],
            'price': ['Бесплатная', 'инди-цена', 'AAA-цена'],
            'game_type': ['Одиночная', 'Многопользовательская', 'Кооператив', 'Соревновательный'],
            'duration': ['Короткая', 'средняя', 'долгая', 'океан контента'],
            'graphics': ['Фотореализм', 'стилизованная графика', 'пиксель-арт']
        }

        # Для удобства вывода полных названий
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

    def get_user_preferences(self):
        """Запрос предпочтений у пользователя с вопросами-ассоциациями"""
        print("=== СИСТЕМА ПОДБОРА ВИДЕОИГР ===")
        print("Ответьте на вопросы о ваших предпочтениях (да/нет):\n")

        preferences = {}

        # Платформа (можно выбрать несколько)
        print("На каких устройствах вы играете?")
        for i, platform in enumerate(self.criteria_options['platform'], 1):
            print(f"{i}. {platform}")

        platform_choice = input("\nВведите номера предпочитаемых платформ через запятую (например: 1,2,3): ")
        platform_indices = [int(x.strip()) - 1 for x in platform_choice.split(',') if x.strip().isdigit()]
        preferences['platform'] = [self.criteria_options['platform'][i] for i in platform_indices if
                                   0 <= i < len(self.criteria_options['platform'])]

        # Жанры (вопросы да/нет)
        print("\nКакие типы игр вам нравятся?")
        preferred_genres = []

        genre_associations = {
            'Экшен': "Вам нравятся динамичные игры с экшеном и сражениями?",
            'Приключения': "Вам нравятся исследования и решение загадок?",
            'Ролевая игра': "Вам нравятся прокачка персонажей и развитие сюжета?",
            'Стратегии': "Вам нравятся планирование и тактические решения?",
            'Симуляторы': "Вам нравятся реалистичные симуляции жизни или деятельности?",
            'Гонки': "Вам нравятся скоростные соревнования и автомобили?",
            'Спортивные': "Вам нравятся спортивные соревнования и турниры?"
        }

        for genre, question in genre_associations.items():
            response = input(f"{question} ").lower().strip()
            if response in ['да', 'д', 'yes', 'y', 'yes']:
                preferred_genres.append(genre)

        if preferred_genres:
            preferences['genre'] = preferred_genres

        # Сеттинги через ассоциации
        print("\nКакие миры и атмосферы вам интересны?")
        preferred_settings = []

        setting_associations = {
            'Фэнтези': "Вам нравятся рыцари, магия и древние замки?",
            'Научная фантастика': "Вам нравятся космос, технологии и будущее?",
            'Киберпанк': "Вам нравятся неоновые города, кибернетика и высокие технологии?",
            'Стимпанк': "Вам нравятся паровые машины, шестерёнки и викторианская эпоха?",
            'Постапокалипсис': "Вам нравятся выживание в разрушенном мире?",
            'Исторический': "Вам нравятся древние цивилизации и исторические события?",
            'Современный': "Вам нравятся современные города и реалистичные истории?",
            'Хоррор': "Вам нравятся ужасы и пугающая атмосфера?"
        }

        for setting, question in setting_associations.items():
            response = input(f"{question} ").lower().strip()
            if response in ['да', 'д', 'yes', 'y', 'yes']:
                preferred_settings.append(setting)

        if preferred_settings:
            preferences['setting'] = preferred_settings

        # Возрастной рейтинг
        print("\nДля какой возрастной категории ищем игры?")
        for i, rating in enumerate(self.criteria_options['rating'], 1):
            print(f"{i}. {self.rating_names[rating]}")

        rating_choice = input("Выберите номер рейтинга: ")
        if rating_choice.isdigit() and 1 <= int(rating_choice) <= len(self.criteria_options['rating']):
            preferences['rating'] = self.criteria_options['rating'][int(rating_choice) - 1]

        # Цена
        print("\nКакой бюджет вас интересует?")
        for i, price in enumerate(self.criteria_options['price'], 1):
            print(f"{i}. {self.price_names[price]}")

        price_choice = input("Выберите номер ценовой категории: ")
        if price_choice.isdigit() and 1 <= int(price_choice) <= len(self.criteria_options['price']):
            preferences['price'] = self.criteria_options['price'][int(price_choice) - 1]

        # Тип игры
        print("\nКак вы любите играть?")
        preferred_game_types = []

        type_associations = {
            'Одиночная': "Вам нравятся игры, где можно играть в одиночку?",
            'Многопользовательская': "Вам нравятся игры с другими игроками онлайн?",
            'Кооператив': "Вам нравятся игры, где можно играть с друзьями вместе?",
            'Соревновательный': "Вам нравятся соревнования против других игроков?"
        }

        for game_type, question in type_associations.items():
            response = input(f"{question} ").lower().strip()
            if response in ['да', 'д', 'yes', 'y', 'yes']:
                preferred_game_types.append(game_type)

        if preferred_game_types:
            preferences['game_type'] = preferred_game_types

        # Продолжительность
        print("\nКакую продолжительность игры предпочитаете?")
        for i, duration in enumerate(self.criteria_options['duration'], 1):
            print(f"{i}. {self.duration_names[duration]}")

        duration_choice = input("Выберите номер продолжительности: ")
        if duration_choice.isdigit() and 1 <= int(duration_choice) <= len(self.criteria_options['duration']):
            preferences['duration'] = self.criteria_options['duration'][int(duration_choice) - 1]

        # Графика
        print("\nКакой визуальный стиль вам нравится?")
        preferred_graphics = []

        graphics_associations = {
            'Фотореализм': "Вам нравится реалистичная графика, как в кино?",
            'стилизованная графика': "Вам нравится художественный стиль и уникальный визуал?",
            'пиксель-арт': "Вам нравится ретро-стиль и пиксельная графика?"
        }

        for graphics, question in graphics_associations.items():
            response = input(f"{question} ").lower().strip()
            if response in ['да', 'д', 'yes', 'y', 'yes']:
                preferred_graphics.append(graphics)

        if preferred_graphics:
            preferences['graphics'] = preferred_graphics

        return preferences

    # ... (остальные методы find_matching_games, display_results, run остаются без изменений)
    def find_matching_games(self, preferences):
        """Поиск игр с системой баллов - более гибкий подход"""
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

    def display_results(self, results, preferences):
        """Отображение результатов с балльной системой"""
        print("\n" + "=" * 60)
        print("РЕЗУЛЬТАТЫ ПОДБОРА (отсортированы по релевантности)")
        print("=" * 60)

        if not results:
            print("К сожалению, не найдено идеально подходящих игр.")
            print("Попробуйте ослабить некоторые критерии поиска.")
            return

        print(f"Найдено подходящих игр: {len(results)}\n")

        for i, result in enumerate(results[:10], 1):  # Показываем топ-10
            game = result['game']
            print(f"{i}. {game['title']} [Совпадение: {result['score']} баллов]")
            print(f"   Платформы: {', '.join(game['platform'])}")
            print(f"   Жанр: {game['genre']} | Сеттинг: {game['setting']}")
            print(f"   Цена: {game['price']} | Тип: {', '.join(game['game_type'])}")

            # Показываем причины рекомендации
            if 'reasons' in result:
                print("   Почему рекомендована:")
                for reason in result['reasons'][:3]:  # Первые 3 причины
                    print(f"     {reason}")

            print()

    def run(self):
        """Запуск системы рекомендаций"""
        try:
            preferences = self.get_user_preferences()
            matching_games = self.find_matching_games(preferences)
            self.display_results(matching_games, preferences)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            input("\nНажмите Enter для выхода...")


# Запуск программы
if __name__ == "__main__":
    system = GameRecommendationSystem()
    system.run()
