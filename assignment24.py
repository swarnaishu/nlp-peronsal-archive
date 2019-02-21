from nltk.corpous import moie_reviews
documents=[(list(movie_reviews.words(field)),category)
              for category in moie_reviews.categories()
              for field in moie_reviews.fields(category)]
random.shuffle(documents)
