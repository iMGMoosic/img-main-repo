weight = float(input("Please enter your weight in pounds: "))
height = float(input("Please enter your height in inches: "))
age = int(input("Please enter your age in years: "))
gender = str(input("Are you male or female [M/F]?: "))

if gender == "M":
    bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    chocolate_bars = bmr / 230
    print("To maintain your weight, you'd need to eat", chocolate_bars, "chocolate bars.")
else:
    bmr = 65.5 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    chocolate_bars = bmr / 230
    print("To maintain your weight, you'd need to eat", chocolate_bars, "chocolate bars.")
