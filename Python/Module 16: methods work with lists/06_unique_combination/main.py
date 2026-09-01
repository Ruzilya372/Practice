def get_merge_sorted_lists(first, second):
    merged = first+second
    merged.sort()
    result = []
    for item in merged:
        if not result or result[-1] != item:
            result.append(item)
    
    return result

# Пример использования:
catalog1 = [1, 3, 5, 7, 9]
catalog2 = [2, 4, 5, 6, 8, 10]
merged = get_merge_sorted_lists(catalog1, catalog2)
print(merged)