import pytest
import time
import os
import tkinter as tk
from memory_profiler import memory_usage
from calculator.CalculatorApp import CalculatorApp


@pytest.fixture
def app():
    """Fixture to set up the CalculatorApp."""
    root = tk.Tk()
    app = CalculatorApp(root, "test_db")
    app.app.update_idletasks()
    yield app  # Provide the app instance to tests
    root.destroy()
    if os.path.exists("test_db"):
        os.remove("test_db")


def test_multiplication_performance_time(app):
    """Test the time performance of multiplication."""
    start_time = time.time()
    
    for _ in range(100):
        app.first_value_entry.focus_force()
        app.bouton_six.invoke()
        app.operator_entry.focus_force()
        app.bouton_multiply.invoke()
        app.second_value_entry.focus_force()
        app.bouton_two.invoke()
        app.bouton_equals.invoke()
        print(app.first_value_entry.get())
        print(app.result_display.cget("text"))
        app.bouton_clear.invoke()
    
    end_time = time.time()
    time_taken = end_time - start_time

    # Assert that the operation completes within acceptable time limits
    assert time_taken < 0.2, f"Time taken too long: {time_taken} seconds"
