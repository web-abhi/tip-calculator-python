print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage would you like to give? 10, 12, or 15?")
split = input("How many people to split the bill?")
total = (float(bill)/100*float(tip))
bill_total = ((float(total)+float(bill))/float(split))
total_per_person = (round(bill_total, 2))
pay = ("Each person should pay: $"+str(total_per_person))
print(pay)
