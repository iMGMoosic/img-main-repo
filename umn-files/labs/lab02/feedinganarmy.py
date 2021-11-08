brussels_sprouts = 2
apple = 1
pancetta = 4
olive_oil = 2
rosemary = 1
chicken = 6

people = int(input("How many people do you need to feed? "))

brussels_sprouts *= people
apple *= people
pancetta *= people
olive_oil *= people
rosemary *= people
chicken *= people

print("To cook this recipe for", people, "people, you'll need:")
print(brussels_sprouts, "cups of Brussels sprouts, halved")
print(apple, "red apple, cut into 1-inch cubes")
print(pancetta, "oz of pancetta")
print(olive_oil, "tablespoons of olive oil, divided")
print(rosemary, "teaspoons of minced fresh rosemary")
print(chicken, "skinless, boneless chicken thighs")
print("Salt and ground black pepper to taste")

print("Enjoy!")
