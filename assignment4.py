from nltk.corpus import brown
from nltk.tokenize import word_tokenize 

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                 if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

    tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
        for tag in sorted(tagdict):
              print(tag, tagdict[tag])






