from pymystem3 import Mystem
from nltk.corpus import stopwords
import os.path

m = Mystem()
has_initialized_dict = False
stop_words = set(stopwords.words('russian'))

syn_dict_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
    'syn_dict.txt'))

synonim_dict = open(syn_dict_path).read().split('\n')
syn_dict = {}

def get_syn_dict():
    global has_initialized_dict
    if has_initialized_dict:
        return syn_dict
    has_initialized_dict = True
    for it in synonim_dict:
        string = it.split('|')
        if len(string) >= 2:
            # There can be multiword "words" in synonim dictionary.
            # Ignore them.
            if ' ' in string[0].strip():
                continue
            # And they may be in non-lemmatized form.
            initial_word = ' '.join(word for word in m.lemmatize(string[0]) if all(ch.isalpha() for ch in word))
            # Lemmatized forms can repeat.
            if initial_word in syn_dict:
                continue
            other_words = [' '.join(word for word in m.lemmatize(t) if all(ch.isalpha() for ch in word)) for t in string[1:]]

            other_words = set(other_words)
            try:
                other_words.remove(initial_word)
            except KeyError:
                pass
            syn_dict[initial_word] = list(other_words)
    return syn_dict
        
def get_features_synonim(reviews_array, texts):
    features = []
    syn_dict = get_syn_dict()
    for text in texts:
        features.append([0])
        lemmas = text.split(' ')
        for lemma in lemmas:
            count_syn = 0
            if lemma.isalpha() and lemma not in stop_words:
                var = syn_dict.get(lemma, [])
                for word in var:
                    if word in stop_words:
                        continue
                    while word in lemmas:
                        count_syn += 1
                        lemmas.remove(word)
            features[-1][0] += count_syn
    return features




