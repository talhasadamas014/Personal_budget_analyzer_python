import pandas as pd
import matplotlib.pyplot as plt

budget_data = {}

while True:

    print("\n===== Personal Budget Analyzer =====")
    print("1. Add Monthly Budget")
    print("2. View Data")
    print("3. Visualize Data")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        month = input("Enter Month (i.e. January,February...): ").title()
        income = float(input("Enter Income: "))
        expenses = {}

        expenses["Food"] = float(input("Food Expense: "))
        expenses["Transport"] = float(input("Transport Expense: "))
        expenses["Education"] = float(input("Education Expense: "))
        expenses["Entertainment"] = float(input("Entertainment Expense: "))
        expenses["Other"] = float(input("Other Expense: "))

        total_expense = sum(expenses.values())
        savings = income - total_expense

        budget_data[month] = {
            "Income": income,
            "Expenses": expenses,
            "Total Expense": total_expense,
            "Savings": savings
        }

        row = {
            "Month": month,
            "Income": income,
            "Food": expenses["Food"],
            "Transport": expenses["Transport"],
            "Education": expenses["Education"],
            "Entertainment": expenses["Entertainment"],
            "Other": expenses["Other"],
            "Total Expense": total_expense,
            "Savings": savings
        }

        df = pd.DataFrame([row])

        df.to_csv(
            "personal_budget.csv",
            mode="a",
            header=False,
            index=False
        )

        print("\nBudget Saved Successfully!")

    elif choice == "2":

        try:
            df = pd.read_csv("personal_budget.csv")
            print(df)

        except:
            print("No Data Found!")

    elif choice == "3":

        try:
            df = pd.read_csv(
                "personal_budget.csv"
            )

            print("\nChoose Visualization")
            print("1. Monthly Savings")
            print("2. Income vs Expenses")
            print("3. Expense Categories")

            chart_choice = input("Enter Choice: ")

            if chart_choice == "1":

                plt.figure(figsize=(8,5))
                plt.bar(df["Month"], df["Savings"])

                plt.title("Monthly Savings")
                plt.xlabel("Month")
                plt.ylabel("Savings")
                plt.savefig("monthly_savings.png")
                plt.show()

            elif chart_choice == "2":

                plt.figure(figsize=(8,5))
                plt.plot(
                    df["Month"],
                    df["Income"],
                    marker="o",
                    label="Income"
                )
                plt.plot(
                    df["Month"],
                    df["Total Expense"],
                    marker="o",
                    label="Expense"
                )

                plt.title("Income vs Expense")
                plt.xlabel("Month")
                plt.ylabel("Amount")
                plt.legend()
                plt.savefig("income_vs_expense.png")
                plt.show()

            elif chart_choice == "3":

                total_food = df["Food"].sum()
                total_transport = df["Transport"].sum()
                total_education = df["Education"].sum()
                total_entertainment = df["Entertainment"].sum()
                total_other = df["Other"].sum()

                categories = [
                    "Food",
                    "Transport",
                    "Education",
                    "Entertainment",
                    "Other"
                ]

                values = [
                    total_food,
                    total_transport,
                    total_education,
                    total_entertainment,
                    total_other
                ]

                plt.figure(figsize=(7,7))

                plt.pie(
                    values,
                    labels=categories,
                    autopct="%1.1f%%"
                )

                plt.title("Expense Category Breakdown")
                plt.savefig("expense_categories.png")
                plt.show()

            else:
                print("Invalid Visualization Choice")

        except:
            print("No Data Available For Visualization!")

    elif choice == "4":

        print("Program Closed.")
        break

    else:
        print("Invalid Choice")