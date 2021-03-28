import random


def create_cast_list(filename):
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list
    with open(filename, 'r') as f:
        return [line.split(',')[0].strip() for line in f]


# cast_list = create_cast_list('files/flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor)


# print(__name__)


def create_word_list():
    word_file = "files/words.txt"

    # # Using for loop
    # word_list = []
    # with open(word_file, 'r') as words:
    #     for line in words:
    #         # remove white space and make everything lowercase
    #         word = line.strip().lower()
    #         # don't include words that are too long or too short
    #         if 3 < len(word) < 8:
    #             word_list.append(word)

    # short-hand
    with open(word_file, 'r') as words:
        word_list = [
            line.strip().lower()
            for line in words
            if 3 < len(line.strip().lower()) < 8
        ]

    return word_list


# Returns a string consisting of three random words concatenated together without spaces
def generate_password():
    word_list = create_word_list()

    # # Using for loop
    # words = []
    # for i in range(3):
    #     words.append(random.choice(word_list))
    # return ''.join(words)

    # short-hand
    return ''.join(
        random.sample(word_list, 3)
    )


# print(generate_password())


# HINT: create a dictionary from flowers.txt
def get_flowers_dict():
    flowers_dict = {}
    with open('files/flowers.txt', 'r') as f:
        for line in f:
            letter, name = line.strip().split(': ')
            flowers_dict[letter] = name
    return flowers_dict


# HINT: create a function to ask for user's first and last name
def match_flower_name():
    try:
        first_name, last_name = input('Enter your First [space] Last name only: ').split(' ')
        first_letter = first_name[0].upper()
        flowers_dict = get_flowers_dict()

        # print the desired output
        print('Unique flower name with the first letter: {}'.format(flowers_dict[first_letter]))
    except ValueError as ve:
        print('Error: ', ve)
    except KeyError as ke:
        print('No flower starts with provided first letter {}'.format(ke))


match_flower_name()
