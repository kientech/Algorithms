def remove_duplicate_string(string):
    new_string = "".join(sorted(set(string)))
    if new_string:
        return (new_string, len(string) - len(new_string))
    else:
        return None

print(remove_duplicate_string("codingwithkien"))