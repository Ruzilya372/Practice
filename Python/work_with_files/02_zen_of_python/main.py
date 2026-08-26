import os


file_zen = open((os.path.join("Module22", "02_zen_of_python", 'zen.txt')), 'r', encoding = 'utf-8')

zen_catalog = []
for line in file_zen:
    zen_catalog.append(line)

file_zen.close()

reverse_zen_catalog = zen_catalog[::-1]
for reverse_line in reverse_zen_catalog:
    print(reverse_line, end = '')
