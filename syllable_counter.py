def syllable_counter(word):
    counter = 0
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    word = word.lower()
    word_letters = list(word)
    for letter in word_letters:
        if letter in vowel:
            counter += 1
        else:
            pass
    return counter
