def snakes():
    how_many_snakes = 1
    snake_string = """
    Welcome to Python3!
    
                 ____
                / . .\\
                \\  ---<
                 \\  /
       __________/ /
    -=:___________/
    
    <3, Juno
    """

    print(snake_string * how_many_snakes)


# snakes()


def get_list_input(prompt, delimiter=','):
    """Accepts a CSV input string and converts it to a proper list
    Example:
        input: apple, orange, banana
        return value: ['apple', 'orange', 'banana']
    :param str prompt: The prompt to display to the user.
    :param str delimiter: The delimiter string to use in splitting the input text. Defaults to a single comma (,)
    :return: The list
    """
    return [item.strip() for item in input(prompt).split(delimiter)]


def send_assignment_message():
    # get and process input for a list of names
    # Example input: nonso umeh, diogo nans, ifee mary g, etoo travis
    names = [name.title() for name in get_list_input('Enter names of students separated by commas: ')]
    # names = ['Nonso Umeh', 'Diogo Nans', 'Ifee MaryG', 'Etoo Travis']
    print(names)

    # get and process input for a list of the number of assignments
    # Example input: 2, 1, 5, 3
    # assignments = [2, 1, 5, 3]
    assignments = None
    while assignments is None:
        try:
            assignments = [
                int(count) for count in get_list_input("Enter a list of their missing assignments' counts: ")
            ]
        except ValueError as e:
            # str(e) gives only the message string
            # repr(e) gives you the exception (and the message string)
            invalid_int = str(e).split(':')[1].strip()
            print('Supplied list contains an invalid integer: {}'.format(invalid_int))
            print(repr(e))
    print(assignments)

    # get and process input for a list of grades
    # Example input: 65.3, 88.9, 39.0, 51.5
    grades = [float(grade) for grade in get_list_input('Enter a list of their missing assignments: ')]
    # grades = [65.3, 88.9, 39.0, 51.5]
    print(grades)

    # message string to be used for each student
    # HINT: use .format() with this string in your for loop
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"

    # write a for loop that iterates through each set of names, assignments, and grades to print each student's message
    for name, assignments_count, current_grade in zip(names, assignments, grades):
        potential_grade = current_grade + 2*assignments_count
        print(message.format(name, assignments_count, current_grade, potential_grade))


# send_assignment_message()
