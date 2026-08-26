shop = [
        ['каретка', 1200],
        ['шатун', 1000],
        ['седло', 300],
        ['педаль', 100],
        ['седло', 1500],
        ['рама', 12000],
        ['обод', 2000],
        ['шатун', 200],
        ['седло', 2700]
]

name_detail = input("Название детали: ")
how_much_details = int(input("Кол-во деталей: "))
for detail, price in shop:
    if name_detail == detail:
        final_price = price * how_much_details
        
print("Общая стоимость:", final_price)


