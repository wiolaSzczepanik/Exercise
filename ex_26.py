def add_sufix(word):
    last_letter_index = -1
    one_before_last_index = -2
    consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
                 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W', 'Y']

    if word[last_letter_index] == 'e':
        if word[one_before_last_index] == 'e':
            return word + 'ing'
        elif word[one_before_last_index] == 'i':
            return word[:-1] + 'ying'
        return word[:-1] + 'ing'
    elif word[last_letter_index].upper() in consonant:
        return word + word[last_letter_index] + 'ing'
    else:
        return word + 'ing'
