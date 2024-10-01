import random

rest_list = ["Bob", "Tom", "Julie", "Samantha"]

random_person_selection = random.randint(0,3)
start = input("Type start to begin the program: ")
if start == "start":
    print("The one who will pay the bill today is " + rest_list[random_person_selection])
else:
    print("The program ended as you did not type start. Have a good day!")