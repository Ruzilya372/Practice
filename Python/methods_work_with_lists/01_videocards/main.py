video_cards = []
how_much_video = int(input("Количество видеокарт: "))
for video_card in range(how_much_video):
    num_video_card = int(input("Видеокарта: "))
    video_cards.append(num_video_card)

print("Старый список видеокарт:", video_cards)


max_element = max(video_cards)

new_video_cards = []
for card in video_cards:
    if card != max_element:
        new_video_cards.append(card)

print("Новый список видеокарт", new_video_cards)
