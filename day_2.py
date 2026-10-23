print("Welcome to the tip calculator!")
total_bill = int(input("what was the total bill? $ \n"))
tip = int(input("How much tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))
tip_amount = total_bill * (tip / 100)
per_person = (total_bill + tip_amount) /people
print(f"Each person should pay: ${per_person:.2f}")