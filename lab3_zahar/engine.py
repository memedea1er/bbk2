import math
from typing import List, Optional, Tuple, Dict
from models import Hypothesis


class NeilerDecisionEngine:
    def __init__(self, hypotheses: List[Hypothesis]):
        self.hypotheses = hypotheses
        self.probabilities = [h.prior for h in hypotheses]
        self.observed_evidence: Dict[int, Optional[bool]] = {}
        self.all_evidence_ids = set()

        # Пороги
        self.PM = 0.85
        self.M1 = 0.7
        self.M2 = 0.1

        # Вопросы про видеоигры
        self.questions = {
            1: "Насколько вам нравится динамичный геймплей и экшен?",
            2: "Насколько важна для вас сюжетная составляющая?",
            3: "Насколько вы цените тактические элементы и планирование?",
            4: "Насколько вам интересно исследование игрового мира?",
            5: "Насколько важна для вас кастомизация персонажа?",
            6: "Насколько вам нравятся ролевые элементы (прокачка, диалоги)?",
            7: "Насколько важна для вас графика и визуальные эффекты?",
            8: "Насколько вам нравятся многопользовательские режимы?"
        }

        # Инициализация
        for h in hypotheses:
            for evidence_id in h.evidence_map.keys():
                self.all_evidence_ids.add(evidence_id)

        for evidence_id in self.all_evidence_ids:
            self.observed_evidence[evidence_id] = None

    def calculate_evidence_cost(self, evidence_id: int) -> float:
        total_cost = 0.0

        for i, hypothesis in enumerate(self.hypotheses):
            pH = self.probabilities[i]  # P(Hi)
            pNotH = 1.0 - pH  # P(¬Hi)

            # Получаем P(E|Hi) и P(E|¬Hi)
            p_plus, p_minus = hypothesis.evidence_map.get(evidence_id, (0.01, 0.99))

            # P(E) = P(E|Hi)P(Hi) + P(E|¬Hi)P(¬Hi)
            pE = p_plus * pH + p_minus * pNotH
            pNotE = 1.0 - pE

            # P(Hi|E) = P(E|Hi)P(Hi) / P(E)
            pHGivenE = (p_plus * pH) / pE if pE > 1e-9 else 0.0

            # P(Hi|¬E) = (1 - P(E|Hi))P(Hi) / P(¬E)
            pHGivenNotE = ((1.0 - p_plus) * pH) / pNotE if pNotE > 1e-9 else 0.0

            total_cost += abs(pHGivenE - pHGivenNotE)

        return total_cost

    def get_next_question(self) -> Tuple[Optional[int], Optional[str]]:
        unasked = [
            evidence_id for evidence_id, value in self.observed_evidence.items()
            if value is None
        ]

        if not unasked:
            return None, None

        # Выбираем свидетельство с максимальной стоимостью
        best = max(unasked, key=self.calculate_evidence_cost)
        return best, self.questions.get(best)

    def update_probabilities(self, evidence_id: int, user_rating: int) -> None:
        if evidence_id not in self.observed_evidence or self.observed_evidence[evidence_id] is not None:
            return

        observed_likelihood = (user_rating - 1) / 4.0  # 1–5 → [0,1]
        new_probs = [0.0] * len(self.hypotheses)
        total = 0.0

        for i, hypothesis in enumerate(self.hypotheses):
            current_p = self.probabilities[i]
            p_plus, p_minus = hypothesis.evidence_map.get(evidence_id, (0.01, 0.99))

            likelihood = observed_likelihood * p_plus + (1 - observed_likelihood) * p_minus
            new_probs[i] = current_p * likelihood
            total += new_probs[i]

        if total > 1e-9:
            self.probabilities = [p / total for p in new_probs]
        else:
            uniform = 1.0 / len(self.hypotheses)
            self.probabilities = [uniform] * len(self.hypotheses)

        self.observed_evidence[evidence_id] = True

    def check_stopping_condition(self) -> Tuple[bool, str]:
        if not any(value is True for value in self.observed_evidence.values()):
            return False, ""

        p_max = max(self.probabilities)
        p_min = min(self.probabilities)
        best_index = self.probabilities.index(p_max)

        # Правило 1: Останов по наиболее вероятной гипотезе
        if p_max > self.PM:
            hypothesis_name = self.hypotheses[best_index].name
            return True, f"{hypothesis_name} (уверенность: {p_max:.0%})"

        # Правило 2: Останов по правдоподобной гипотезе
        if p_min > self.M1:
            hypothesis_name = self.hypotheses[best_index].name
            return True, f"{hypothesis_name} (все варианты достаточно вероятны)"

        # Правило 3: Невозможно выбрать заключение
        if p_max < self.M2:
            return True, "Не удалось определить подходящую игру."

        # Если вопросы закончились
        if all(value is not None for value in self.observed_evidence.values()):
            hypothesis_name = self.hypotheses[best_index].name
            return True, f"{hypothesis_name} (наиболее вероятный вариант)"

        return False, ""