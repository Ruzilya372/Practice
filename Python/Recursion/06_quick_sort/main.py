def split_by_pivot(hoar_numbers):
    pivot = hoar_numbers[-1]
    less = []
    equal = []
    greater = []
    
    for element in hoar_numbers:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    
    return less, equal, greater


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    less, equal, greater = split_by_pivot(numbers)
    return quicksort(less) + equal + quicksort(greater)


import_numbers = [4, 9, 2, 7, 5]
print(quicksort(import_numbers))