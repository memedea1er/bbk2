import time

class Item:
    def __init__(self, id, weight, price):
        self.id = id
        self.weight = weight
        self.price = price
        self.ratio = price / weight if weight > 0 else 0

    def __repr__(self):
        return f"Item(id={self.id}, weight={self.weight}, price={self.price})"


class BranchAndBoundMethod:
    MAX_WEIGHT = 15  # W - максимальная вместимость рюкзака
    MAX_AMOUNT = 7  # M - количество предметов

    def __init__(self):
        self.items = []
        self.best_value = 0
        self.best_taken = []
        self.current_taken = []
        self.node_count = 0
        self.init_items()

    def init_items(self):
        """Инициализация предметов"""
        self.items = [
            Item(1, 2, 10),
            Item(2, 3, 5),
            Item(3, 5, 15),
            Item(4, 7, 7),
            Item(5, 1, 6),
            Item(6, 4, 18),
            Item(7, 1, 3)
        ]

    def calculate_upper_bound(self, level, current_weight):
        """
        Вычисление верхней границы (ограничение сверху) для узла
        Использует жадный алгоритм для оценки максимально возможной стоимости
        """
        remaining = self.MAX_WEIGHT - current_weight
        bound = 0.0

        for i in range(level, len(self.items)):
            item = self.items[i]
            if remaining >= item.weight:
                remaining -= item.weight
                bound += item.price
            else:
                bound += item.ratio * remaining
                break

        return bound

    def branch_and_bounds(self, level, weight, price):
        """
        Рекурсивный метод ветвей и границ
        level: текущий уровень (индекс предмета)
        weight: текущий вес в рюкзаке
        price: текущая стоимость в рюкзаке
        """
        self.node_count += 1

        # Проверка: превышен ли максимальный вес
        if weight > self.MAX_WEIGHT:
            return

        # Вычисление верхней границы и отсечение неперспективных ветвей
        upper_bound = price + self.calculate_upper_bound(level, weight)
        if upper_bound <= self.best_value:
            return

        # Базовый случай: достигнут конец списка предметов
        if level == len(self.items):
            if price > self.best_value:
                self.best_value = price
                self.best_taken = self.current_taken.copy()
            return

        # Ветвь 1: берем текущий предмет
        self.current_taken[level] = True
        self.branch_and_bounds(
            level + 1,
            weight + self.items[level].weight,
            price + self.items[level].price
        )

        # Ветвь 2: не берем текущий предмет
        self.current_taken[level] = False
        self.branch_and_bounds(level + 1, weight, price)

    def solve(self):
        """Основной метод решения задачи"""
        # Сохраняем оригинальный порядок предметов
        original_items = self.items.copy()

        # Сортируем предметы по убыванию соотношения цена/вес
        # Это улучшает отсечение неперспективных ветвей
        self.items.sort(key=lambda x: x.ratio, reverse=True)

        # Инициализация массивов выбранных предметов
        self.best_taken = [False] * self.MAX_AMOUNT
        self.current_taken = [False] * self.MAX_AMOUNT

        # Запуск алгоритма
        start_time = time.perf_counter()
        self.branch_and_bounds(0, 0, 0)
        end_time = time.perf_counter()
        total_time = (end_time - start_time) * 1000  # в миллисекундах

        # Восстановление оригинального порядка
        final_selection = self.get_default_ordering(self.best_taken)

        # Вывод результатов
        total_weight = 0
        total_value = 0
        selected_items = []

        print("Оптимальный набор предметов: ", end="")
        for i in range(self.MAX_AMOUNT):
            if final_selection[i]:
                selected_items.append(i + 1)
                total_weight += original_items[i].weight
                total_value += original_items[i].price

        print(*selected_items)
        print(f"Оптимальная суммарная стоимость P* = {total_value}")
        print(f"Оптимальный суммарный вес W* = {total_weight}")
        print(f"Количество рассчитанных вариантов (узлов): {self.node_count}")
        print(f"Время поиска решения: {total_time:.3f} мс")

        return {
            'value': total_value,
            'weight': total_weight,
            'selected': selected_items,
            'nodes': self.node_count,
            'time': total_time
        }

    def get_default_ordering(self, target_array):
        """
        Восстановление выбора предметов в оригинальном порядке
        после сортировки по соотношению цена/вес
        """
        final_array = [False] * self.MAX_AMOUNT
        for i in range(len(target_array)):
            if target_array[i]:
                # items[i] сейчас отсортированы, нужно найти оригинальный индекс
                item_id = self.items[i].id
                final_array[item_id - 1] = True
        return final_array


# Запуск решения
if __name__ == "__main__":
    solver = BranchAndBoundMethod()
    result = solver.solve()