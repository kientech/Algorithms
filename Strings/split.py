def split(strings, separator):
    split_word = []
    last_index = 0
    for index, character in enumerate(strings):
        if character == separator:
            split_word.append(strings[last_index:index])
            last_index = index + 1
        elif index + 1 == len(strings):
            split_word.append(strings[last_index: index + 1])
    return split_word
print(split("Hello/Kien", "/"))