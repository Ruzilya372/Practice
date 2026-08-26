violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

how_much = int(input("Сколько песен выбрать? "))
count_time = 0
found_songs = 0

for song_number in range(1, how_much + 1):
    name_song = input(f"Название {song_number}-й песни: ")
    song_found = False
    
    for song in violator_songs:
        if song[0] == name_song:
            count_time += song[1]
            found_songs += 1
            song_found = True
            break
    
    if not song_found:
        print("Песни", name_song, "нет в списке.")

if found_songs > 0:
    print("Общее время звучания песен:", count_time)
else:
    print("Не найдено ни одной песни из списка")