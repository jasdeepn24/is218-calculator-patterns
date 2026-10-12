from calculator.calculation import Calculation


class CalculateCommand:
    def __init__(self, calculation: Calculation, history: list[str], label: str = ""):
        # The command receives the calculation and shared history list.
        self.calculation = calculation
        self.history = history
        self.label = label

    def execute(self) -> float:
        # Only save the calculation if it completes successfully.
        result = self.calculation.execute()
        self.history.append(f"{self.label} = {result}")
        return result


class HistoryCommand:
    def __init__(self, history: list[str]):
        self.history = history

    def execute(self) -> list[str]:
        # Return a copy so the original history cannot be changed.
        return self.history.copy()