def prime_numbers():
    # Your code should check if each number in the list is a prime number
    check_prime = [26, 39, 51, 53, 57, 79, 85]

    # write your code here
    # HINT: You can use the modulo operator to find a factor
    iterations = {}
    for number in check_prime:
        iterations['for'] = iterations.get('for', 0) + 1
        is_prime = False
        divisor = 2
        print('number: {}, divisor: {}, iterations.for: {}'.format(number, divisor, iterations['for']))
        while number % divisor != 0:
            iterations['while'] = iterations.get('while', 0) + 1
            divisor += 1
            print('divisor: {}, upper_bound: {}, iterations.while: {}'.format(divisor, number / divisor,
                                                                              iterations['while']))
            if divisor >= number / divisor:
                is_prime = True
                break

        if is_prime:
            print('{} IS a prime number'.format(number), '\n')
        else:
            print('{} is NOT a prime number, because {} is a factor of {}'.format(number, divisor, number), '\n')

    print(iterations)


def zip_function():
    x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
    y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
    z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
    labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

    points = []
    # write your for loop here
    # for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    #    points.append('{}: {}, {}, {}'.format(label, x, y, z))
    for point in zip(labels, x_coord, y_coord, z_coord):
        points.append('{}: {}, {}, {}'.format(*point))  # spread from the zip variable {point}

    for point in points:
        print(point)


def test_transpose():
    """TRANSPOSE an Array using zip function"""
    data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

    data_transpose = tuple(zip(*data))  # replace with your code
    print(data_transpose)
    # Output: ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))


def test_enumerate():
    """Use "enumerate" to iterate through a list, accessing the {index: value} pair in each iteration"""
    cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
    heights = [72, 68, 72, 66, 76]

    # write your for loop here
    for index, name in enumerate(cast):
        cast[index] = '{} {}'.format(name, heights[index])
        # Or: cast[index] = character + " " + str(heights[index])

    print(cast)
    # Output: ['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']


def list_comprehension():
    """List Comprehension => one-line shorthand for a "for" loop"""
    # Example 1:
    # Create a new list {first_names} containing just the first names in names in lowercase.

    names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

    # Using normal "for" loop
    first_names = []
    for name in names:
        first_names.append(name.split()[0].lower())
        # Output: ['rick', 'morty', 'summer', 'jerry', 'beth']

    # Using List Comprehension
    first_names = [name.split()[0].lower() for name in names]
    print(first_names)
    # Output: ['rick', 'morty', 'summer', 'jerry', 'beth']

    # Example 2:
    # Use a list comprehension to create a list of names passed that only include those that scored at least 65.

    scores = {
        "Rick Sanchez": 70,
        "Morty Smith": 35,
        "Summer Smith": 82,
        "Jerry Smith": 23,
        "Beth Smith": 98
    }

    passed = [name for name, score in scores.items() if score >= 65]
    print(passed)
    # Output: ['Rick Sanchez', 'Summer Smith', 'Beth Smith']


print('"Dictionary" methods:')
print('====================')
flowers_dict = {}
print('1: ', flowers_dict)
flowers_dict.update({'a': '111'})
print('2: ', flowers_dict)
flowers_dict.update({'b': '222'})
print('3: ', flowers_dict)
new_dict = flowers_dict.fromkeys(['c', 'd'], False)
print('5 keys: ', flowers_dict, new_dict)
ccc = new_dict.pop('c')
print('6 ccc: ', flowers_dict, ccc)
eee = new_dict.pop('e', 'default value')
print('7 eee: ', flowers_dict, eee)
fff = flowers_dict.popitem()
print('8 fff: ', flowers_dict, fff)
flowers_dict.clear()
print('4: ', flowers_dict)
