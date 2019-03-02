import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpusdir = 'newcorpus/' # Directory of corpus.
newcorpus = PlaintextCorpusReader(corpusdir, '.*')
nltk.tokenize.sent_tokenize() and nltk.tokenize.word_tokenize()