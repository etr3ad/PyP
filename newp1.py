# 👷 Simple Bonus Calculator for Employees

# Get the employee's name
name = input("Employee’s name: ")

# Get number of shifts worked
shifts = int(input("Number of Shifts: "))

# Get number of transactions
transactions = int(input("Number of transactions: "))

# Get total transaction value
value = float(input("Transaction dollar value: "))

# Calculate productivity score
score = (value / transactions) / shifts

# Decide bonus using nested if
if score <= 30:
    bonus = 50.00
else:
    if score <= 69:
        bonus = 75.00
    else:
        if score <= 199:
            bonus = 100.00
        else:
            bonus = 200.00

# Output results
print("\nEmployee Name:", name)
print("Employee Bonus: $" + str(bonus))
