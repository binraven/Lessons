#Задание "Слишком древний шифр"

import random
from time import sleep

pwd = [[]]
pwd_i = 0
st = 1
nd = 2
def randomize():
    ran_number = random.randrange(3,21)
    return ran_number

ran_number = randomize()

while st + nd <= ran_number:
    if ran_number % (st+nd) == 0:
        if st == nd:
            nd +=1
        else:
            pwd[pwd_i].extend([st,nd])
            nd += 1
    else:
        nd += 1
    if st + nd > ran_number:
        nd = st + 1
        st += 1

un_pwd = pwd[0]
print (f'Рандомное число: {ran_number}')
print ('Наш пароль: ', *un_pwd)

sleep(1)
print(f'Побег суцефуле!!! :)')


