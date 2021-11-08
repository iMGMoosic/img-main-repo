valid_units = {'pounds', 'ounces', 'miles', 'inches', 'kilos', 'grams', 'kilometers', 'centimeters'}
value = float(input("Please input a value: "))
unit = input("Please input a unit: ")

if unit not in valid_units:
    print(unit, "is not a valid unit.")
else:
    if unit == "pounds":
        value *= 0.453592
        print("%.4f" % value, "kilos")
    elif unit == "kilos":
        value /= 0.453592
        print("%.4f" % value, "pounds")
    elif unit == "ounces":
        value *= 28.3495
        print("%.4f" % value, "grams")
    elif unit == "grams":
        value /= 28.3495
        print("%.4f" % value, "ounces")
    elif unit == "miles":
        value *= 1.60934
        print("%.4f" % value, "kilometers")
    elif unit == "kilometers":
        value /= 1.60934
        print("%.4f" % value, "miles")
    elif unit == "inches":
        value *= 2.54
        print("%.4f" % value, "centimeters")
    else:
        value /= 2.54
        print("%.4f" % value, "inches")
