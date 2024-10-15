def calculate_love_score():
    name1 = "Angela Yuu"
    name2 = "Jack Bauer"
    lowercase_name1 = name1.lower()
    lowercase_name2 = name2.lower()
    name_string_01 = list(lowercase_name1)
    name_string_02 = list(lowercase_name2)
    number_of_elements_01 = len(name_string_01)
    number_of_elements_02 = len(name_string_02)
    number_of_letters_t = 0
    number_of_letters_r = 0
    number_of_letters_u = 0
    number_of_letters_e = 0
    number_of_letters_l = 0
    number_of_letters_o = 0
    number_of_letters_v = 0


    for x in range(number_of_elements_01):
        if name_string_01[x] == 't':
            number_of_letters_t += 1
        elif name_string_01[x] == 'r':
            number_of_letters_r += 1
        elif name_string_01[x] == 'u':
            number_of_letters_u += 1
        elif name_string_01[x] == 'e':
            number_of_letters_e += 1

    # Reset number of letters for e as we are re-using it
    number_of_letters_e = 0
    for y in range(number_of_elements_02):
        if name_string_02[y] == 'l':
            number_of_letters_l += 1
        elif name_string_02[y] == 'o':
            number_of_letters_o += 1
        elif name_string_02[y] == 'v':
            number_of_letters_v += 1
        elif name_string_02[y] == 'e':
            number_of_letters_e += 1

    print("=========== First Name ===============" + '\n')
    print(f"T occurs {number_of_letters_t} times")
    print(f"R occurs {number_of_letters_r} times")
    print(f"U occurs {number_of_letters_u} times")
    print(f"E occurs {number_of_letters_e} times" + '\n')

    print("=========== Second Name ===============" + '\n')
    print(f"L occurs {number_of_letters_l} times")
    print(f"O occurs {number_of_letters_o} times")
    print(f"V occurs {number_of_letters_v} times")
    print(f"E occurs {number_of_letters_e} times" + '\n')

calculate_love_score()