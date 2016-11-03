import numpy as np
import matplotlib.pylab as plt
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.model_selection import cross_val_score, train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report


def main():
    # json = load_reviews()
    # json = json['good'] + json['paid']
    # texts = [lemmatize_text(text) for text in json_to_texts(json)]
    #
    # X_train_vect = vectorize_texts(texts)
    # np.save('computed_features/feature_words_vector', X_train_vect)
    #
    # X_train_typos = count_all_typos(texts)
    # np.save('computed_features/feature_spelling', X_train_typos)

    features = [
                'feature_words_vector',
                'get_features_synonim',
                'feature_caps_words',
                'feature_contradistinctive_particles',
                'feature_firstperson',
                'feature_length_of_review',
                #'feature_parts_of_speech',
                'feature_unigrams_bigrams',
                'get_features_mean_len_word',
                'get_features_meta',
                'get_features_number_exclamation'
                ]
    print([(feature, len(np.load('computed_features/{}.npy'.format(feature))))
                         for feature in features])
    X = np.hstack((np.load('computed_features/{}.npy'.format(feature))
                         for feature in features))
    num_of_reviews = len(X)
    y = np.array([0 for _ in range(num_of_reviews // 2)] + [1 for _ in range(num_of_reviews // 2)])

    cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    scores = cross_val_score(RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42),
                              X, y, scoring='accuracy', cv=cv)
    
    print(scores.mean())
    return 0

    classifiers = {
        'Multinomial Naive Bayes':            MultinomialNB(),
        'Gaussian Naive Bayes':               GaussianNB(),
        'Logistic Regression':                LogisticRegression(n_jobs=-1, random_state=42),
        'SGD':                                SGDClassifier(loss='log', n_jobs=-1, random_state=42),
        'Linear SVC':                         LinearSVC(random_state=42),
        'RBF SVC':                            SVC(probability=True, C=0.7, random_state=42),
        'Decision Tree (depth = None)':       DecisionTreeClassifier(random_state=42),
        'Decision Tree (depth = 10)':         DecisionTreeClassifier(max_depth=10, random_state=42),
        'Random Forest (n_estimators = 250)': RandomForestClassifier(n_estimators=250, n_jobs=-1, random_state=42),
        'Random Forest (n_estimators = 500)': RandomForestClassifier(n_estimators=500, n_jobs=-1, random_state=42),
        'AdaBoost':                           AdaBoostClassifier(),
        'Voting Classifier':                  VotingClassifier(estimators=[
                                                ('LR', LogisticRegression(n_jobs=-1, random_state=42)),
                                                ('RF', RandomForestClassifier(n_estimators=250, n_jobs=-1, random_state=42)),
                                                ('NB', MultinomialNB())
                                                ])#, voting='soft', weights=[2,1,2])

    }

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    for clf_name, clf in sorted(classifiers.items()):
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print('Classifier:', clf_name)
        print('Accuracy score:', accuracy_score(y_test, y_pred))
        if clf_name == 'Random Forest (n_estimators = 500)':
            print(y_test)
            print(y_pred)
        #print('Classification report:\n', classification_report(y_test, y_pred))
        print('----------------------------------------------')


if __name__ == '__main__':
    main()
