def make_ing_form(word):
    last_letter = -1
    second_to_last = -2
    third_to_last = -3
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w', 'y']

    if word[last_letter] == "e":
        if word[second_to_last] == "i":
            return word[:second_to_last]+"ying"
        return word[:last_letter] + "ing"
    elif word[third_to_last].upper() in consonant and word[second_to_last].upper() not in consonant and word[last_letter].upper() in consonant:
        return word + word[last_letter] + "ing"
    else:
        return word + "ing"
