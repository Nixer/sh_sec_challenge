def char_word(elements):
    value = False
    for e in elements:
        for w in e.text.split():
            if len(w) >= 10:
                value = True
    return value


def longest_word(elements):
    word = ""
    for e in elements:
        word_max = max(e.text, key=len)
        if word_max > word:
            word = word_max
    return word
