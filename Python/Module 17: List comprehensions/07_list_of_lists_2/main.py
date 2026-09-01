nice_catalog = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_catalog = [number for subcatalog1 in nice_catalog for subcatalog2 in subcatalog1 for number in subcatalog2]
print(new_catalog)