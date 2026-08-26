def tpl_sort(tpl_catalog):
    for element in tpl_catalog:
        if type(element) != int:
            return tpl_catalog
        
    return tuple(sorted(tpl_catalog))


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))
