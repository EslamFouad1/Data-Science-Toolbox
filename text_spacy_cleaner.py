#Transform the text
def spacy_cleaner(original_text):
    """Cleans text data to be processed.
    Removes punctuation, whitespace, numbers, stopwords from the text
    and lemmatizes each token."""

    final_tokens = []
    parsed_text = nlp(original_text)

    for token in parsed_text:
        if token.is_punct or token.is_space or token.like_num or token.is_stop:
            pass
        else:
            if token.lemma_ == '-PRON-':
                final_tokens.append(str(token))  # Keep pronouns as they are.
            else:
                sc_removed = re.sub('[^a-zA-Z]', '', str(token.lemma_))
                if len(sc_removed) > 1:
                    final_tokens.append(sc_removed)
    joined = ' '.join(final_tokens)
    preprocessed_text = re.sub(r'(.)\1+', r'\1\1', joined)

    return preprocessed_text
