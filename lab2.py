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

def create_gain_matrix(loss_matrix):
    """Преобразование матрицы потерь в матрицу выигрышей"""
    gain_matrix = []
    n_strategies = len(loss_matrix)
    n_states = len(loss_matrix[0])
    
    # Находим максимальное значение в матрице для преобразования
    max_val = 0
    for i in range(n_strategies):
        for j in range(n_states):
            if loss_matrix[i][j] > max_val:
                max_val = loss_matrix[i][j]
    
    # Преобразуем потери в выигрыши (чем меньше потери - тем больше выигрыш)
    for i in range(n_strategies):
        row = []
        for j in range(n_states):
            row.append(max_val - loss_matrix[i][j])
        gain_matrix.append(row)
    
    return gain_matrix

def maximin_criterion(gain_matrix, n_strategies, n_states):
    """Критерий максимина (для матрицы выигрышей)"""
    min_gains = []
    for i in range(n_strategies):
        min_gain = gain_matrix[i][0]
        for j in range(1, n_states):
            if gain_matrix[i][j] < min_gain:
                min_gain = gain_matrix[i][j]
        min_gains.append(min_gain)
    
    # Находим оптимальную стратегию (максимальный минимальный выигрыш)
    max_min_gain = min_gains[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if min_gains[i] > max_min_gain:
            max_min_gain = min_gains[i]
            optimal_strategy = i
    
    return min_gains, optimal_strategy

def gambler_criterion(gain_matrix, n_strategies, n_states):
    """Критерий азартного игрока"""
    max_gains = []
    for i in range(n_strategies):
        max_gain = gain_matrix[i][0]
        for j in range(1, n_states):
            if gain_matrix[i][j] > max_gain:
                max_gain = gain_matrix[i][j]
        max_gains.append(max_gain)
    
    # Находим оптимальную стратегию (максимальный максимальный выигрыш)
    max_max_gain = max_gains[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if max_gains[i] > max_max_gain:
            max_max_gain = max_gains[i]
            optimal_strategy = i
    
    return max_gains, optimal_strategy

def neutral_criterion(gain_matrix, n_strategies, n_states):
    """Нейтральный критерий (равные вероятности)"""
    averages = []
    for i in range(n_strategies):
        total = 0
        for j in range(n_states):
            total += gain_matrix[i][j]
        averages.append(total / n_states)
    
    # Находим оптимальную стратегию (максимальное среднее)
    max_avg = averages[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if averages[i] > max_avg:
            max_avg = averages[i]
            optimal_strategy = i
    
    return averages, optimal_strategy

def hurwitz_criterion(gain_matrix, n_strategies, n_states, alpha=0.5):
    """Критерий Гурвица"""
    hurwitz_values = []
    
    for i in range(n_strategies):
        min_gain = gain_matrix[i][0]
        max_gain = gain_matrix[i][0]
        
        for j in range(1, n_states):
            if gain_matrix[i][j] < min_gain:
                min_gain = gain_matrix[i][j]
            if gain_matrix[i][j] > max_gain:
                max_gain = gain_matrix[i][j]
        
        # alpha * min + (1-alpha) * max
        hurwitz_value = alpha * min_gain + (1 - alpha) * max_gain
        hurwitz_values.append(hurwitz_value)
    
    # Находим оптимальную стратегию
    max_hurwitz = hurwitz_values[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if hurwitz_values[i] > max_hurwitz:
            max_hurwitz = hurwitz_values[i]
            optimal_strategy = i
    
    return hurwitz_values, optimal_strategy

def bayes_laplace_criterion(gain_matrix, n_strategies, n_states, probabilities=None):
    """Критерий Байеса-Лапласа"""
    if probabilities is None:
        # Равномерное распределение
        probability = 1.0 / n_states
        probabilities = [probability] * n_states
    
    expected_gains = []
    
    for i in range(n_strategies):
        expected_gain = 0.0
        for j in range(n_states):
            expected_gain += gain_matrix[i][j] * probabilities[j]
        expected_gains.append(expected_gain)
    
    # Находим оптимальную стратегию
    max_expected_gain = expected_gains[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if expected_gains[i] > max_expected_gain:
            max_expected_gain = expected_gains[i]
            optimal_strategy = i
    
    return expected_gains, optimal_strategy

def hodge_lehman_criterion(gain_matrix, n_strategies, n_states, confidence=0.5, probabilities=None):
    """Критерий Ходжа-Лемана"""
    if probabilities is None:
        probability = 1.0 / n_states
        probabilities = [probability] * n_states
    
    hl_values = []
    
    for i in range(n_strategies):
        # Байесовская часть
        bayes_part = 0.0
        for j in range(n_states):
            bayes_part += gain_matrix[i][j] * probabilities[j]
        
        # Максиминная часть
        min_gain = gain_matrix[i][0]
        for j in range(1, n_states):
            if gain_matrix[i][j] < min_gain:
                min_gain = gain_matrix[i][j]
        
        # Комбинация
        hl_value = confidence * bayes_part + (1 - confidence) * min_gain
        hl_values.append(hl_value)
    
    # Находим оптимальную стратегию
    max_hl = hl_values[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if hl_values[i] > max_hl:
            max_hl = hl_values[i]
            optimal_strategy = i
    
    return hl_values, optimal_strategy

def minimum_variance_criterion(gain_matrix, n_strategies, n_states, probabilities=None):
    """Критерий минимальной дисперсии"""
    if probabilities is None:
        probability = 1.0 / n_states
        probabilities = [probability] * n_states
    
    variances = []
    
    for i in range(n_strategies):
        # Сначала находим математическое ожидание
        expected = 0.0
        for j in range(n_states):
            expected += gain_matrix[i][j] * probabilities[j]
        
        # Затем дисперсию
        variance = 0.0
        for j in range(n_states):
            deviation = gain_matrix[i][j] - expected
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

def germeier_criterion(gain_matrix, n_strategies, n_states, probabilities=None):
    """Критерий Гермейера"""
    if probabilities is None:
        probability = 1.0 / n_states
        probabilities = [probability] * n_states
    
    germeier_values = []
    
    for i in range(n_strategies):
        min_weighted_gain = gain_matrix[i][0] * probabilities[0]
        for j in range(1, n_states):
            weighted_gain = gain_matrix[i][j] * probabilities[j]
            if weighted_gain < min_weighted_gain:
                min_weighted_gain = weighted_gain
        germeier_values.append(min_weighted_gain)
    
    # Находим оптимальную стратегию
    max_germeier = germeier_values[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if germeier_values[i] > max_germeier:
            max_germeier = germeier_values[i]
            optimal_strategy = i
    
    return germeier_values, optimal_strategy

def savage_criterion(gain_matrix, n_strategies, n_states):
    """Критерий Сэвиджа (минимаксных сожалений)"""
    # Находим максимальные выигрыши по каждому столбцу
    max_gains = []
    for j in range(n_states):
        col_max = gain_matrix[0][j]
        for i in range(1, n_strategies):
            if gain_matrix[i][j] > col_max:
                col_max = gain_matrix[i][j]
        max_gains.append(col_max)
    
    # Строим матрицу сожалений
    regret_matrix = []
    for i in range(n_strategies):
        row = []
        for j in range(n_states):
            row.append(max_gains[j] - gain_matrix[i][j])
        regret_matrix.append(row)
    
    # Находим максимальные сожаления для каждой стратегии
    max_regrets = []
    for i in range(n_strategies):
        max_regret = regret_matrix[i][0]
        for j in range(1, n_states):
            if regret_matrix[i][j] > max_regret:
                max_regret = regret_matrix[i][j]
        max_regrets.append(max_regret)
    
    # Находим оптимальную стратегию (минимальное максимальное сожаление)
    min_max_regret = max_regrets[0]
    optimal_strategy = 0
    for i in range(1, n_strategies):
        if max_regrets[i] < min_max_regret:
            min_max_regret = max_regrets[i]
            optimal_strategy = i
    
    return regret_matrix, max_regrets, optimal_strategy

def main():
    # Исходные данные (матрица потерь)
    loss_matrix = [
        [5, 10, 18, 25],   # Q1
        [8, 7, 8, 23],     # Q2
        [21, 18, 12, 21],  # Q3
        [30, 22, 19, 15]   # Q4
    ]
    
    strategies = ['Q1', 'Q2', 'Q3', 'Q4']
    states = ['200', '250', '300', '350']
    
    n_strategies = len(strategies)
    n_states = len(states)
    
    # Преобразуем матрицу потерь в матрицу выигрышей
    gain_matrix = create_gain_matrix(loss_matrix)
    
    print("=" * 80)
    print("ПОЛНЫЙ АНАЛИЗ ОПТИМАЛЬНОГО УРОВНЯ ПРЕДЛОЖЕНИЯ УСЛУГ")
    print("=" * 80)
    
    # Вывод исходных матриц
    print_matrix(loss_matrix, n_strategies, n_states, strategies, states, 
                "ИСХОДНАЯ МАТРИЦА ПОТЕРЬ (в тыс. руб.):")
    
    print_matrix(gain_matrix, n_strategies, n_states, strategies, states,
                "МАТРИЦА ВЫИГРЫШЕЙ (преобразованная):")
    
    # Вероятности для критериев (предположим равные)
    probabilities = [0.25, 0.25, 0.25, 0.25]
    
    results = {}
    
    # 1. Критерий максимина
    print("\n" + "=" * 80)
    print("1. КРИТЕРИЙ МАКСИМИНА (Вальда):")
    min_gains, maximin_opt = maximin_criterion(gain_matrix, n_strategies, n_states)
    print("Минимальные выигрыши по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {min_gains[i]}")
    print(f"Оптимальная стратегия: {strategies[maximin_opt]}")
    results['Максимин'] = strategies[maximin_opt]
    
    # 2. Критерий азартного игрока
    print("\n" + "-" * 50)
    print("2. КРИТЕРИЙ АЗАРТНОГО ИГРОКА:")
    max_gains, gambler_opt = gambler_criterion(gain_matrix, n_strategies, n_states)
    print("Максимальные выигрыши по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {max_gains[i]}")
    print(f"Оптимальная стратегия: {strategies[gambler_opt]}")
    results['Азартный игрок'] = strategies[gambler_opt]
    
    # 3. Нейтральный критерий
    print("\n" + "-" * 50)
    print("3. НЕЙТРАЛЬНЫЙ КРИТЕРИЙ:")
    averages, neutral_opt = neutral_criterion(gain_matrix, n_strategies, n_states)
    print("Средние выигрыши по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {averages[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[neutral_opt]}")
    results['Нейтральный'] = strategies[neutral_opt]
    
    # 4. Критерий Гурвица
    print("\n" + "-" * 50)
    print("4. КРИТЕРИЙ ГУРВИЦА (α=0.5):")
    hurwitz_values, hurwitz_opt = hurwitz_criterion(gain_matrix, n_strategies, n_states, 0.5)
    print("Значения критерия Гурвица:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {hurwitz_values[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[hurwitz_opt]}")
    results['Гурвица'] = strategies[hurwitz_opt]
    
    # 5. Критерий Байеса-Лапласа
    print("\n" + "-" * 50)
    print("5. КРИТЕРИЙ БАЙЕСА-ЛАПЛАСА:")
    expected_gains, bayes_opt = bayes_laplace_criterion(gain_matrix, n_strategies, n_states, probabilities)
    print("Ожидаемые выигрыши по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {expected_gains[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[bayes_opt]}")
    results['Байеса-Лапласа'] = strategies[bayes_opt]
    
    # 6. Критерий Ходжа-Лемана
    print("\n" + "-" * 50)
    print("6. КРИТЕРИЙ ХОДЖА-ЛЕМАНА (доверие=0.5):")
    hl_values, hl_opt = hodge_lehman_criterion(gain_matrix, n_strategies, n_states, 0.5, probabilities)
    print("Значения критерия Ходжа-Лемана:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {hl_values[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[hl_opt]}")
    results['Ходжа-Лемана'] = strategies[hl_opt]
    
    # 7. Критерий минимальной дисперсии
    print("\n" + "-" * 50)
    print("7. КРИТЕРИЙ МИНИМАЛЬНОЙ ДИСПЕРСИИ:")
    variances, variance_opt = minimum_variance_criterion(gain_matrix, n_strategies, n_states, probabilities)
    print("Дисперсии по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {variances[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[variance_opt]}")
    results['Минимальной дисперсии'] = strategies[variance_opt]
    
    # 8. Критерий Гермейера
    print("\n" + "-" * 50)
    print("8. КРИТЕРИЙ ГЕРМЕЙЕРА:")
    germeier_values, germeier_opt = germeier_criterion(gain_matrix, n_strategies, n_states, probabilities)
    print("Значения критерия Гермейера:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {germeier_values[i]:.2f}")
    print(f"Оптимальная стратегия: {strategies[germeier_opt]}")
    results['Гермейера'] = strategies[germeier_opt]
    
    # 9. Критерий Сэвиджа
    print("\n" + "-" * 50)
    print("9. КРИТЕРИЙ СЭВИДЖА:")
    regret_matrix, max_regrets, savage_opt = savage_criterion(gain_matrix, n_strategies, n_states)
    print_matrix(regret_matrix, n_strategies, n_states, strategies, states, 
                "Матрица сожалений:")
    print("\nМаксимальные сожаления по стратегиям:")
    for i, strategy in enumerate(strategies):
        print(f"  {strategy}: {max_regrets[i]}")
    print(f"Оптимальная стратегия: {strategies[savage_opt]}")
    results['Сэвиджа'] = strategies[savage_opt]
    
    # Сводная таблица результатов
    print("\n" + "=" * 80)
    print("СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ:")
    print("=" * 80)
    print(f"{'Критерий':<25} {'Оптимальная стратегия':<20}")
    print("-" * 50)
    
    for criterion, strategy in results.items():
        print(f"{criterion:<25} {strategy:<20}")
    
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
    
    # Дополнительные рекомендации
    print("\nДОПОЛНИТЕЛЬНЫЕ РЕКОМЕНДАЦИИ:")
    print(f"- Для консервативного подхода (избежание риска): {results['Максимин']}")
    print(f"- Для рискованного подхода: {results['Азартный игрок']}")
    print(f"- Для сбалансированного подхода: {results['Гурвица']}")
    print(f"- Для минимизации сожалений: {results['Сэвиджа']}")

if __name__ == "__main__":
    main()
