import pytest
import tkinter as tk
import os
from calculator.CalculatorApp import CalculatorApp

@pytest.fixture
def app():
    """Fixture to create the app instance and run it."""
    db_name = "temp.db"
    root = tk.Tk()
    app = CalculatorApp(root, db_name)
    yield app
    root.quit()  # Close the app after the test
    if os.path.exists(db_name):
        os.remove(db_name)

def test_calculation_integration(app):
    """Test full calculation process: adding values, calculating, and saving to the database."""

    # Add values directly to the fields
    app.first_value_entry.delete(0, tk.END)  # Clear any existing value
    app.first_value_entry.insert(tk.END, "5.4")

    app.operator_entry.delete(0, tk.END)
    app.operator_entry.insert(tk.END, "+")

    app.second_value_entry.delete(0, tk.END)
    app.second_value_entry.insert(tk.END, "3.8")

    # Perform the calculation
    app.get_result()
    
    # Check if the calculation is saved in the database
    conn = app.db_manager._connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM calculations WHERE first_value = '5.4' AND operator = '+' AND second_value = '3.8'")
    result_row = cursor.fetchone()
    app.db_manager._disconnect(conn)
    
    assert result_row is not None, "The calculation should be saved in the database."
    assert result_row[4] == "9.2", "The result should be '9.2' in the database."



def test_remove_last_character(app):
    """Test that the 'remove last character' functionality works as expected."""
    
    # Add values to the calculator
    app.add_to_field("5")
    app.add_to_field("+")
    app.add_to_field("3")
    
    # Remove the last character
    app.remove_last_char()
    result = app.first_value_entry.get()  # This should now be '5+'
    assert result == "5+", f"Expected first value to be '5+', but got {result}."
    
    app.remove_last_char()
    result = app.first_value_entry.get()  # This should now be '5'
    assert result == "5", f"Expected first value to be '5', but got {result}."


def test_empty_history_when_no_calculations(app):
    """Test that the history is empty when no calculations have been made."""
    
    # Check the history when no calculations are performed
    history_items = app.history_listbox.get(0, tk.END)
    assert len(history_items) == 0, "The history should be empty if no calculations have been made."


def test_reset_all_fields(app):
    """Test that the 'reset all fields' functionality works as expected."""
    
    # Add values to the calculator
    app.add_to_field("5")
    app.add_to_field("+")
    app.add_to_field("3")
    
    # Reset all fields
    app.reset_all_fields()
    
    # Check if all fields are empty
    assert app.first_value_entry.get() == "", "First value field should be empty after reset."
    assert app.operator_entry.get() == "", "Operator field should be empty after reset."
    assert app.second_value_entry.get() == "", "Second value field should be empty after reset."
    assert app.result_display.cget("text") == "", "Result display should be empty after reset."