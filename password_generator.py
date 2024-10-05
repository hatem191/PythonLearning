import random

symbols = ['`','!','@','#','$','%','^','&','*','(',')','-']
numbers = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

password_generated =""
b = 0
c = 0
password_list=[]

number_of_characters=int(input("Enter the number of characters that you want in your password: "))
number_of_symbols=int(input("How many symbols would you like in your password: "))
number_of_numbers=int(input("How many numbers would you like in your password: "))

for a in range(1,number_of_characters+1):
    if b < number_of_symbols:
        b+=1
        password_list.append(random.choice(symbols))
    elif c < number_of_numbers:
        c+=1
        password_list.append(random.choice(numbers))
    else:
        password_list.append(random.choice(alphabet))

# This will shuffle the password
random.shuffle(password_list)

#complete this step
password_generated = ''.join(password_list)

print("The password that was generated is " + password_generated)




