# PipInstall

This is a DevDays Fall 2016 project. We strive to create a classifier, which predicts whether a review for some product/service is *paid* or *not*.

## Team PipInstall
In alphabetical order:
 - Mike Koltsov
 - Boris Simiutin
 - Lesya Tishenko
 - Mikhail Chernyavsky
 
## Our progress on day 1
 - we chose a [review domain](https://github.com/ItsLastDay/PipInstall/wiki/Choosing-reviews-domain) - Internet Markets;
 - we gathered dataset from Yandex.Market;
 - we evaluated our dataset (1 assessor per 1 review) and split it into paid and good categories;
 - we brainstormed machine learning [features](https://github.com/ItsLastDay/PipInstall/wiki/ML-features) that we'll use + did some [research](https://github.com/ItsLastDay/PipInstall/wiki/Research-papers) of existing work.  
Overall, our team gave solid performance on day 1.

## Our progress on day 2
 - we implemented most of the planned [features](https://github.com/ItsLastDay/PipInstall/wiki/ML-features) (i.e. feature extraction functions);
 - we employed various [libraries](https://github.com/ItsLastDay/PipInstall/wiki/Libraries) to do ML- and text-work for us;
 - we more or less chose a way to get {f1|accuracy}-score using sklearn classifiers and computed features;
 - we got our first results! Using 10-fold cross-validation, we have obtained 0.55-0.60 accuracy score with RandomForest.  
Overall, on day 2 we dived into code writing and finally got a feeling of the problem at hand.

## Our progress on day 3
 - we analyzed our features and selected the most effective ones;
 - we implemented a method for obtaining more labeled reviews using seed labeled reviews + raw unlabeled reviews;
 - we re-labeled our data, so that each review is labeled by 3 assessors;
 - finally, we used reviews with >= 2 assessor agreement as seed reviews and obtained a training set with more than 1000 reviews. We trained RandomForest on this set and measured classifier performance on held-out data, achieving ~70% accuracy!  
After three days of work, we got to the desired result - something that can predict truthfulness of a given review. Application of this result is questionable, because measuring review truthfulness proved to be harder than we expected.
