try:
    answer = 20 / 0
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('Invalid input')
