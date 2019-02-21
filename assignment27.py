from nltk.parse.corenlp imort coreNLPDependencyParser
der_parser=coreNLPDependencyParser
parse=dep_parser.raw_parse('ram jumped over sunnil')
print(parse.to_conll(4))