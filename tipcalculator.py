print("Welcome to the tip calculator! ")
total_bill = float(input("What was the total bill? "))
tip_amount = float(input("How much would you like to give 10%,12%, or 15% ? "))
tip_amount = (tip_amount / 100) * total_bill
number_of_payers = int(input("How many people to split the bill? "))
print("Calculating how much each person should pay: ")
total_amount = float(tip_amount + total_bill)
amount_each_person = round(total_amount / number_of_payers, 2)
print("Each person should pay: " + str(amount_each_person))
