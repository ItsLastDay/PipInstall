import numpy as np
import enchant
from enchant.utils import levenshtein


checker = enchant.Dict('ru_RU')


def count_typos(text):
    errors = 0
    for word in text:
        if not checker.check(word):
            suggestions = checker.suggest(word)
            if suggestions:
                errors += levenshtein(word, suggestions[0])

    return [errors]


def feature_spelling(reviews_array, texts):
    return [[count_typos(text.split(' '))] for text in texts]


def count_all_typos(texts):
    return np.asarray([count_typos(text) for text in texts])


def main():
    texts = [['Мама', 'мыла', 'рамй'], ['Фыва', 'олдж']]
    print(count_all_typos(texts))

if __name__ == '__main__':
    main()
