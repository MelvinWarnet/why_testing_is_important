import sqlite3

class DatabaseManager:
    """Class to handle database interactions."""
    
    def __init__(self, db_name="calculations.db"):
        """Initialize the DatabaseManager with the database name."""
        self.db_name = db_name
        self.create_table()
    
    def _connect(self):
        """Create and return a database connection."""
        return sqlite3.connect(self.db_name)
    
    def _disconnect(self, conn):
        """Disconnect from the database."""
        conn.close

    def create_table(self):
        """Create the table for storing calculations if it doesn't exist."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_value TEXT,
                operator TEXT,
                second_value TEXT,
                result TEXT
            )
        ''')
        conn.commit()
        self._disconnect(conn)

    def save_calculation(self, first_value, operator, second_value, result):
        """Save a calculation into the database."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO calculations (first_value, operator, second_value, result)
            VALUES (?, ?, ?, ?)
        ''', (first_value, operator, second_value, result))
        conn.commit()
        self._disconnect(conn)

    def get_history(self):
        """Retrieve the history of calculations."""
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('SELECT first_value, operator, second_value, result FROM calculations')
        calculations = cursor.fetchall()
        self._disconnect(conn)
        return calculations
