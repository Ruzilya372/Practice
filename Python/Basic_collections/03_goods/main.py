goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product_name in goods:
    product_code = goods[product_name]
    orders = store[product_code]

    total_quantity = 0
    total_cost = 0

    for order in orders:
        quantity = order['quantity']
        price = order['price']
        total_quantity += quantity
        total_cost += quantity * price

    print(f"{product_name} - {total_quantity} штук, стоимость {total_cost} рублей")