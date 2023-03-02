def check_palindrome_sentence(sentence):
    split = sentence.split()
    reverse = split[::-1]
    return " ".join(reverse)
print(check_palindrome_sentence("coding with kien"))

if __name__ == "__main__":
    import doctest
    doctest.testmod()