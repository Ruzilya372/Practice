films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

my_favorite = []
add_films = int(input("Сколько фильмов хотите добавить? "))
for film in range(add_films):
    film_name = input("Введите название фильма: ")
    if film_name in films:
        my_favorite.append(film_name)
    else:
        print("Фильма", film_name, "у нас нет :( )")
print("Ваш список любимыех фильмов:", my_favorite)

