# Program to calculate due amount

bill_amount = float(input("Enter the total bill amount: "))
paid_amount = float(input("Enter the amount paid by the customer: "))

due_amount = bill_amount - paid_amount

print("Customer's due amount is:", due_amount)