# Write your code here
from random import choice
ratings = 0

n = input('Enter your name: ')
print('Hello, ' + n)
file = open('rating.txt', 'r')
rek = file.read()
re = rek.split()
re_dct = {re[i]: re[i + 1] for i in range(0, len(re), 2)}
if n in re_dct:
    ratings = int(re_dct[n])

input_2 = input().split(',')
if len(input_2) == 1:
    input_2 = ['rock', 'paper', 'scissors']

print("Okay, let's start")
input_1 = ''

while True:
    option = choice(input_2)
    input_1 = input()
    if input_1 == '!exit' or input_1 == 'Bye!':
        break

    if input_1 not in input_2 and input_1 != '!rating':
        print('Invalid input')
        continue
    elif input_1 == '!rating':
        print(ratings)
        continue

    # fuc
    q = []
    for i in input_2[input_2.index(input_1)+1:]:
        q.append(i)
    for i in input_2[:input_2.index(input_1)]:
        q.append(i)

    if option == input_1:
        print(f'There is a draw ({option})')
        ratings += 50
        continue

    if (len(q)/2) > q.index(option):
        print(f'Sorry, but the computer chose {option}')
    else:
        print(f'Well done. The computer chose {option} and failed')
        ratings += 100
print('Bye!')
file.close()
