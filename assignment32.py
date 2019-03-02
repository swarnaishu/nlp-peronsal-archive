def _setup_tokenizer(self, tokenizer: object):
    language_punkt_vars = PunktLanguageVars
    language_punkt_vars.sent_end_chars = self.external_punctuation
    language_punkt_vars.internal_punctuation = self.internal_punctuation
    tokenizer.INCLUDE_ALL_COLLOCS = True
    tokenizer.INCLUDE_ABBREV_COLLOCS = True
    params = tokenizer.get_params()
    return PunktSentenceTokenizer(params)
