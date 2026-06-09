count_tasks = 0
count_calls = 0
calls = 0

print("Начался восьмичасовой рабочий день.")
for hour in range(1,9):
  print(hour, "-й час")
  tasks = int(input("Сколько  задач решил Максим?"))
  count_tasks += tasks
  if calls == 0:
    calls = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет):"))
    if calls == 1:
      count_calls = 1
print("Рабочий день закончился. Всего выполнено задач:", count_tasks)
if count_calls == 1:
  print("Нужно зайти в магазин.")
