user_number = input('Hi, there! Please, type a number: ')

try:
    user_num_to_int = int(user_number)
    print(f'Here\'s your number: {user_num_to_int}')
except ValueError:
    print('Please, type an integer')
