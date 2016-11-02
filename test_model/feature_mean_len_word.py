
# coding: utf-8

# In[8]:

def get_features_mean_len_word(reviews_array):
    features = []
    mstem = Mystem()
    for review in reviews_array:
        features.append(0)
        lemmas = mstem.lemmatize(review.get('text','') + review.get('pro','') + review.get('contra',''))
        count_words = 0
        for lemma in lemmas:
            if lemma.isalnum():
                features[len(features) - 1] += len(lemma)
                count_words += 1
        if count_words != 0:
            features[len(features) - 1] /= count_words
        
    return features


# In[ ]:


