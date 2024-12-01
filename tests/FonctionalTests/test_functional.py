import os
import tkinter as tk
import pytest
from calculator.CalculatorApp import CalculatorApp


@pytest.fixture
def app():
    """Fixture to set up the test environment."""
    root = tk.Tk()  # Créer la fenêtre principale
    app = CalculatorApp(root, "test_db")
    app.app.update_idletasks()
    yield app
    root.destroy()
    if os.path.exists("test_db"):
        os.remove("test_db")


def test_add_value_to_first_field(app):
    """Test that values are correctly added to the first value entry."""
    app.first_value_entry.focus_force()
    app.bouton_one.invoke()
    assert app.first_value_entry.get() == '1'


def test_add_value_to_operator_field(app):
    """Test that the operator is correctly added to the operator entry."""
    app.operator_entry.focus_force()
    app.bouton_plus.invoke()
    assert app.operator_entry.get() == '+'


def test_add_value_to_second_field(app):
    """Test that values are correctly added to the second value entry."""
    app.second_value_entry.focus_force()
    app.bouton_one.invoke()
    assert app.second_value_entry.get() == '1'


def test_remove_last_char(app):
    """Test that the last character is removed from the active field."""
    app.second_value_entry.focus_force()
    app.bouton_one.invoke()
    app.bouton_two.invoke()
    app.bouton_three.invoke()
    app.bouton_four.invoke()
    app.bouton_backspace.invoke()
    assert app.second_value_entry.get() == '123'


def test_calculate_result(app):
    """Test that the result is correctly calculated."""
    app.first_value_entry.focus_force()
    app.bouton_one.invoke()
    app.operator_entry.focus_force()
    app.bouton_plus.invoke()
    app.second_value_entry.focus_force()
    app.bouton_two.invoke()
    app.bouton_equals.invoke()
    assert app.result_display.cget("text") == '3.0'


def test_reset_all_fields(app):
    """Test that all fields are correctly reset."""
    app.first_value_entry.focus_force()
    app.bouton_one.invoke()
    app.operator_entry.focus_force()
    app.bouton_plus.invoke()
    app.second_value_entry.focus_force()
    app.bouton_two.invoke()
    app.bouton_equals.invoke()
    app.bouton_clear.invoke()
    assert app.first_value_entry.get() == ''
    assert app.operator_entry.get() == ''
    assert app.second_value_entry.get() == ''
    assert app.result_display.cget("text") == ''


def test_show_history(app):
    """Test that the history is correctly displayed."""
    app.first_value_entry.focus_force()
    app.bouton_one.invoke()
    app.operator_entry.focus_force()
    app.bouton_plus.invoke()
    app.second_value_entry.focus_force()
    app.bouton_two.invoke()
    app.bouton_equals.invoke()
    assert app.history_listbox.get(first=0) == "1 + 2 = 3.0"
