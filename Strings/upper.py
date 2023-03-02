# Converts a string to uppercase
def upper(word):
    lenght = len(word)
    for i in range(lenght):
        if ('a' <= word[i] <= 'z'):
            word = word[0:i] + chr(ord(word[i]) - ord('a') + ord('A')) + word[i + 1:]
            '''
            Kien -> word
            KIen -> word
            KIEn -> word
            KIEN -> word
            '''
    return word
# Driver code
if __name__ == '__main__':
    word = 'kien'
    print(upper(word))


