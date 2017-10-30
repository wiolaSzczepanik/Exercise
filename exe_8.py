def is_palindrome(word_to_check):
    if word_to_check == word_to_check[::-1]:
        return True
    else:
        return False
