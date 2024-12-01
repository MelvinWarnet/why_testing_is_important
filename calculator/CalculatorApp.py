import tkinter as tkinter
import tkinter.font as tkFont
from CalculatorLogic import CalculatorLogic
from DatabaseManager import DatabaseManager


class CalculatorApp:
    """This class is responsible for the IHM of the calculator."""

    def add_to_field(self, value):
        """Add a value to the active field."""
        if(self.first_value_entry == self.app.focus_get()):
            self.first_value_entry.insert(tkinter.END, value)
        elif(self.operator_entry == self.app.focus_get()):
            self.operator_entry.delete(0, tkinter.END)
            self.operator_entry.insert(tkinter.END, value)
        elif(self.second_value_entry == self.app.focus_get()):
            self.second_value_entry.insert(tkinter.END, value)
        else:
            self.first_value_entry.insert(tkinter.END, value)

    def reset_all_fields(self):
        """Reset all fields."""
        self.first_value_entry.delete(0, tkinter.END)
        self.operator_entry.delete(0, tkinter.END)
        self.second_value_entry.delete(0, tkinter.END)
        self.result_display.config(text="")

    def remove_last_char(self):
        """Remove the last character of the active field."""
        if(self.first_value_entry == self.app.focus_get()):
            self.first_value_entry.delete(len(self.first_value_entry.get())-1, tkinter.END)
        elif(self.second_value_entry == self.app.focus_get()):
            self.second_value_entry.delete(len(self.second_value_entry.get())-1, tkinter.END)
        elif(self.operator_entry == self.app.focus_get()):
            self.operator_entry.delete(len(self.operator_entry.get())-1, tkinter.END)
        else:
            self.first_value_entry.delete(len(self.first_value_entry.get())-1, tkinter.END)

    def get_result(self):
        """Calculate the result and display it."""
        first_value = self.first_value_entry.get()
        operator = self.operator_entry.get()
        second_value = self.second_value_entry.get()
        self.calculator_logic.calcul[0] = first_value
        self.calculator_logic.calcul[1] = operator
        self.calculator_logic.calcul[2] = second_value
        result = self.calculator_logic.calculate_result()
        self.db_manager.save_calculation(first_value, operator, second_value, result)
        self.show_history()
        self.result_display.config(text=result)

    def show_history(self):
        """Show the calculation history from the database."""
        calculations = self.db_manager.get_history()
        calculations.reverse()

        self.history_listbox.delete(0, tkinter.END)
        for calc in calculations:
            self.history_listbox.insert(tkinter.END, f"{calc[0]} {calc[1]} {calc[2]} = {calc[3]}")


    def __init__(self, app):
        """Initializes the calculator app."""
        self.db_manager = DatabaseManager()
        self.calculator_logic = CalculatorLogic()
        self.app = app
        self.app.title("Calculator")
        self.app.geometry("483x650")
        self.app.configure(background='light grey')

        self.font = tkFont.Font(family="Digital-7", size=32)

        self.result_display = tkinter.Label(self.app, text="", font=self.font, height=2, width=24, bg="black", fg="white")
        self.result_display.grid(row=0, column=0, columnspan=5, pady=2)

        self.first_value_entry = tkinter.Entry(self.app, font=self.font, width=8, justify="center", bd=8, relief="ridge", bg="black", fg="white", insertbackground="white")
        self.first_value_entry.grid(row=1, column=0, columnspan=2, pady=2)

        self.operator_entry = tkinter.Entry(self.app, font=self.font, width=2, justify="center", bd=8, relief="ridge", bg="black", fg="white", insertbackground="white")
        self.operator_entry.grid(row=1, column=2, columnspan=1, pady=2)

        self.second_value_entry = tkinter.Entry(self.app, font=self.font,  width=8, justify="center", bd=8, relief="ridge", bg="black", fg="white", insertbackground="white")
        self.second_value_entry.grid(row=1, column=3, columnspan=2, pady=2)

        bouton = tkinter.Button(self.app, text="1",  width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("1"))
        bouton.grid(row=2, column=0, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="2", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("2"))
        bouton.grid(row=2, column=1, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="3", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("3"))
        bouton.grid(row=2, column=2, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="<--", width=15, height=2, font=("Arial", 14, "bold"), bg="red", fg="white" ,command=self.remove_last_char)
        bouton.grid(row=2, column=3, columnspan=2, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="4", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("4"))
        bouton.grid(row=3, column=0, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="5", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("5"))
        bouton.grid(row=3, column=1, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="6", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("6"))
        bouton.grid(row=3, column=2, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="+", width=5, height=2, font=("Arial", 14, "bold"), bg="orange", fg="white" ,command=lambda: self.add_to_field("+"))
        bouton.grid(row=3, column=3, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="-", width=5, height=2, font=("Arial", 14, "bold"), bg="orange", fg="white" ,command=lambda: self.add_to_field("-"))
        bouton.grid(row=3, column=4, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="7", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("7"))
        bouton.grid(row=4, column=0, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="8", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("8"))
        bouton.grid(row=4, column=1, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="9", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("9"))
        bouton.grid(row=4, column=2, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="*", width=5, height=2, font=("Arial", 14, "bold"), bg="orange", fg="white" ,command=lambda: self.add_to_field("*"))
        bouton.grid(row=4, column=3, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="/", width=5, height=2, font=("Arial", 14, "bold"), bg="orange", fg="white" ,command=lambda: self.add_to_field("/"))
        bouton.grid(row=4, column=4, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text=".", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("."))
        bouton.grid(row=5, column=0, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="0", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("0"))
        bouton.grid(row=5, column=1, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="00", width=5, height=2, font=("Arial", 14, "bold"), bg="grey", fg="white" ,command=lambda: self.add_to_field("00"))
        bouton.grid(row=5, column=2, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="C", width=5, height=2, font=("Arial", 14, "bold"), bg="red", fg="white" ,command=self.reset_all_fields)
        bouton.grid(row=5, column=3, padx=2, pady=2)

        bouton = tkinter.Button(self.app, text="=", width=5, height=2, font=("Arial", 14, "bold"), bg="green", fg="white" ,command=self.get_result)
        bouton.grid(row=5, column=4, padx=2, pady=2)

        self.history_listbox = tkinter.Listbox(self.app, font=("Arial", 14, "bold"), width=30, height=7, fg="black")
        self.history_listbox.grid(row=7, column=0, columnspan=5, pady=2)
        self.show_history()