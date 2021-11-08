# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 1

half_dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

cents = int(input("Please enter the number of cents: "))

# throughout block, code checks if cents is greater than the value of the coin
# then uses floor division to find the amount of said coin, then replaces cents
# with the remainder of the coin it just checked for times its value
if cents >= 50:
    half_dollars = cents // 50
    cents %= (half_dollars * 50)
if cents >= 25:
    quarters = cents // 25
    cents %= (quarters * 25)
if cents >= 10:
    dimes = cents // 10
    cents %= (dimes * 10)
if cents >= 5:
    nickels = cents // 5
    cents %= (nickels * 5)
if cents <= 4:
    pennies = cents

print(half_dollars, "half dollars")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
print(pennies, "pennies")
