celsius = 100
fahrenheit = 0

while celsius != fahrenheit:
    fahrenheit = int(celsius * (9/5) + 32)
    celsius -= 1

print("The value at which Celsius & Fahrenheit temperatures values are the same is " + str(celsius) + "º.")
