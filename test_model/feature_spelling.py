import enchant
from enchant.utils import levenshtein


def count_typos(list_of_lists_of_words):
    checker = enchant.Dict('ru_RU')
    return sum(levenshtein(word, checker.suggest(word)[0]) if not checker.check(word) else 0
               for word in list_of_lists_of_words)


def count_all_typos(list_of_words):
    return [count_typos(text) for text in list_of_words]


def main():
    texts = [['Мама', 'мыла', 'рамй'], ['Фыва', 'олдж']]
    print(count_all_typos(texts))

if __name__ == '__main__':
    main()
