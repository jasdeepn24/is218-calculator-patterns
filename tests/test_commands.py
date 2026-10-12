import pytest

from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def test_calculate_command():
    history = []
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calculation, history, "add 5 3")

    assert command.execute() == 8
    assert history == ["add 5 3 = 8"]


def test_failed_calculation_not_saved():
    history = []
    calculation = ArithmeticCalculation.create(5, 0, Operations.divide)
    command = CalculateCommand(calculation, history, "divide 5 0")

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

    assert history == []


def test_history_command():
    history = ["add 5 3 = 8"]
    command = HistoryCommand(history)

    assert command.execute() == ["add 5 3 = 8"]


def test_history_copy_and_empty_history():
    history = []
    command = HistoryCommand(history)

    assert command.execute() == []

    history.append("add 5 3 = 8")
    history_copy = command.execute()
    history_copy.append("subtract 5 3 = 2")

    assert history == ["add 5 3 = 8"]