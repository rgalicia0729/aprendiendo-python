
def is_numbers_friends(a, b):
    sum_divisors_a = 0
    sum_divisors_b = 0

    for i in range(1, (a // 2) + 1):
        if a % i == 0:
            sum_divisors_a += i

    for i in range(1, (b // 2) + 1):
        if b % i == 0:
            sum_divisors_b += i

    if a == sum_divisors_b and b == sum_divisors_a:
        return True
    else:
        return False


if __name__ == '__main__':
    number_one = int(input('Enter number one: '))
    number_two = int(input('Enter number two: '))

    print(f'{number_one} and {number_two} are friends' if is_numbers_friends(
        number_one, number_two) else f'{number_one} and {number_two} are not friends')
