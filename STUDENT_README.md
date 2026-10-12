# My calculator submission

Replace these prompts with your own short explanations.

## Setup, run, and test

Write the commands for your completed project.

This project is a Python command-line calculator that supports addition, subtraction, multiplication, division, and calculation history. It uses object-oriented programming and the Factory, Command, and Strategy patterns.

To set up the project, run:

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

To start the calculator:

python -m calculator

To run the tests and check coverage:

python -m pytest --cov=calculator --cov-report=term-missing --ail-under=100



## Example conversation

Show arithmetic, history, an error, and exit.

> add 5 3
8.0
> subtract 10 4
6.0
> multiply 5 3
15.0
> divide 10 2
5.0
> history
add 5 3 = 8.0
subtract 10 4 = 6.0
multiply 5 3 = 15.0
divide 10 2 = 5.0
> divide 5 0
Cannot divide by zero
> exit

The calculator keeps running until the user enters exit. It also handles invalid commands and numbers without stopping the program. Only successful calculations are added to history.



## Static, class, and instance methods

Explain each using your own method names.

Static methods: The Operations class uses static methods for addition, subtraction, multiplication, and division because they only need the two numbers given to them.

Class methods: The create() method in Calculation uses cls to create a new calculation object. This allows ArithmeticCalculation to inherit and use the factory method.

Instance methods: The execute() method in ArithmeticCalculation uses self to access the numbers and operation stored in that particular calculation.



## Factory, Command, and Strategy

Trace `add 5 3` through your code.

Factory: The ArithmeticCalculation.create() method creates calculation objects. For example, it can create a calculation using the numbers 5 and 3 and the addition operation.

Command: The CalculateCommand class runs a calculation and saves the result to history if it succeeds. The HistoryCommand class returns a copy of the saved history.

Strategy: The dictionary in cli.py connects command names like add and subtract to their operation methods. This lets the program choose the correct operation based on what the user enters.

For example, when the user enters add 5 3, the CLI selects Operations.add from the dictionary. It then creates an ArithmeticCalculation, passes it to CalculateCommand, executes the calculation, and prints the result.



## OOP

Explain encapsulation, abstraction, inheritance, polymorphism, and composition with examples from your code.

Encapsulation: The Calculation class keeps the numbers and selected operation together in one object. HistoryCommand also protects the history by returning a copy of the list instead of the original.

Abstraction: The abstract Calculation class requires subclasses to provide an execute() method without specifying how the calculation must be performed.

Inheritance: ArithmeticCalculation inherits from Calculation and reuses its constructor and create() method.

Polymorphism: CalculateCommand calls execute() on a calculation without needing to know the exact operation being used. Different calculation implementations can follow the same method contract.

Composition: CalculateCommand contains a calculation object, and the calculation object stores an operation function. These parts work together to perform the calculation.



## SOLID

Give one short example for each principle. Describe adding another operation without changing calculation execution.

Single Responsibility: Each part has its own job. Operations handles arithmetic, Calculation stores the calculation details, and the CLI handles user input and output.

Open/Closed: Another arithmetic operation could be added without changing how calculations are executed. The new operation would be added to Operations and registered in the CLI dictionary.

Liskov Substitution: Another subclass of Calculation could be used as long as its execute() method follows the same behavior of returning a numeric result or raising an appropriate error.

Interface Segregation: The calculation interface is kept simple because subclasses only need to implement the execute() method.

Dependency Inversion: CalculateCommand receives a Calculation object instead of directly depending on a specific arithmetic operation. The calculation also receives its operation as a function rather than hard-coding addition.

Adding subtraction, multiplication, and division did not require changing ArithmeticCalculation.execute(). The same method works with all four operation functions.



## Tests and GitHub Actions

Add your successful Actions run URL and confirm 100% line coverage.

I used pytest to test arithmetic operations, calculation objects, commands, history, and the CLI. The tests also cover invalid input, division by zero, negative numbers, decimals, exit, and EOF.

All 34 tests passed with 100% line coverage.

Successful GitHub Actions run:
https://github.com/jasdeepn24/is218-calculator-patterns/actions/runs/38261628400



## Coverage exclusions

The starter excludes the abstract `Calculation.execute()` placeholder because it declares the contract and supplies no implementation. List and explain any other exclusions you add.

The starter code uses # pragma: no cover on the abstract Calculation.execute() placeholder because it only defines a required method and does not perform an actual calculation.

The starter also excludes the if __name__ == "__main__" condition in __main__.py, which is only responsible for starting the program. The CLI startup was still tested using runpy.

No other coverage exclusions were added.