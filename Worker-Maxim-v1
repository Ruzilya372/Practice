print("Начался восьмичасовой рабочий день.")
hour = 0
wife_call_count = 0
tasks_count = 0

while hour != 8:
  hour += 1
  print(hour,"-й час")
  tasks = int(input("Сколько задач решит Максим? "))
  tasks_count += tasks
  if wife_call_count != 1:
    wife_call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    if wife_call == 1:
      wife_call_count = 1
      tasks_count += 1

print("Рабочий день закончился. Всего выполнено задач: ", tasks_count)
if wife_call_count > 0:
  print("Нужно зайти в магазин.")
