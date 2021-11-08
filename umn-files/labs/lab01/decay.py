# Hey, look, it's a comment on line 1 or something!

init = eval(input("Initial Amount: "))
halflife = eval(input("Half-life: "))
time = eval(input("Elapsed-time: "))
residual = init*.5**(time/halflife)
print("Residual amount remaining = ",residual)
