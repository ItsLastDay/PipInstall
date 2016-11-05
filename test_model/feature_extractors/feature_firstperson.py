import pymystem3
import re

mystem = pymystem3.Mystem()

re_all_nonwords = re.compile('[^\w]')

def is_first_person_pro(mystem_output):
    # Example output from mystem:
    # [{'analysis': [{'lex': 'я', 'gr': 'SPRO,ед,1-л=им'}], 'text': 'я'}, {'text': '\n'}]
    try:
        gr_info = mystem_output[0]['analysis'][0]['gr']
        return 'PRO' in gr_info and '1-л' in gr_info
    except (IndexError, KeyError):
        return False

def is_second_person_pro(mystem_output):
    # Example output from mystem:
    # [{'analysis': [{'lex': 'ты', 'gr': 'SPRO,ед,2-л=им'}], 'text': 'ты'}, {'text': '\n'}]
    try:
        gr_info = mystem_output[0]['analysis'][0]['gr']
        return 'PRO' in gr_info and '2-л' in gr_info
    except (IndexError, KeyError):
        return False


def feature_firstperson(reviews_array, texts):
    features = []

    for text in texts:
        count_first_person = 0
        count_second_person = 0

        for word in text.split(' '):
            if not word:
                continue
            mystem_output = mystem.analyze(word)
            count_first_person += is_first_person_pro(mystem_output)
            count_second_person += is_second_person_pro(mystem_output)

        # Avoid division by zero.
        features.append([count_first_person / (1 + count_second_person)])

    return features


