def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    balance = withdraw(balance, amount)

except ValueError as e:
    print("Error:", e)

else:
    print("Withdrawal successful")
    print("Remaining balance:", balance)

finally:
    print("Transaction completed")