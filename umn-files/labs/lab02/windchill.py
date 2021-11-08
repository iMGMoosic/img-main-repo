temp = float(input("Please enter the temperature in Fahrenheit: "))

if temp <= 41.0 and temp >= -58.0:
    wind_speed = float(input("Please enter the wind velocity in mph: "))
    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp * (wind_speed ** 0.16))
    print("The wind chill is", wind_chill, "ºF")
else:
    print("That isn't a valid temperature! Temperature must be between -58ºF and 41ºF.")
