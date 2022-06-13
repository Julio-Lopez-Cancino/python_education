qs = ['What is your name?\n',
      'What is your fav. color?\n',
      'What is your quest?\n']

n = 0
while True:
    print('Type q to quit')
    a = input(qs[n])
    if a == 'q':
        break
    n = (n + 1) % 3
