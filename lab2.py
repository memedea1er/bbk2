def print_matrix(matrix, rows, cols, row_labels, col_labels, title):
    """Вывод матрицы в читаемом формате"""
    print(f"\n{title}")
    print(" " * 8, end="")
    for label in col_labels:
        print(f"{label:>8}", end="")
    print()

    for i in range(rows):
        print(f"{row_labels[i]:>8}", end="")
        for j in range(cols):
            print(f"{matrix[i][j]:>8}", end="")
        print()


def savage_criterion(loss_matrix, n_strategies, n_states):
    """Критерий Сэвиджа (минимаксных сожалений)"""
    # Находим минимальные потери по каждому столбцу
    min_losses = []
    for j in range(n_states):
        col_min = loss_matrix[0][j]
        for i in range(1, n_strategies):
            if loss_matrix[i][j] < col_min:
                col_min = loss_matrix[i][j]
        min_losses.append(col_min)

    # Строим матрицу сожалений
    regret_matrix = []
    for i in range(n_strategies):
        row = []
        for j in range(n_states):
            row.append(loss_matrix[i][j] - min_losses[j])
        regret_matrix.append(row)

    # Находим максимальные сожаления для каждой стратегии
    max_regrets = []
    for i in range(n_strategies):
        max_regret = regret_matrix[i][0]
        for j in range(1, n_states):
            if regret_matrix[i][j] > max_regret:
                max_regret = regret_matrix[i][j]
        max_regrets.append(max_regret)

    # Находим оптимальную стратегию
    min_max_regret = max_regrets[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if max_regrets[i] < min_max_regret:
            min_max_regret = max_regrets[i]
            optimal_strategy = i

    return regret_matrix, max_regrets, optimal_strategy


def maximin_criterion(loss_matrix, n_strategies, n_states):
    """Максиминный критерий (для матрицы потерь)"""
    # Находим максимальные потери для каждой стратегии
    max_losses = []
    for i in range(n_strategies):
        max_loss = loss_matrix[i][0]
        for j in range(1, n_states):
            if loss_matrix[i][j] > max_loss:
                max_loss = loss_matrix[i][j]
        max_losses.append(max_loss)

    # Находим оптимальную стратегию (минимальный максимальный проигрыш)
    min_max_loss = max_losses[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if max_losses[i] < min_max_loss:
            min_max_loss = max_losses[i]
            optimal_strategy = i

    return max_losses, optimal_strategy


def hurwitz_criterion(loss_matrix, n_strategies, n_states, alpha=0.5):
    """Критерий Гурвица для матрицы потерь"""
    hurwitz_values = []

    for i in range(n_strategies):
        # Находим минимальные и максимальные потери для стратегии
        min_loss = loss_matrix[i][0]
        max_loss = loss_matrix[i][0]

        for j in range(1, n_states):
            if loss_matrix[i][j] < min_loss:
                min_loss = loss_matrix[i][j]
            if loss_matrix[i][j] > max_loss:
                max_loss = loss_matrix[i][j]

        # Для матрицы потерь: alpha * min + (1-alpha) * max
        hurwitz_value = alpha * min_loss + (1 - alpha) * max_loss
        hurwitz_values.append(hurwitz_value)

    # Находим оптимальную стратегию
    min_hurwitz = hurwitz_values[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if hurwitz_values[i] < min_hurwitz:
            min_hurwitz = hurwitz_values[i]
            optimal_strategy = i

    return hurwitz_values, optimal_strategy


def bayes_laplace_criterion(loss_matrix, n_strategies, n_states):
    """Критерий Байеса-Лапласа для матрицы потерь"""
    # Равномерное распределение вероятностей
    probability = 1.0 / n_states

    expected_losses = []

    for i in range(n_strategies):
        expected_loss = 0.0
        for j in range(n_states):
            expected_loss += loss_matrix[i][j] * probability
        expected_losses.append(expected_loss)

    # Находим оптимальную стратегию
    min_expected_loss = expected_losses[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if expected_losses[i] < min_expected_loss:
            min_expected_loss = expected_losses[i]
            optimal_strategy = i

    return expected_losses, optimal_strategy


def dict_to_string(dictionary, keys):
    """Преобразование словаря в строку"""
    result = "{"
    for i, key in enumerate(keys):
        if i > 0:
            result += ", "
        result += f"'{key}': {dictionary[key]}"
    result += "}"
    return result


def main():
    # Исходные данные
    loss_matrix = [
        [5, 10, 18, 25],  # A1
        [8, 7, 8, 23],  # A2
        [21, 18, 12, 21],  # A3
        [30, 22, 19, 15]  # A4
    ]

    strategies = ['A1', 'A2', 'A3', 'A4']
    states = ['200', '250', '300', '350']

    n_strategies = len(strategies)
    n_states = len(states)

    print("=" * 70)
    print("АНАЛИЗ ОПТИМАЛЬНОГО УРОВНЯ ПРЕДЛОЖЕНИЯ УСЛУГ")
    print("=" * 70)

    # Вывод исходной матрицы
    print_matrix(loss_matrix, n_strategies, n_states, strategies, states,
                 "ИСХОДНАЯ МАТРИЦА ПОТЕРЬ (в тыс. руб.):")

    print("\n" + "=" * 70)

    # 1. Критерий Сэвиджа
    print("\n1. КРИТЕРИЙ СЭВИДЖА (минимаксных сожалений):")
    regret_matrix, max_regrets, savage_opt = savage_criterion(loss_matrix, n_strategies, n_states)

    print_matrix(regret_matrix, n_strategies, n_states, strategies, states,
                 "Матрица сожалений:")

    print(f"\nМаксимальные сожаления:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {max_regrets[i]}")

    print(f"\nОптимальная стратегия: {strategies[savage_opt]} " +
          f"(максимальное сожаление = {max_regrets[savage_opt]})")

    # 2. Максиминный критерий
    print("\n" + "-" * 50)
    print("\n2. МАКСИМИННЫЙ КРИТЕРИЙ:")
    max_losses, maximin_opt = maximin_criterion(loss_matrix, n_strategies, n_states)

    print(f"Максимальные потери:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {max_losses[i]}")

    print(f"\nОптимальная стратегия: {strategies[maximin_opt]} " +
          f"(максимальный проигрыш = {max_losses[maximin_opt]})")

    # 3. Критерий Гурвица
    print("\n" + "-" * 50)
    print("\n3. КРИТЕРИЙ ГУРВИЦА (α=0.5):")
    hurwitz_values, hurwitz_opt = hurwitz_criterion(loss_matrix, n_strategies, n_states, 0.5)

    print(f"Значения критерия:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {hurwitz_values[i]:.2f}")

    print(f"\nОптимальная стратегия: {strategies[hurwitz_opt]} " +
          f"(значение = {hurwitz_values[hurwitz_opt]:.2f})")

    # 4. Критерий Байеса-Лапласа
    print("\n" + "-" * 50)
    print("\n4. КРИТЕРИЙ БАЙЕСА-ЛАПЛАСА (равные вероятности):")
    expected_losses, bayes_opt = bayes_laplace_criterion(loss_matrix, n_strategies, n_states)

    print(f"Ожидаемые потери:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {expected_losses[i]:.2f}")

    print(f"\nОптимальная стратегия: {strategies[bayes_opt]} " +
          f"(ожидаемые потери = {expected_losses[bayes_opt]:.2f})")

    # Сводная таблица результатов
    print("\n" + "=" * 70)
    print("СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ:")
    print("=" * 70)
    print(f"{'Критерий':<25} {'Оптимальная стратегия':<20}")
    print("-" * 50)
    print(f"{'Сэвиджа':<25} {strategies[savage_opt]:<20}")
    print(f"{'Максиминный':<25} {strategies[maximin_opt]:<20}")
    print(f"{'Гурвица (α=0.5)':<25} {strategies[hurwitz_opt]:<20}")
    print(f"{'Байеса-Лапласа':<25} {strategies[bayes_opt]:<20}")

    # Подсчет частоты выбора каждой стратегии
    frequency = {strategy: 0 for strategy in strategies}
    frequency[strategies[savage_opt]] += 1
    frequency[strategies[maximin_opt]] += 1
    frequency[strategies[hurwitz_opt]] += 1
    frequency[strategies[bayes_opt]] += 1

    print("\n" + "=" * 70)
    print("РЕКОМЕНДАЦИЯ:")
    print("=" * 70)
    print("На основе проведенного анализа:")
    print(f"- По критерию Сэвиджа: {strategies[savage_opt]}")
    print(f"- По максиминному критерию: {strategies[maximin_opt]}")
    print(f"- По критерию Гурвица: {strategies[hurwitz_opt]}")
    print(f"- По критерию Байеса-Лапласа: {strategies[bayes_opt]}")

    print(f"\nЧастота выбора стратегий:")
    for strategy in strategies:
        print(f"  {strategy}: {frequency[strategy]}/4")

    # Определение наиболее часто рекомендуемой стратегии
    max_freq = max(frequency.values())
    best_strategies = [s for s, freq in frequency.items() if freq == max_freq]

    print(f"\nОБЩАЯ РЕКОМЕНДАЦИЯ:")
    if len(best_strategies) == 1:
        print(f"Стратегия {best_strategies[0]} является оптимальной " +
              f"по {max_freq} из 4 критериев.")
    else:
        print(f"Стратегии {', '.join(best_strategies)} являются оптимальными " +
              f"по {max_freq} критериям каждая.")

    print(f"\nДля консервативного подхода к минимизации рисков " +
          f"рекомендуется стратегия {strategies[savage_opt]}.")


if __name__ == "__main__":
    main()