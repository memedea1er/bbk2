# -*- coding: utf-8 -*-
class GameRecommendationSystem:
    def __init__(self):
        # Расширенная база данных видеоигр
        self.games_db = [
            # RPG игры
            {
                "id": 1,
                "title": "The Witcher 3: Wild Hunt",
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S", "Nintendo Switch"],
                "genre": "RPG",
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
                "platform": ["PC", "PlayStation 5", "PlayStation 4", "Xbox Series X/S", "Xbox One"],
                "genre": "RPG",
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
                "platform": ["PC", "PlayStation 5", "PlayStation 4", "Xbox Series X/S", "Xbox One"],
                "genre": "RPG",
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S", "Nintendo Switch"],
                "genre": "RPG",
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
                "platform": ["PC", "PlayStation 4", "Xbox One"],
                "genre": "RPG",
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 5"],
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
                "platform": ["PC", "PlayStation 5", "PlayStation 4", "Xbox Series X/S", "Xbox One", "Nintendo Switch",
                             "мобильные устройства"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One", "Nintendo Switch"],
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
                "platform": ["Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5"],
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
                "platform": ["PC", "Xbox One", "Xbox Series X/S", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 5", "Xbox Series X/S"],
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
                "platform": ["PC", "Xbox Series X/S"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One", "Nintendo Switch", "мобильные устройства"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One"],
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
                "platform": ["PC", "Xbox Series X/S"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S"],
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
                "platform": ["PC", "Xbox Series X/S", "Xbox One"],
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
                "platform": ["PlayStation 4", "PlayStation 5"],
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
                "platform": ["Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S"],
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
                "platform": ["PC", "PlayStation 5", "PlayStation 4", "Xbox Series X/S"],
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
                "platform": ["PC", "PlayStation 4", "PlayStation 5", "Xbox One", "Xbox Series X/S", "Nintendo Switch",
                             "мобильные устройства"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One", "Nintendo Switch"],
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
                "platform": ["PC", "PlayStation 4", "Xbox One"],
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
            'platform': ['PC', 'PlayStation 5', 'PlayStation 4', 'Xbox Series X/S', 'Xbox One', 'Nintendo Switch',
                         'мобильные устройства'],
            'genre': ['Экшен', 'Приключения', 'RPG', 'Стратегии', 'Симуляторы', 'Гонки', 'Спортивные'],
            'setting': ['Фэнтези', 'Научная фантастика', 'Киберпанк', 'Стимпанк', 'Постапокалипсис', 'Исторический',
                        'Современный', 'Хоррор'],
            'rating': ['E', 'E10+', 'T', 'M'],
            'price': ['Бесплатная', 'инди-цена', 'AAA-цена'],
            'game_type': ['Одиночная', 'Многопользовательская', 'Кооператив', 'Соревновательный'],
            'duration': ['Короткая', 'средняя', 'долгая', 'океан контента'],
            'graphics': ['Фотореализм', 'стилизованная графика', 'пиксель-арт', 'низкополигональная', 'cel-shading']
        }

        # Для удобства вывода полных названий
        self.rating_names = {
            'E': 'Для всех (E)',
            'E10+': 'Для всех от 10+ (E10+)',
            'T': 'Для подростков (T)',
            'M': 'Для взрослых (M/A)'
        }

        self.duration_names = {
            'Короткая': 'Короткая (менее 10 часов)',
            'средняя': 'Средняя (10-30 часов)',
            'долгая': 'Долгая (30-60 часов)',
            'океан контента': 'Океан контента (60+ часов)'
        }

    def get_user_preferences(self):
        """Запрос предпочтений у пользователя"""
        print("=== СИСТЕМА ПОДБОРА ВИДЕОИГР ===")
        print("Ответьте на вопросы о ваших предпочтениях:\n")

        preferences = {}

        # Платформа (можно выбрать несколько)
        print("Доступные платформы:")
        for i, platform in enumerate(self.criteria_options['platform'], 1):
            print(f"{i}. {platform}")

        platform_choice = input("\nВведите номера предпочитаемых платформ через запятую (например: 1,3,5): ")
        platform_indices = [int(x.strip()) - 1 for x in platform_choice.split(',') if x.strip().isdigit()]
        preferences['platform'] = [self.criteria_options['platform'][i] for i in platform_indices if
                                   0 <= i < len(self.criteria_options['platform'])]

        # Жанр
        print("\nДоступные жанры:")
        for i, genre in enumerate(self.criteria_options['genre'], 1):
            print(f"{i}. {genre}")

        genre_choice = input("Выберите номер жанра: ")
        if genre_choice.isdigit() and 1 <= int(genre_choice) <= len(self.criteria_options['genre']):
            preferences['genre'] = self.criteria_options['genre'][int(genre_choice) - 1]

        # Сеттинг
        print("\nДоступные сеттинги:")
        for i, setting in enumerate(self.criteria_options['setting'], 1):
            print(f"{i}. {setting}")

        setting_choice = input("Выберите номер сеттинга: ")
        if setting_choice.isdigit() and 1 <= int(setting_choice) <= len(self.criteria_options['setting']):
            preferences['setting'] = self.criteria_options['setting'][int(setting_choice) - 1]

        # Возрастной рейтинг
        print("\nДоступные возрастные рейтинги:")
        for i, rating in enumerate(self.criteria_options['rating'], 1):
            print(f"{i}. {self.rating_names[rating]}")

        rating_choice = input("Выберите номер рейтинга: ")
        if rating_choice.isdigit() and 1 <= int(rating_choice) <= len(self.criteria_options['rating']):
            preferences['rating'] = self.criteria_options['rating'][int(rating_choice) - 1]

        # Цена
        print("\nДоступные ценовые категории:")
        for i, price in enumerate(self.criteria_options['price'], 1):
            print(f"{i}. {price}")

        price_choice = input("Выберите номер ценовой категории: ")
        if price_choice.isdigit() and 1 <= int(price_choice) <= len(self.criteria_options['price']):
            preferences['price'] = self.criteria_options['price'][int(price_choice) - 1]

        # Тип игры (можно выбрать несколько)
        print("\nДоступные типы игры:")
        for i, game_type in enumerate(self.criteria_options['game_type'], 1):
            print(f"{i}. {game_type}")

        type_choice = input("Введите номера предпочитаемых типов через запятую: ")
        type_indices = [int(x.strip()) - 1 for x in type_choice.split(',') if x.strip().isdigit()]
        preferences['game_type'] = [self.criteria_options['game_type'][i] for i in type_indices if
                                    0 <= i < len(self.criteria_options['game_type'])]

        # Продолжительность
        print("\nДоступная продолжительность:")
        for i, duration in enumerate(self.criteria_options['duration'], 1):
            print(f"{i}. {self.duration_names[duration]}")

        duration_choice = input("Выберите номер продолжительности: ")
        if duration_choice.isdigit() and 1 <= int(duration_choice) <= len(self.criteria_options['duration']):
            preferences['duration'] = self.criteria_options['duration'][int(duration_choice) - 1]

        # Графика
        print("\nДоступные стили графики:")
        for i, graphics in enumerate(self.criteria_options['graphics'], 1):
            print(f"{i}. {graphics}")

        graphics_choice = input("Выберите номер стиля графики: ")
        if graphics_choice.isdigit() and 1 <= int(graphics_choice) <= len(self.criteria_options['graphics']):
            preferences['graphics'] = self.criteria_options['graphics'][int(graphics_choice) - 1]

        return preferences

    def find_matching_games(self, preferences):
        """Поиск игр, соответствующих предпочтениям пользователя"""
        matching_games = []

        for game in self.games_db:
            # Проверка платформы (хотя бы одна должна совпадать)
            if preferences.get('platform'):
                platform_match = any(platform in game['platform'] for platform in preferences['platform'])
                if not platform_match:
                    continue

            # Проверка жанра
            if preferences.get('genre') and game['genre'] != preferences['genre']:
                continue

            # Проверка сеттинга
            if preferences.get('setting') and game['setting'] != preferences['setting']:
                continue

            # Проверка возрастного рейтинга
            if preferences.get('rating') and game['rating'] != preferences['rating']:
                continue

            # Проверка цены
            if preferences.get('price') and game['price'] != preferences['price']:
                continue

            # Проверка типа игры (хотя бы один должен совпадать)
            if preferences.get('game_type'):
                type_match = any(game_type in game['game_type'] for game_type in preferences['game_type'])
                if not type_match:
                    continue

            # Проверка продолжительности
            if preferences.get('duration') and game['duration'] != preferences['duration']:
                continue

            # Проверка графики
            if preferences.get('graphics') and game['graphics'] != preferences['graphics']:
                continue

            # Если все критерии совпали, добавляем игру в результат
            matching_games.append(game)

        return matching_games

    def display_results(self, games, preferences):
        """Отображение результатов подбора"""
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТЫ ПОДБОРА")
        print("=" * 50)

        if not games:
            print("К сожалению, по вашим критериям не найдено подходящих игр.")
            print("Попробуйте изменить некоторые параметры поиска.")
            return

        print(f"Найдено игр: {len(games)}\n")

        for i, game in enumerate(games, 1):
            print(f"{i}. {game['title']}")
            print(f"   Платформы: {', '.join(game['platform'])}")
            print(f"   Жанр: {game['genre']}")
            print(f"   Сеттинг: {game['setting']}")
            print(f"   Рейтинг: {self.rating_names[game['rating']]}")
            print(f"   Цена: {game['price']}")
            print(f"   Тип игры: {', '.join(game['game_type'])}")
            print(f"   Продолжительность: {self.duration_names[game['duration']]}")
            print(f"   Графика: {game['graphics']}")
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