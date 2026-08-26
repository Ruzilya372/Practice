total_orders = int(input("Введите количество заказов: "))

order_dictionary = dict()

for order_number in range(1, total_orders + 1):
    order = input(f"{order_number} заказ:")
    order_catalog = order.split(" ")

    customer = order_catalog[0]
    pizza = order_catalog[1]
    quantity = int(order_catalog[2])

    if customer in order_dictionary:
        if pizza in order_dictionary[customer]:
            order_dictionary[customer][pizza] += quantity
        else:
            order_dictionary[customer][pizza] = quantity 
    else:
        order_dictionary[customer] = {pizza: quantity}

print()

for customer in sorted(order_dictionary.keys()):
    print(customer)

    for pizza in sorted(order_dictionary[customer].keys()):
        quantity = order_dictionary[customer][pizza]
        print(f"{pizza}: {quantity}")
