def add_two_numbers() -> int:
    user_input = input()
    string_list = user_input.split(",")
    
    a = int(string_list[0])
    b = int(string_list[1])
    
    return a + b



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
