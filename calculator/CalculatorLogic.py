

class CalculatorLogic:
    """This class is responsible for the logic of the calculator."""

    def __init__(self):
        self.calcul = ["", "", ""]

    def calculate_result(self):
        """Calculate the result of the calcul."""
        if not self.verify_syntax():
            return "Syntax error"

        first_value = float(self.calcul[0])
        operator = self.calcul[1]
        second_value = float(self.calcul[2])

        if operator == "+":
            return self.add(first_value, second_value)
        elif operator == "-":
            return self.subtract(first_value, second_value)
        elif operator == "*":
            return self.multiply(first_value, second_value)
        elif operator == "/":
            return self.divide(first_value, second_value)
        return "Syntax error"

    def add(self, a, b):
        """Do the addition."""
        return a + b

    def subtract(self, a, b):
        """Do the subtraction."""
        return a - b

    def multiply(self, a, b):
        """Do the multiplication."""
        return a * b

    def divide(self, a, b):
        """Do the division."""
        if b == 0:
            return "Syntax error"
        return a / b

    def verify_syntax(self):
        """Verify the syntax of the calcul."""
        if self.calcul[0] == "" or self.calcul[1] == "" or self.calcul[2] == "":
            return False
        
        try:
            float(self.calcul[0])
            float(self.calcul[2])
        except ValueError:
            return False
        
        if self.calcul[1] not in "+-*/":
            return False
        return True
