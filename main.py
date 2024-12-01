import tkinter
from calculator.CalculatorApp import CalculatorApp

if __name__ == "__main__":
    try:
        app = tkinter.Tk()
        myApp = CalculatorApp(app, "calculator.db")
        app.mainloop()
    except Exception as e:
        print(f"Error : {e}")
