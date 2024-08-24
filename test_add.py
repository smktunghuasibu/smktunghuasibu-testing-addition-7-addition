import add
import pytest

def test_sum():
    result = add.sum(2,5)
    assert result == 7

def test_addition(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3", "4"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    add.addition()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Sum of 3 and 4 is 7"