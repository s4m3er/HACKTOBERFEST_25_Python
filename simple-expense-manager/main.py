import csv
from datetime import datetime
import os

FILENAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., Food, Travel, Shopping): ").capitalize()
    description = input("Enter description: ")
    amount = input("Enter amount (₹): ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print(f"✅ Expense of ₹{amount} added successfully!\n")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("⚠️ No expense file found. Add some expenses first.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("\n📊 All Expenses:\n")
        print(f"{'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>8}")
        print("-" * 60)
        total = 0
        for row in reader:
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<20} ₹{row[3]:>6}")
            total += float(row[3])
        print("-" * 60)
        print(f"Total Spent: ₹{total:.2f}\n")

def summary_by_category():
    if not os.path.exists(FILENAME):
        print("⚠️ No expense file found. Add some expenses first.")
        return

    category_totals = {}
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            category_totals[category] = category_totals.get(category, 0) + amount

    print("\n📈 Category-wise Summary:\n")
    for cat, total in category_totals.items():
        print(f"{cat:<15}: ₹{total:.2f}")
    print()

def main():
    init_file()
    while True:
        print("====== Simple Expense Manager ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
