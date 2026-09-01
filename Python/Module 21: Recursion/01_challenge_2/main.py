def print_number(current_element, final_element):
    if current_element > final_element:
        return

    print(current_element)
    
    print_number(current_element + 1, final_element)


number = int(input("Введите number: "))
print_number(1, number)