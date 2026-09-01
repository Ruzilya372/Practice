import os

first_file = open(os.path.join('Module22', '04_tournament', 'first_tour.txt'), 'r', encoding = 'utf-8')
first_content = first_file.read()
first_file.close()

print("Содержимое файла first_tour.txt")
print(first_content)

first_file = open(os.path.join('Module22', '04_tournament', 'first_tour.txt'), 'r', encoding = 'utf-8')

first_line = True
passed_players = []

for line in first_file:
    if first_line:
        minimal_score = int(line.strip())
        first_line = False
    else:
        if line.strip():
            surname, name, score = line.split()
            score = int(score)

            if score > minimal_score:
                passed_players.append((surname, name, score))

first_file.close()
print("")

second_file = open(os.path.join('Module22', '04_tournament', 'second_tour.txt'), 'w', encoding = 'utf-8')

second_file.write(str(len(passed_players)) + '\n')

for index, player in enumerate(passed_players, 1):
    surname, name, score = player
    initsyal = name[0]
    second_file.write(f"{index}) {initsyal}. {surname} {score}\n")

second_file.close()


second_file = open(os.path.join('Module22', '04_tournament', 'second_tour.txt'), 'r', encoding = 'utf-8')
print("Содержимое файла second_tour.txt:")
print(second_file.read())


