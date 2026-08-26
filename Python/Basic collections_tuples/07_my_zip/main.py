text = "abcd"
numbers = tuple([10,20,30,40])
result = zip(text, numbers)

print(result)

for pair in result:
    print(pair)