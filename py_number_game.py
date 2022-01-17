import random as rnd

min_boundary = 1
max_boundary = int(input('max boundary to guess  '))  # setting boundaries for randomizing


def number_create():
    """
creating random number
    """
    random_number = rnd.randint(min_boundary, max_boundary)
    return random_number


def number_guess():
    """
guessing the number. we will use Divide and Conquer Algorithm
the main point is to divide big problem in 2 sub-problems until they become easy to solve.
in our case we are going to  divide guessing range by 2 and move to the next sub-problem
    """
    count = 0  # variable for counting tries
    min_number, max_number = min_boundary, max_boundary
    number_to_guess = number_create()
    try_to_guess = max_number / 2

    while try_to_guess != number_to_guess:  # continue our cycle until we guess the number
        count += 1
        if try_to_guess < number_to_guess:  # if our guess < number we want to guess
            min_number = try_to_guess + 1
            try_to_guess = round((min_number + max_number) / 2)  # we start to search left side of boundary
        elif try_to_guess > number_to_guess:  # if our guess > number we want to guess
            max_number = try_to_guess - 1
            try_to_guess = round((min_number + max_number) / 2)  # we start to search right side of boundary

    return count  # print(f'number {number_to_guess} guessed in {count} iterations') delete count and \# if want to play


def game_test(number_test):
    """
we will test our game number_test times
    """
    count_list = []  # make a list to save our tries
    test = (number for number in range(number_test))  # generator for test

    for number in test:  # we play game number_test times
        count_list.append(number_guess())
    mid_counts = sum(count_list) / len(count_list)  # count our mid-amount of tries

    return mid_counts


print(f'average tries to guess the number is {game_test(1000)}')
