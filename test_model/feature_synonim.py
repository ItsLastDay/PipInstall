from pymystem3 import Mystem

synonim_dict = open("syn_dict.txt").read().split('\n')
syn_dict = {}
for it in synonim_dict:
    string = it.split('\t')
    if len(string) == 2:
        syn_dict[string[0]] = string[1].split(' ')
    
def get_features_synonim(reviews_array):
    features = []
    mstem = Mystem()
    for review in reviews_array:
        features.append([0])
        lemmas = mstem.lemmatize(review.get('text','') + review.get('pro','') + review.get('contra',''))
        for lemma in lemmas:
            count_syn = 0
            if lemma.isalpha():
                var = syn_dict.get(lemma, [])
                for word in var:
                    if word in lemmas != -1:
                        count_syn += 1
                        lemmas.remove(word)
            features[len(features) - 1][0] += count_syn
    return features




