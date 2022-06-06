from utils.validators import is_input_valid
from utils.file import write_to_file


def display_form():
    print("Enter your name: ")
    name = input()
    print("Enter your DOB (dd/mm/yyyy): ")
    dob = input()
    print("Enter your age: ")
    age = input()
    print("Enter your Hobbies: ")
    hobbies = input()

    # check if input is valid
    if is_input_valid(name, dob, age, hobbies):
        # write the data to the file
        write_to_file(name, dob, age, hobbies)
    else:
        print("Invalid input. Please try again.")
        display_form()


display_form()
