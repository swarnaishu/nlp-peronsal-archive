#install textblob, nltk
from textblob import Textblob
b=Textblob('bonjour')
b.detect_language()