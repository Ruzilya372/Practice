class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        return None

    def __str__(self):
        return "Вода"

class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        return None
    
    def __str__(self):
        return "Воздух"


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        return None

    def __str__(self):
        return "Огонь"


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None

    def __str__(self):
        return "Земля"



class Ice:
    def __add__(self, other):
        if isinstance(other, Water):
            return Water()
        elif isinstance(other, Air):
            return Snow()
        elif isinstance(other, Fire):
            return Water()
        return None

    def __str__(self):
        return "Лед"




class Storm:
    def __add__(self, other):
        return None

    def __str__(self):
        return "Шторм"


class Steam:
    def __add__(self, other):
        return None

    def __str__(self):
        return "Пар"


class Mud:
    def __add__(self, other):
        return None

    def __str__(self):
        return "Грязь"


class Lightning:
    def __add__(self, other):
        return None

    def __str__(self):
        return "Молния"


class Dust:
    def __add__(self, other):
        return None

    def __str__(self):
        return "Пыль"


class Lava:
    def __add__(self, other):
        return None

    def __str__(self):
        return "Лава"


class Snow:
    def __add__(self, other):
        return None

    def __str__(self):
        return "Снег"


def combine_elements(first_element, second_element):
    result = first_element + second_element
    if result:
        print(f"{first_element} + {second_element} = {result}")
        return result
    else:
        print(f"{first_element} + {second_element} = неизвестная комбинация.")
        return None


water = Water()
fire = Fire()
air = Air()
earth = Earth()
ice = Ice()

print("Таблица преобразований")
combine_elements(water, air)
combine_elements(water, fire)
combine_elements(water, earth)
combine_elements(air, fire)
combine_elements(air, earth)
combine_elements(fire, earth)

print("\nПреобразования неизвестных комбинаций")
combine_elements(water, water)
combine_elements(air, air)
combine_elements(fire, fire)
combine_elements(earth, earth)

print("\nКомбинация с новым элементом 'Лед'")
combine_elements(ice, fire)
combine_elements(ice, water)
combine_elements(ice, air)
combine_elements(ice, earth)
combine_elements(ice, ice)
