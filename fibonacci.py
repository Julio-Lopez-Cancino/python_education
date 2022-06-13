def fibonacci(stop, start):
    first = 0
    second = 1
    while second < stop:
        print(second)
        first, second = second, first + second
while True:
    try:
        n = int(input("n = "))
        fibonacci(n, 0)
        break
    except ValueError:
        print('Please enter a number')
