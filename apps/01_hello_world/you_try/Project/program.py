import random

print('-----------------------------------')
print('      Guess that Number Game')
print('-----------------------------------')

the_number = random.randint(0, 100)

name = input('Player what is your name?' )
guess = -1

while guess != the_number:

    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry, {}. Your guess of {} was too low ' .format(name, guess))
    elif guess > the_number:
        print('Sorry, {}. Your guess of {} is too high. ' .format(name, guess))
    else:
        print('Excellent work {}, you won! The correct number was {} '.format(name, guess))

print('done')

