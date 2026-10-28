# Installment 5: The Menu Comes Alive

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

# Setup asked once at the start
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!\n")

# Variables to track progress
subtotal = 0.0
count = 0

while True:
    print("MAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal = subtotal + amount
        count = count + 1

        if amount > 200:
            print("  Huge expense, are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget

        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}")

        if over_budget:
            over_amount = total - budget
            print(f"Over budget by ${over_amount}!")
        elif total > (budget * 0.90):
            left = budget - total
            print(f"Careful: only ${left} left.")
        else:
            left = budget - total
            print(f"Within budget. ${left} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("Made by: Nemenz-Drew D. Tolentino | Installment 5")
        break

    else:
        print("Please choose 1, 2, 3 or 4.")