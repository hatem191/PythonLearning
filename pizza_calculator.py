print("Welcome to the Pizza Calculator!")

cost_of_pizza = 0
pizza_size = input("What is the size of the pizza S, M, L ? ")
if pizza_size == "S":
    cost_of_pizza = 15
elif pizza_size == "M":
    cost_of_pizza = 20
elif pizza_size == "L":
    cost_of_pizza = 25

if pizza_size in ("S", "M", "L"):
    has_pepperoni = input("Do you want pepperoni slices Y or N ? ")
    if has_pepperoni == "Y":
        cost_of_pizza += 2
        if pizza_size in ("M", "L"):
            cost_of_pizza += 1
        has_extra_cheese = input("Do you want extra cheese on your slices Y or N ? ")
        if has_extra_cheese == "Y":
            cost_of_pizza += 1

print(f"Your pizza size is {pizza_size} and the total cost is ${cost_of_pizza}")


