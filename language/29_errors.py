
def average(grades):
    sum_grades = sum(grades)
    count_grades = len(grades)

    if count_grades == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')

    return sum_grades / count_grades


if __name__ == '__main__':
    print('Welcome to the average grade program.')

    grades = []

    try:
        my_average = average(grades)
        print(f'Your average of grades is: {my_average}')
    except ZeroDivisionError as e:
        print(e)
        print('There are no grades yet in your list')
    finally:
        print('Thank you!')
