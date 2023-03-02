def lower(word):
    lenght = len(word)
    for i in range(lenght):
        if ('A' <= word[i] <= 'Z'):
            word = word[0:i] + chr(ord(word[i]) - ord('A') + ord('a')) + word[i + 1:]
    return word
print(lower('PYTHON'))