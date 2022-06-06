# format string for csv
def format_string(string):
    string = string.replace("\\", "\\\\").replace(",", "\,").replace(
        "\"", "\\\"").replace("'", "\\'")

    return '"' + string + '"'
