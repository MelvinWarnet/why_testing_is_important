import pytest
import sqlite3
import os
from calculator.DatabaseManager import DatabaseManager

@pytest.fixture
def db_manager():
    """Fixture to initialize a DatabaseManager object for each test."""
    db_name = "temp.db"
    db = DatabaseManager(db_name)
    yield db
    if os.path.exists(db_name):
        os.remove(db_name)

def test_create_table(db_manager):
    """Test the creation of the table in the database."""
    conn = db_manager._connect()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='calculations'")
    table_exists = cursor.fetchone() is not None
    db_manager._disconnect(conn)
    assert table_exists, "Table 'calculations' should be created in the database."

def test_save_calculation(db_manager):
    """Test saving a calculation into the database."""
    db_manager.save_calculation("5", "+", "3", "8")
    conn = db_manager._connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM calculations WHERE first_value = '5' AND operator = '+' AND second_value = '3'")
    result = cursor.fetchone()
    db_manager._disconnect(conn)
    assert result is not None, "The calculation should be saved in the database."
    assert result[1] == "5", "The first_value should be '5'."
    assert result[2] == "+", "The operator should be '+'."
    assert result[3] == "3", "The second_value should be '3'."
    assert result[4] == "8", "The result should be '8'."

def test_get_history(db_manager):
    """Test retrieving the calculation history."""
    db_manager.save_calculation("5", "+", "3", "8")
    history = db_manager.get_history()
    assert len(history) == 1, "There should be one calculation in the history."
    assert history[0] == ("5", "+", "3", "8"), "The history should contain the correct calculation."

def test_save_multiple_calculations(db_manager):
    """Test saving multiple calculations."""
    db_manager.save_calculation("5", "+", "3", "8")
    db_manager.save_calculation("10", "-", "4", "6")
    history = db_manager.get_history()
    assert len(history) == 2, "There should be two calculations in the history."
    assert history[1] == ("10", "-", "4", "6"), "The second calculation should be saved correctly."

def test_no_results_in_empty_db(db_manager):
    """Test that no calculations are returned if the database is empty."""
    history = db_manager.get_history()
    assert len(history) == 0, "The history should be empty if no calculations have been saved."
