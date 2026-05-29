
class Transaction:

    def __init__(self, transaction_id, user_id, amount, category, transaction_type):

        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type

    def add_transaction(self):
        print("Transaction added:", self.category, "-", self.amount)

class Goal:

    def __init__(self, goal_id, user_id, goal_name, target_amount):

        self.goal_id = goal_id
        self.user_id = user_id
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.saved_amount = 0
        self.status = "IN_PROGRESS"

    def update_progress(self, amount):
        self.saved_amount += amount

        if self.saved_amount >= self.target_amount:
            self.status = "COMPLETED"
            print("Goal completed!")

        else:
            print("Progress:", self.saved_amount, "/", self.target_amount)

    def calculate_remaining(self):
        return self.target_amount - self.saved_amount

class Statistics:

    def __init__(self):

        self.total_income = 0
        self.total_expenses = 0
        self.monthly_savings = 0

    def calculate(self, transactions):

        self.total_income = 0
        self.total_expenses = 0

        for t in transactions:
            if t.transaction_type == "INCOME":
                self.total_income += t.amount
            else:
                self.total_expenses += t.amount
        self.monthly_savings = self.total_income - self.total_expenses

    def show_statistics(self):

        print("\n===== STATISTICS =====")
        print("Income:", self.total_income)
        print("Expenses:", self.total_expenses)
        print("Savings:", self.monthly_savings)

        if self.monthly_savings < 0:
            print("Warning! Expenses exceed income!")

class Notification:

    def __init__(self, message, notification_type):

        self.message = message
        self.notification_type = notification_type

    def show_notification(self):

        print("\n===== SMART NOTIFICATION =====")
        print("Type:", self.notification_type)
        print("Message:", self.message)
        print("================================")

class User:

    def __init__(self, user_id, name, email, password, monthly_budget):

        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.monthly_budget = monthly_budget
        self.balance = 0

    def add_income(self, amount):

        self.balance += amount
        print("Income added. Balance:", self.balance)

    def add_expense(self, amount):

        self.balance -= amount
        print("Expense added. Balance:", self.balance)

class FinanceSystem:

    def __init__(self):

        self.users = []
        self.transactions = []
        self.goals = []

    def add_user(self, user):

        self.users.append(user)
        print("User registered:", user.name)

    def add_transaction(self, transaction):

        self.transactions.append(transaction)
        transaction.add_transaction()

    def create_goal(self, goal):

        self.goals.append(goal)
        print("Goal created:", goal.goal_name)

    def generate_statistics(self):

        stats = Statistics()
        stats.calculate(self.transactions)
        return stats

    def send_notification(self, message, notification_type):

        notif = Notification(message, notification_type)
        notif.show_notification()

    def smart_notification(self, user):

        if user.balance < 0:

            self.send_notification(
                "Your balance is negative!",
                "WARNING"
            )

        elif user.balance < 1000:

            self.send_notification(
                "Your balance is very low!",
                "ALERT"
            )

        elif user.balance > user.monthly_budget:

            self.send_notification(
                "Excellent! Your balance is above monthly budget.",
                "SUCCESS"
            )

print("====================================")
print("      SMART FINANCE TRACKER")
print("====================================")



system = FinanceSystem()
print("\n===== REGISTER =====")

name = input("Name: ")
email = input("Email: ")
password = input("Create password: ")
monthly_budget = int(input("Monthly budget: "))

user = User(
    1,
    name,
    email,
    password,
    monthly_budget
)

system.add_user(user)

print("\n===== LOGIN =====")
login_email = input("Enter email: ")
login_password = input("Enter password: ")

if login_email == user.email and login_password == user.password:

    print("\nLogin successful!")

    system.send_notification(
        "Welcome to Smart Finance Tracker!",
        "INFO"
    )

    transaction_id = 1

    while True:

        print("\n========== MENU ==========")
        print("1 - Add income")
        print("2 - Add expense")
        print("3 - Create goal")
        print("4 - View statistics")
        print("5 - Send notification")
        print("0 - Exit")
        print("==========================")

        choice = input("Choose: ")

        if choice == "1":

            amount = int(input("Income amount: "))
            category = input("Category: ")

            t = Transaction(
                transaction_id,
                1,
                amount,
                category,
                "INCOME"
            )

            system.add_transaction(t)

            user.add_income(amount)

            system.smart_notification(user)

            transaction_id += 1

        elif choice == "2":

            amount = int(input("Expense amount: "))
            category = input("Category: ")

            t = Transaction(
                transaction_id,
                1,
                amount,
                category,
                "EXPENSE"
            )

            system.add_transaction(t)

            user.add_expense(amount)

            system.smart_notification(user)

            transaction_id += 1

        elif choice == "3":

            goal_name = input("Goal name: ")
            target_amount = int(input("Target amount: "))
            saved = int(input("Saved amount: "))

            goal = Goal(
                1,
                1,
                goal_name,
                target_amount
            )

            system.create_goal(goal)

            goal.update_progress(saved)

            print("Remaining:", goal.calculate_remaining())

        elif choice == "4":

            stats = system.generate_statistics()

            stats.show_statistics()

        elif choice == "5":

            message = input("Enter notification message: ")

            system.send_notification(
                message,
                "INFO"
            )

        elif choice == "0":

            print("\nProgram finished.")

            break

        else:

            print("Wrong choice! Try again.")

else:

    print("\nWrong email or password!")