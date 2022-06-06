# check if input is valid
def is_input_valid(name, dob, age, hobbies):
    # valid name
    if len(name) < 1:
        return False

    # valid date format: dd/mm/yyyy
    if len(dob) != 10 or dob[2] != '/' or dob[5] != '/':
        return False

    # valid age
    if not age.isdigit() or int(age) < 0:
        return False

    # valid hobbies
    if len(hobbies) < 1:
        return False

    return True
