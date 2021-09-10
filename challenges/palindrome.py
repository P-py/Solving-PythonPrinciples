def palindrome(text):
    list_letters = list(text)
    list_letters = list_letters[::-1]
    new_text = ''.join(list_letters)
    
    return new_text == text