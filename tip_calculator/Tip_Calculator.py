print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? ₹"))
split = int(input("How many ppl to split the bill?"))
percentage = int(input("What percentage tip would you like to give?"))
tip = percentage / 100 * bill + bill
Split_Amount = round((tip/split),2)
Split_Amount = '{0:.2f}'.format(Split_Amount)
print(f"Each person should pay: ₹{Split_Amount}")
