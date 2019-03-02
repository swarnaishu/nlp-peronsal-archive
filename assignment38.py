def get_user_to_word_proportion(user_to_text, word):
    user_to_word_proportion = {}
    for user in user_to_text:
        lm = LanuageModel(user_to_text[user])
        n_tokens = len(lm.lowercase_tokens)
        if n_tokens > 0:
            fd = nltk.FreqDist(lm.lowercase_tokens)
            user_to_word_proportion[user] = fd[word] / float(n_tokens)
        else:
            user_to_word_proportion[user] = 0.0
        print 'Finished user {}'.format(user.encode('utf-8'))
    return user_to_word_proportion
