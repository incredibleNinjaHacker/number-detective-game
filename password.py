from random import randint

lowest = 1
highest = 97

awnser = randint(lowest, highest)

while True:
    guess = input ('The number is:' + str (lowest) + '-' + str(highest) +
  ':\n>>')


    try:
        guess = int(guess)
    except ValueError:
        print('sorry, the password must be/n')
        continue


    if guess <= lowest or guess >= highest:
        print("please enter a password from" + str(lowest) + '-' + str(highest) + '/n')
        continue


    if guess == awnser:
        print("You are right!!!!!!!!You win!!!!")
        break
    elif guess < awnser:
        lowest = guess
    else:
        highest = guess
