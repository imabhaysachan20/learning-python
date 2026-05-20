
balance = 10000

transactions = [
    ("deposit", 2000),
    ("withdraw", 500),
    ("withdraw", 12000),
    ("deposit", 1500),
    ("withdraw", 3000),
]

# ------------------ TRACKERS ------------------

successful_withdrawals = []
failed_withdrawals = []

deposit_count = 0
withdraw_count = 0
failed_count = 0

highest_balance = balance
consecutive_failed = 0

# ------------------ PROCESS ------------------

for t in transactions:
    action = t[0]
    amount = t[1]

    if action == "deposit":
        balance = balance + amount
        deposit_count = deposit_count + 1
        consecutive_failed = 0   # reset

    elif action == "withdraw":
        withdraw_count = withdraw_count + 1

        if amount <= balance:
            balance = balance - amount
            successful_withdrawals.append(amount)
            consecutive_failed = 0   # reset
        else:
            print("Insufficient balance for:", amount)
            failed_withdrawals.append(amount)
            failed_count = failed_count + 1
            consecutive_failed = consecutive_failed + 1

            # Fraud rule
            if consecutive_failed == 3:
                print("Account temporarily blocked")
                break

    # Track highest balance
    if balance > highest_balance:
        highest_balance = balance

# ------------------ OUTPUT ------------------

print("\nFinal Balance:", balance)
print("Highest Balance:", highest_balance)
print("Deposits:", deposit_count)
print("Withdrawals:", withdraw_count)
print("Failed Withdrawals:", failed_count)
print("Successful Withdrawals List:", successful_withdrawals)
print("Failed Withdrawals List:", failed_withdrawals)