loan_amount = float(input("Please input the amount of your loan: $"))
interest = float(input("Please input your interest rate: "))
interest /= 100
loan_duration = int(input("Please input your loan duration in months: "))

monthly_interest = interest / 12
payment = (monthly_interest * loan_amount) / (1 - ((1 + monthly_interest) ** -loan_duration))

print("To pay off your loan in " + str(loan_duration) + " months, you'll need to pay $" + str(round(payment, 2)) + " per month.")
