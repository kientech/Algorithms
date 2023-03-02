def remove_duplicates_sentence(sentence):
    """
       Remove duplicates from sentence
    """
    split = sentence.split()
    add_set = set(split)
    sort_set = sorted(add_set)
    return " ".join(sort_set)
print(remove_duplicates_sentence('Python is great and Java is also great'))




