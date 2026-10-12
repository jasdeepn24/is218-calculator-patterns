from calculator.operations import Operations
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand


def main():
    history = []

    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    while True:
        try:
            words = input("> ").split()
        except EOFError:
            break

        if not words:
            continue

        command_name = words[0]

        if command_name == "exit":
            if len(words) != 1:
                print("Exit does not take any numbers.")
                continue
            break

        if command_name == "history":
            if len(words) != 1:
                print("History does not take any numbers.")
                continue

            entries = HistoryCommand(history).execute()

            if not entries:
                print("History is empty.")
            else:
                for entry in entries:
                    print(entry)
            continue

        if command_name not in operations:
            print("Unknown command.")
            continue

        if len(words) != 3:
            print("Please enter exactly two numbers.")
            continue

        try:
            a = float(words[1])
            b = float(words[2])
        except ValueError:
            print("Invalid number.")
            continue

        # Select an operation, create a calculation, and run its command.
        operation = operations[command_name]
        calculation = ArithmeticCalculation.create(a, b, operation)
        label = f"{command_name} {words[1]} {words[2]}"
        command = CalculateCommand(calculation, history, label)

        try:
            result = command.execute()
            print(result)
        except ValueError as error:
            print(error)