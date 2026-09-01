def find_last_person(number_people, number_rhyme):
    people = list(range(1, number_people + 1))

    current_index = 0

    print("\nТекущий круг людей:", people)
    print("Начало счета с номера", people[current_index])

    while len(people) > 1:
        remove_index = (current_index + number_rhyme - 1) % len(people)
        print("Выбывает человек под номером", people[remove_index])
        people.pop(remove_index)

        if people:
            current_index = remove_index % len(people)
            print("Текущий круг людей:", people)
            print("Начало счета с номера", people[current_index])
        else:
            current_index = 0

    return people [0]


how_much_people = int(input("Кол-во человек: "))
rhyme = int(input("Какое число в считалке: "))

print("Значит, выбывает каждый "+ str(rhyme ) + "-й человек")

last_person = find_last_person(how_much_people, rhyme)

if last_person is not None:
    print("Остался человек под номером", last_person)