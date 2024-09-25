team1_num = 5
team2_num = 6

print('В команде Мастера кода участников: %d!' % team1_num)
print('В команде Волшебники данных участников: %d!' % team2_num)
print("Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num))

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print("Команда Мастера кода решила задач: {}!".format(score_1))
print("Мастера кода решили задачи за {}с!".format(team1_time))
print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {}с!".format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'Кто-то должен победить!'
tasks_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = round(time_total / tasks_total, 1)

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')