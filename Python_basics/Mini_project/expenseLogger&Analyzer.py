import os
from datetime import datetime

FILE_NAME = "expenses.txt"

def add_expense(category, amount, **kwargs):
    date = kwargs.get('date',datetime.now().strftime('%Y-%m-%d'))
    entry = f"{date},{category},{amount}\n"
    with open(FILE_NAME, 'a' ) as file:
        file.write(entry)
    print(f"Added:{category} - ${amount} on {date}")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
        for _ in lines:
            print(_.strip())

def filter_expenses(category):
    with open(FILE_NAME, 'r') as file:
        filtered = [line.strip() for line in file if line.split(',')[1].strip().lower() == category.lower()]
    print(f"\nFiltered expenses for category '{category}':")
    for line in filtered:
        print(line)

def expense_stats():
    if not os.path.exists(FILE_NAME):
        print("No data availabe")
        return
    
    def parse():
        with open(FILE_NAME, 'r') as file:
            return [float(line.split(',')[2]) for line in file]
        
    def stats(amounts):
        total = sum(amounts)
        if amounts:
            average = total / len(amounts)
        else:
            average = 0
        return total, average
    
    amounts = parse()
    total, avg = stats(amounts)
    print(f"\nTotal Expenses: ${total:.2f} | Average: ${avg:.2f}")

def remove_expense(date, category):
    if not os.path.exists(FILE_NAME):
        print("File not found")
        return
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

    updated = [line for line in lines if not (line.startswith(date) and category in line)]
    with open (FILE_NAME, 'w') as file:
        file.writelines(updated)

    print(f"Removed entries with date: {date} and category: {category}")

def list_categories():
    with open(FILE_NAME, 'r') as file:
        categories = set(line.split(',')[1].strip().lower() for line in file)
    print("\nCategories Used:", categories)

def main():
    while True:
        print("""
-------- Expense Tracker Menu --------
1. Add Expense
2. View All
3. Filter by Category
4. Show Stats
5. Remove Entry
6. Show Categories
7. Exit
        """)
        choice = input("Choose option: ")

        if choice == '1':
            cat = input("Enter category: ")
            amt = float(input("Enter amount ($): "))
            add_expense(cat, amt)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            cat = input("Enter category to filter: ")
            filter_expenses(cat)
        elif choice == '4':
            expense_stats()
        elif choice == '5':
            dt = input("Enter date (YYYY-MM-DD): ")
            cat = input("Enter category: ")
            remove_expense(dt, cat)
        elif choice == '6':
            list_categories()
        elif choice == '7':
            print("Exiting Expense Logger.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()