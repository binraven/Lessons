"""
"Форматирование строк".
Цель задания:

Освоить различные методы форматирования строк в Python.
Научиться применять эти методы в контексте описания соревнования. История: соперничество двух команд - Мастера кода и Волшебники данных.

"""
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'


print("\nИспользование %:")
print("В команде Мастера кода участников: %d ! " % team1_num )
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

print("\nИспользование format():")
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {team1_time}".format(team1_time=team1_time))

print("\nИспользование f-строк:")
print(f'Команды решили {score_1} и {score_2} задач.')
print(f"Результат битвы: победа команды {challenge_result}")
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем по"
      f" {round(team1_time + team2_time / score_1 + score_2, 1)} секунды на задачу!.")





