__author__ = 'bernardino'


def age_program():
    user_age = int(input("Please enter you age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f'Your age in seconds is {age_seconds}')


age_program()
