import tkinter as tk
from tkinter import messagebox

# Welcome Window class (Login page)
class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dynamic Budget Tracker - Login")
        self.geometry("300x200")

        # Title label
        self.label = tk.Label(self, text="Welcome to Dynamic Budget Tracker", font=("Arial", 14))
        self.label.pack(pady=20)

        # Username field
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Password field
        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Buttons for login and exit
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=5)

    # Function to validate login input
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simple check for empty fields
        if username == "" or password == "":
            messagebox.showerror("Error", "Username and password cannot be empty.")
        else:
            self.destroy()
            self.open_budget_tracker()

    def exit_app(self):
        self.quit()

    def open_budget_tracker(self):
        # Open the main budget tracker window
        TrackerWindow()

# Main Budget Tracker Window class
class TrackerWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dynamic Budget Tracker")
        self.geometry("400x400")

        # Labels
        self.income_label = tk.Label(self, text="Monthly Income:")
        self.income_label.pack(pady=5)
        self.income_entry = tk.Entry(self)
        self.income_entry.pack()

        self.expense_label = tk.Label(self, text="Enter Expense Categories (comma separated):")
        self.expense_label.pack(pady=5)
        self.expense_entry = tk.Entry(self)
        self.expense_entry.pack()

        self.remaining_label = tk.Label(self, text="Remaining Budget: $0")
        self.remaining_label.pack(pady=10)

        # Buttons
        self.add_expense_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=5)

        self.view_summary_button = tk.Button(self, text="View Summary", command=self.view_summary)
        self.view_summary_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=5)

        # Variables for calculations
        self.total_income = 0
        self.total_expenses = 0

    # Function to add expense
    def add_expense(self):
        try:
            income = float(self.income_entry.get())
            expenses = self.expense_entry.get().split(",")
            total_expenses = sum([float(expense) for expense in expenses if expense.strip().replace(".", "", 1).isdigit()])

            self.total_income = income
            self.total_expenses = total_expenses

            self.update_remaining_budget()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for income and expenses.")

    # Function to update remaining budget
    def update_remaining_budget(self):
        remaining_budget = self.total_income - self.total_expenses
        self.remaining_label.config(text=f"Remaining Budget: ${remaining_budget:.2f}")

    # Function to show summary
    def view_summary(self):
        summary = f"Total Income: ${self.total_income:.2f}\n"
        summary += f"Total Expenses: ${self.total_expenses:.2f}\n"
        summary += f"Remaining Budget: ${self.total_income - self.total_expenses:.2f}"

        messagebox.showinfo("Summary", summary)

if __name__ == "__main__":
    app = WelcomeWindow()
    app.mainloop()
