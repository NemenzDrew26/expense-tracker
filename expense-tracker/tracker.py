# Installment 3: The Tracker Does Math

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

# Second expense
item2 = input("First expense? ") if False else input("Second expense? ") # maintaining prompt
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

# Calculate average
average = subtotal / 2

# Ask for tax rate and budget
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

# Compute tax, grand total, over_budget, and left in budget
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

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
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

# Footer
print("Made by: Nemenz-Drew D. Tolentino | Installment 3")