#IMPORT
import os; os.system('cls')
import random

#HEADER
print('HIGHER LOWER')
print('------------')

#HÄMTA INFORMATION
correct = random.randint(0, 101)
answer = -1
answers = 0

#ÄR SVARET HÖGRE ELLER LÄGRE
while answer != correct:
    try:
        answer = int(input('>'))
    except ValueError:
        print('MUST BE A NUMBER!')
        continue
    answers += 1
    if answer < correct:
        print('HIGHER!')
    elif answer > correct:
        print('LOWER!')
        
#RESULTAT
print(correct, 'WAS CORRECT!')
print('it took you', answers , 'tries!')