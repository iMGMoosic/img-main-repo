def roundFloat(float_num):
    if float_num > 0:
        float_num += 0.5
    elif float_num < 0:
        float_num -= 0.5
    else:
        float_num == 0
    return int(float_num)

def main():
    num = float(input("Please enter a floating-point number: "))
    num = roundFloat(num)
    print("The rounded integer is", num)
    return

