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


def maximin_criterion(loss_matrix, n_strategies, n_states):
    """Критерий максимина (для матрицы потерь)"""
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


def gambler_criterion(loss_matrix, n_strategies, n_states):
    """Критерий азартного игрока (для матрицы потерь)"""
    min_losses = []
    for i in range(n_strategies):
        min_loss = loss_matrix[i][0]
        for j in range(1, n_states):
            if loss_matrix[i][j] < min_loss:
                min_loss = loss_matrix[i][j]
        min_losses.append(min_loss)

    # Находим оптимальную стратегию (минимальный минимальный проигрыш)
    min_min_loss = min_losses[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if min_losses[i] < min_min_loss:
            min_min_loss = min_losses[i]
            optimal_strategy = i

    return min_losses, optimal_strategy


def neutral_criterion(loss_matrix, n_strategies, n_states):
    """Нейтральный критерий (равные вероятности) для потерь"""
    averages = []
    for i in range(n_strategies):
        total = 0
        for j in range(n_states):
            total += loss_matrix[i][j]
        averages.append(total / n_states)

    # Находим оптимальную стратегию (минимальное среднее)
    min_avg = averages[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if averages[i] < min_avg:
            min_avg = averages[i]
            optimal_strategy = i

    return averages, optimal_strategy


def hurwitz_criterion(loss_matrix, n_strategies, n_states, alpha=0.7):
    """Критерий Гурвица для матрицы потерь"""
    hurwitz_values = []

    for i in range(n_strategies):
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

    # Находим оптимальную стратегию (минимальное значение)
    min_hurwitz = hurwitz_values[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if hurwitz_values[i] < min_hurwitz:
            min_hurwitz = hurwitz_values[i]
            optimal_strategy = i

    return hurwitz_values, optimal_strategy


def bayes_laplace_criterion(loss_matrix, n_strategies, n_states, probabilities=None):
    """Критерий Байеса-Лапласа для матрицы потерь"""
    if probabilities is None:
        # Равномерное распределение
        probability = 1.0 / n_states
        probabilities = [probability] * n_states

    expected_losses = []

    for i in range(n_strategies):
        expected_loss = 0.0
        for j in range(n_states):
            expected_loss += loss_matrix[i][j] * probabilities[j]
        expected_losses.append(expected_loss)

    # Находим оптимальную стратегию (минимальные ожидаемые потери)
    min_expected_loss = expected_losses[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if expected_losses[i] < min_expected_loss:
            min_expected_loss = expected_losses[i]
            optimal_strategy = i

    return expected_losses, optimal_strategy


def hodge_lehman_criterion(loss_matrix, n_strategies, n_states, confidence=0.5, probabilities=None):
    """Критерий Ходжа-Лемана для матрицы потерь"""
    if probabilities is None:
        probability = 1.0 / n_states
        probabilities = [probability] * n_states

    hl_values = []

    for i in range(n_strategies):
        # Байесовская часть
        bayes_part = 0.0
        for j in range(n_states):
            bayes_part += loss_matrix[i][j] * probabilities[j]

        # Максиминная часть
        max_loss = loss_matrix[i][0]
        for j in range(1, n_states):
            if loss_matrix[i][j] > max_loss:
                max_loss = loss_matrix[i][j]

        # Комбинация для потерь
        hl_value = confidence * bayes_part + (1 - confidence) * max_loss
        hl_values.append(hl_value)

    # Находим оптимальную стратегию (минимальное значение)
    min_hl = hl_values[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if hl_values[i] < min_hl:
            min_hl = hl_values[i]
            optimal_strategy = i

    return hl_values, optimal_strategy


def minimum_variance_criterion(loss_matrix, n_strategies, n_states, probabilities=None):
    """Критерий минимальной дисперсии для потерь"""
    if probabilities is None:
        probability = 1.0 / n_states
        probabilities = [probability] * n_states

    variances = []

    for i in range(n_strategies):
        # Сначала находим математическое ожидание
        expected = 0.0
        for j in range(n_states):
            expected += loss_matrix[i][j] * probabilities[j]

        # Затем дисперсию
        variance = 0.0
        for j in range(n_states):
            deviation = loss_matrix[i][j] - expected
            variance += probabilities[j] * deviation * deviation

        variances.append(variance)

    # Находим оптимальную стратегию (минимальная дисперсия)
    min_variance = variances[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if variances[i] < min_variance:
            min_variance = variances[i]
            optimal_strategy = i

    return variances, optimal_strategy


def germeier_criterion(loss_matrix, n_strategies, n_states, probabilities=None):
    """Критерий Гермейера для матрицы потерь"""
    if probabilities is None:
        probability = 1.0 / n_states
        probabilities = [probability] * n_states

    germeier_values = []

    for i in range(n_strategies):
        max_weighted_loss = loss_matrix[i][0] * probabilities[0]
        for j in range(1, n_states):
            weighted_loss = loss_matrix[i][j] * probabilities[j]
            if weighted_loss > max_weighted_loss:
                max_weighted_loss = weighted_loss
        germeier_values.append(max_weighted_loss)

    # Находим оптимальную стратегию (минимальное значение)
    min_germeier = germeier_values[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if germeier_values[i] < min_germeier:
            min_germeier = germeier_values[i]
            optimal_strategy = i

    return germeier_values, optimal_strategy


def savage_criterion(loss_matrix, n_strategies, n_states):
    """Критерий Сэвиджа (минимаксных сожалений) для потерь"""
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
    min_regrets = []
    for i in range(n_strategies):
        min_regret = regret_matrix[i][0]
        for j in range(1, n_states):
            if regret_matrix[i][j] < min_regret:
                min_regret = regret_matrix[i][j]
        min_regrets.append(min_regret)

    # Находим оптимальную стратегию (минимальное максимальное сожаление)
    max_min_regret = min_regrets[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if min_regrets[i] > max_min_regret:
            max_min_regret = min_regrets[i]
            optimal_strategy = i

    return regret_matrix, min_regrets, optimal_strategy


def main():
    # Исходные данные (матрица потерь)
    loss_matrix = [
        [5, 10, 18, 25],  # Q1
        [8, 7, 8, 23],  # Q2
        [21, 18, 12, 21],  # Q3
        [30, 22, 19, 15]  # Q4
    ]

    strategies = ['A1', 'A2', 'A3', 'A4']
    states = ['200', '250', '300', '350']

    n_strategies = len(strategies)
    n_states = len(states)

    print("=" * 80)
    print("ПОЛНЫЙ АНАЛИЗ ОПТИМАЛЬНОГО УРОВНЯ ПРЕДЛОЖЕНИЯ УСЛУГ")
    print("(работа непосредственно с матрицей потерь)")
    print("=" * 80)

    # Вывод исходной матрицы
    print_matrix(loss_matrix, n_strategies, n_states, strategies, states,
                 "МАТРИЦА ПОТЕРЬ (в тыс. руб.):")

    # Вероятности для критериев (предположим равные)
    probabilities = [0.2, 0.3, 0.35, 0.15]

    results = {}

    # 1. Критерий максимина
    print("\n" + "=" * 80)
    print("1. КРИТЕРИЙ МАКСИМИНА (Вальда):")
    max_losses, maximin_opt = maximin_criterion(loss_matrix, n_strategies, n_states)
    print("Максимальные потери по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {max_losses[i]}")
    print(f"Оптимальная стратегия: {strategies[maximin_opt]} (минимальные максимальные потери)")
    results['Максимин'] = strategies[maximin_opt]

    # 2. Критерий азартного игрока
    print("\n" + "-" * 50)
    print("2. КРИТЕРИЙ АЗАРТНОГО ИГРОКА:")
    min_losses, gambler_opt = gambler_criterion(loss_matrix, n_strategies, n_states)
    print("Минимальные потери по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {min_losses[i]}")
    print(f"Оптимальная стратегия: {strategies[gambler_opt]} (минимальные минимальные потери)")
    results['Азартный игрок'] = strategies[gambler_opt]

    # 3. Нейтральный критерий
    print("\n" + "-" * 50)
    print("3. НЕЙТРАЛЬНЫЙ КРИТЕРИЙ:")
    averages, neutral_opt = neutral_criterion(loss_matrix, n_strategies, n_states)
    print("Средние потери по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {averages[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[neutral_opt]} (минимальные средние потери)")
    results['Нейтральный'] = strategies[neutral_opt]

    # 4. Критерий Гурвица
    print("\n" + "-" * 50)
    print("4. КРИТЕРИЙ ГУРВИЦА (α=0.7):")
    hurwitz_values, hurwitz_opt = hurwitz_criterion(loss_matrix, n_strategies, n_states, 0.7)
    print("Значения критерия Гурвица:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {hurwitz_values[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[hurwitz_opt]} (компромисс между оптимизмом и пессимизмом)")
    results['Гурвица'] = strategies[hurwitz_opt]

    # 5. Критерий Байеса-Лапласа
    print("\n" + "-" * 50)
    print("5. КРИТЕРИЙ БАЙЕСА-ЛАПЛАСА:")
    expected_losses, bayes_opt = bayes_laplace_criterion(loss_matrix, n_strategies, n_states, probabilities)
    print("Ожидаемые потери по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {expected_losses[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[bayes_opt]} (минимальные ожидаемые потери)")
    results['Байеса-Лапласа'] = strategies[bayes_opt]

    # 6. Критерий Ходжа-Лемана
    print("\n" + "-" * 50)
    print("6. КРИТЕРИЙ ХОДЖА-ЛЕМАНА (доверие=0.7):")
    hl_values, hl_opt = hodge_lehman_criterion(loss_matrix, n_strategies, n_states, 0.7, probabilities)
    print("Значения критерия Ходжа-Лемана:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {hl_values[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[hl_opt]} (комбинация Байеса и максимина)")
    results['Ходжа-Лемана'] = strategies[hl_opt]

    # 7. Критерий минимальной дисперсии
    print("\n" + "-" * 50)
    print("7. КРИТЕРИЙ МИНИМАЛЬНОЙ ДИСПЕРСИИ:")
    variances, variance_opt = minimum_variance_criterion(loss_matrix, n_strategies, n_states, probabilities)
    print("Дисперсии по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {variances[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[variance_opt]} (минимальный разброс потерь)")
    results['Минимальной дисперсии'] = strategies[variance_opt]

    # 8. Критерий Гермейера
    print("\n" + "-" * 50)
    print("8. КРИТЕРИЙ ГЕРМЕЙЕРА:")
    germeier_values, germeier_opt = germeier_criterion(loss_matrix, n_strategies, n_states, probabilities)
    print("Значения критерия Гермейера:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {germeier_values[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[germeier_opt]} (минимальные взвешенные потери)")
    results['Гермейера'] = strategies[germeier_opt]

    # 9. Критерий Сэвиджа
    print("\n" + "-" * 50)
    print("9. КРИТЕРИЙ СЭВИДЖА:")
    regret_matrix, max_regrets, savage_opt = savage_criterion(loss_matrix, n_strategies, n_states)
    print_matrix(regret_matrix, n_strategies, n_states, strategies, states,
                 "Матрица сожалений:")
    print("\nМаксимальные сожаления по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {max_regrets[i]}")
    print(f"Оптимальная стратегия: {strategies[savage_opt]} (максимальные минимальные сожаления)")
    results['Сэвиджа'] = strategies[savage_opt]

    # Сводная таблица результатов
    print("\n" + "=" * 80)
    print("СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ:")
    print("=" * 80)
    print(f"{'Критерий':<25} {'Оптимальная стратегия':<20} {'Подход':<30}")
    print("-" * 80)

    approach_desc = {
        'Максимин': 'Консервативный',
        'Азартный игрок': 'Оптимистичный',
        'Нейтральный': 'Равновероятный',
        'Гурвица': 'Компромиссный',
        'Байеса-Лапласа': 'Математическое ожидание',
        'Ходжа-Лемана': 'Комбинированный',
        'Минимальной дисперсии': 'Минимизация риска',
        'Гермейера': 'Взвешенный',
        'Сэвиджа': 'Минимизация сожалений'
    }

    for criterion, strategy in results.items():
        print(f"{criterion:<25} {strategy:<20} {approach_desc[criterion]:<30}")

    # Анализ частоты выбора
    print("\n" + "=" * 80)
    print("АНАЛИЗ ЧАСТОТЫ ВЫБОРА СТРАТЕГИЙ:")
    print("=" * 80)

    frequency = {strategy: 0 for strategy in strategies}
    for strategy in results.values():
        frequency[strategy] += 1

    for strategy in strategies:
        print(f"  {strategy}: {frequency[strategy]}/9 критериев")

    # Определение наиболее рекомендуемой стратегии
    max_freq = max(frequency.values())
    best_strategies = [s for s, freq in frequency.items() if freq == max_freq]

    print("\n" + "=" * 80)
    print("ОБЩАЯ РЕКОМЕНДАЦИЯ:")
    print("=" * 80)

    if len(best_strategies) == 1:
        print(f"Стратегия {best_strategies[0]} является оптимальной " +
              f"по {max_freq} из 9 критериев.")
    else:
        print(f"Стратегии {', '.join(best_strategies)} являются оптимальными " +
              f"по {max_freq} критериям каждая.")

    # Дополнительные рекомендации в зависимости от подхода
    print("\nДОПОЛНИТЕЛЬНЫЕ РЕКОМЕНДАЦИИ:")
    print(f"- Для консервативного подхода (избежание риска): {results['Максимин']}")
    print(f"- Для рискованного подхода: {results['Азартный игрок']}")
    print(f"- Для сбалансированного подхода: {results['Гурвица']}")
    print(f"- Для минимизации сожалений: {results['Сэвиджа']}")
    print(f"- Для минимального разброса результатов: {results['Минимальной дисперсии']}")


if __name__ == "__main__":
    main()
