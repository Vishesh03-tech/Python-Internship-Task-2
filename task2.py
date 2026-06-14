import csv
import os
def add_expense (desc, amount):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])
        print(f"Added: {desc}-{amount}")
def view_expenses():
    if not os.path.exists("expenses.csv"):
        print("No record Yet!")
        return
    
    print("\n----All Expenses----\n")
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if row:
                print(f"Item: {row[0]} | Amount: {row[1]}")
def total_expenses():
    if not os.path.exists("expenses.csv"):
        print("Total Expense: Rs. 0.00")
        return
    total = 0.00
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if row:
                try:
                    total += float(row[1])
                except ValueError:
                    continue    
    print(f"Total Expenses: Rs.{total:.2f}")

def main():
    while True:
        print("\n----Expense Tracker Menu----")
        print("1. Add Expense")
        print("2. View all expense")
        print("3. View Total expense")
        print("4. Exit")

        choice = input("Choose an option(1-4): ").strip()
        if choice == "1":
            desc = input("Enter expense Description: ").strip()
            try:
                amount = float(input("Enter Amount: "))
                add_expense(desc,amount)
            except  ValueError:
                print("Invalid Amount! Please enter valid number: ")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("GoodBye!  Stay on Budget :)")       

            break


if __name__ == "__main__":
    main()
