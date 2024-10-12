# -*- coding: utf-8 -*-
"""sin_cosec.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nDKNntJ6yNqfEPJVinQd8BfKfgcJnawN
"""

def degree_approximation(degree):
    degree = degree % 360
    if degree == 0:
        return 0
    elif degree == 90:
        return 1
    elif degree == 180:
        return 0
    elif degree == 270:
        return -1
    elif degree == 360:
        return 0
    if degree > 90 and degree < 180:
        return degree_approximation(180 - degree)
    elif degree > 180 and degree < 270:
        return -degree_approximation(degree - 180)
    elif degree > 270 and degree < 360:
        return -degree_approximation(360 - degree)
    radian = degree * (3.14159 / 180)
    return radian - (radian ** 3) / 6

def sin_cosec_calculator():
    while True:
        print("======================================")
        print('sin to calculate sine : ')
        print('cosec for cosec : ')
        print('q to quit : ')
        print("======================================")
        choice = input('Enter your choice : ')

        if choice == 'sin':
            a = float(input('Enter the value in degree : '))
            res = degree_approximation(a)
            res = round(res, 5)
            print('Sin = ', res)

        elif choice == 'cosec':
            a = float(input('Enter the value in degree : '))
            res = degree_approximation(a)
            if res == 0:
                print('Cosec is undefined for this angle (division by zero).')
            else:
                print('Cosec = ', round(1 / res, 5))

        elif choice == 'q':
            print(".......Exiting the program...")
            break
        else:
            print('Invalid input')

sin_cosec_calculator()
