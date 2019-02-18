from nltk.corpus import words as nltk_words
def is_german_word(word):
    dictionary:dict.fromkeys(nltk_words.words(),none)
    try:
        x=dictionary[word]
        return true
    except keyError:
        return false