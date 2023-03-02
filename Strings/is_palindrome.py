def is_palind_rome(strings):
    '''
        Return string is palindrome or not
    '''
    reverse = strings[::-1]
    if strings == reverse:
        return True
    return False
print(is_palind_rome("codingwithkien"))