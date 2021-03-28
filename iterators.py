lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


# Write a generator function that works like the built-in function "enumerate".
def my_enumerate(iterable, start=0):
    index = start
    for element in iterable:
        yield index, element
        index += 1


# # test with these
# print(my_enumerate(['a', 'b', 'c'], 6))
# print(enumerate(['a', 'b', 'c']))

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
print()


def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    # start, length = 0, len(iterable)
    # while start < length:
    #     yield iterable[start:start+size]
    #     start += size

    # short-hand alternative
    for index in range(0, len(iterable), size):
        yield iterable[index:index + size]

    # generator_comprehension equivalent: (not sure about the correctness of this)
    # return (iterable[index:index + size] for index in range(0, len(iterable), size))


for chunk in chunker(range(25), 4):
    print(list(chunk))
print()


# list_comprehension - produces a list of squares:
sq_list = [x**2 for x in range(10)]
print('sq_list: ', sq_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print('sq_list: ', sq_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] => elements intact
print('=> This list can be iterated through many times')
print('=> Each accessed element stays intact except when explicitly modified', '\n')

# generator_comprehension - produces an iterator of squares:
sq_iterator = (x**2 for x in range(10))
print('list(sq_iterator): ', list(sq_iterator))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print('list(sq_iterator): ', list(sq_iterator))  # [] => now empty
print('=> This iterator is iterated through only once')
print('=> Each accessed element is removed from the iterator', '\n')
