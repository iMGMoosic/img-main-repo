integer = int(input("Enter a four digit integer: "))

digit_1 = integer // 1000 % 10
digit_2 = integer // 100 % 10
digit_3 = integer // 10 % 10
digit_4 = integer % 10

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)
