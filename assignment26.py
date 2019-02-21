import grammar_check
tool=grammar_check.LanguageTool('en-gb')
sentence='he is playing cricket'
matches=tool.check(sentence)
len(matches)
grammar_check.correct(text,matches)