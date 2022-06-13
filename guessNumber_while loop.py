numbers = [x for x in range(101) if x % 8 == 0]

while True:
    print('Type q to quit')
    guess = input('Type a number from 1 to 100:\n')
    if guess == 'q':
        print(f'You type {guess} to quit. Bye!')
        break
    elif int(guess) in numbers:
        print(f'Congrats! Your number {guess} was part of the chosen ones:\n{numbers}')
        break
    else:
        print('Try again\n')



'''
Instructor Example

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == 'q':
        break
    #I missed the error handling.
    try:
        answer = int(answer)
    except ValueError: 
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly")
'''
