# Installment 4: The Tracker Makes Decisions

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("[1] Add an expense\t(coming soon)")
print("[2] View all expenses\t(coming soon)")
print("[3] Show total spent\t(coming soon)")
print("[4] Exit\t\t(coming soon)")
print("-" * 40)

# Greet the user
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

# Start subtotal at 0
subtotal = 0.0

# First expense
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

# Size message for first expense
if amount1 > 200:
    print("  Huge expense, are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Second expense
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

# Size message for second expense
if amount2 > 200:
    print("  Huge expense, are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Two big expenses in a row warning
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row, slow down!")

# Calculate average
average = subtotal / 2

# Ask for tax rate and budget
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

# Compute tax and grand total
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

# Calculate over_budget
over_budget = total > budget

# Print summary
print("\n" + "-" * 40)
print("SUMMARY")
print("-" * 40)
print(f"{item1}:\t\t${amount1}")
print(f"{item2}:\t\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

# Verdict line
if over_budget:
    over_amount = total - budget
    print(f"Over budget by ${over_amount}!")
elif total > (budget * 0.90):
    left = budget - total
    print(f"Careful: only ${left} left.")
else:
    left = budget - total
    print(f"Within budget. ${left} left.")

print("-" * 40)

# Footer
print("Made by: Nemenz-Drew D. Tolentino | Installment 4")