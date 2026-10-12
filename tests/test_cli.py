import runpy

from calculator.cli import main


def test_calculations_and_history(monkeypatch, capsys):
    inputs = iter([
        "add 5 3",
        "subtract 10 4",
        "multiply -2 3",
        "divide 5 2",
        "history",
        "exit",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "8.0" in output
    assert "6.0" in output
    assert "-6.0" in output
    assert "2.5" in output
    assert "add 5 3 = 8.0" in output
    assert "subtract 10 4 = 6.0" in output
    assert "multiply -2 3 = -6.0" in output
    assert "divide 5 2 = 2.5" in output


def test_empty_history_and_blank_input(monkeypatch, capsys):
    inputs = iter(["", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "History is empty." in output


def test_errors_and_continuing(monkeypatch, capsys):
    inputs = iter([
        "unknown",
        "add 5",
        "add 5 3 2",
        "add hello 3",
        "divide 5 0",
        "add 1 2",
        "history",
        "exit",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Unknown command." in output
    assert "Please enter exactly two numbers." in output
    assert "Invalid number." in output
    assert "Cannot divide by zero" in output
    assert "3.0" in output
    assert "add 1 2 = 3.0" in output
    assert "divide 5 0 =" not in output


def test_exit_with_extra_input(monkeypatch, capsys):
    inputs = iter(["exit 1", "add 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "Exit does not take any numbers." in output
    assert "3.0" in output


def test_history_with_extra_input(monkeypatch, capsys):
    inputs = iter(["history 1", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    output = capsys.readouterr().out

    assert "History does not take any numbers." in output


def test_eof(monkeypatch):
    def fake_input(prompt):
        raise EOFError

    monkeypatch.setattr("builtins.input", fake_input)

    main()


def test_main_entry_point(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "exit")

    runpy.run_module("calculator", run_name="__main__")