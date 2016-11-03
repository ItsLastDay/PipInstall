from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from pymystem3 import Mystem

m = Mystem()

def lemmatize_text(text):
    return ' '.join(word for word in m.lemmatize(text) if all(ch.isalpha() for ch in word))


def json_to_texts(json):
    return [r.get('text', '') + '\n' + r.get('pro', '') + '\n' + r.get('contra', '')
            for r in json]


def vectorize_texts(texts):
    vectorizer = CountVectorizer(encoding='koi8r', stop_words=stopwords.words('russian'), max_features=256)
    return vectorizer.fit_transform(texts).toarray()



class FeatureWordsVector:
    def __init__(self):
        self.vectorizer = CountVectorizer(encoding='koi8r', stop_words=stopwords.words('russian'), max_features=256)

    def __call__(self, reviews_json, need_to_fit):
        texts = [lemmatize_text(text) for text in json_to_texts(reviews_json)]
        if need_to_fit:
            return self.vectorizer.fit_transform(texts).toarray()
        else:
            return self.vectorizer.transform(texts).toarray()

