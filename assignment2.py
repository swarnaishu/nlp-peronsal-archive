from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
   
ps = PorterStemmer() 
   
sentence = "Dancing is my passion."
words = word_tokenize(sentence) 
   
for w in words: 
    print(w, " : ", ps.stem(w)) 
