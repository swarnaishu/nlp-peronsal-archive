tagged = tagger.tag(sentence)
tree = chunker.parse(tagged)
for subtree in tree.subtrees(filter=lambda t: t.node == 'NP'):
    print subtree.leaves()
