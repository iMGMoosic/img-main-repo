def estimate_pi(sample_size):
    import random
    import math
    inside_circle = 0
    outside_circle = 0
    for i in range(0,sample_size):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
        else:
            outside_circle += 1
    pi_estimate = (inside_circle / sample_size) * 4
    print("The value of pi is equal to", pi_estimate)
    pi_difference = math.pi - pi_estimate
    print("This value of pi is off by", pi_difference)

flag = "y"
while flag == "y":
    sample_size = int(input("Please enter a sample size: "))
    estimate_pi(int(sample_size))
    flag = ""
    
    answer = input("Would you like to try again? (y/n) ")
    if answer == "y" or answer == "Y":
        flag = "y"
    elif answer == "n" or answer == "N":
        flag = "n"
    else:
        print("That is not a valid input. Please try again.")
