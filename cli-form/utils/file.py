from .formatter import format_string


# write the data to the file
def write_to_file(name, dob, age, hobbies):
    file = open("data.txt", "a")

    try:
        file.write(
            f"{format_string(name)}, {dob}, {age}, {format_string(hobbies)}\n"
        )
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    finally:
        file.close()
