

#Check if word with at least 10 characters exists in text block
def char_word(elements):
    value = False
    for e in elements:
        for w in e.text.split():
            if len(w) >= 10:
                value = True
    return value

#Print the longest word on the page
def longest_word(elements):
    word = ""
    for e in elements:
        word_max = max(e.text.split(), key=len)
        if len(word_max) > len(word):
            word = word_max
    return word
