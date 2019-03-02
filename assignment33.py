From nltk.stem.wordnet import WordNetLemmatizer
Words = [‘gave’,’went’,’going’,’dating’]
For word in words:
         Print word+”-->”+WordNetLemmatizer().lematize(word,’v’)
