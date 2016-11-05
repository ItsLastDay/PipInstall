# PipInstall

This is a DevDays Fall 2016 project. We strive to create a classifier, which predicts whether a review for some product/service is *paid* or *not*.

### Team PipInstall
In alphabetical order:
 - Mike Koltsov
 - Boris Simiutin
 - Lesya Tishenko
 - Mikhail Chernyavsky
 
### Our progress on day 1
 - we chose a [review domain](https://github.com/ItsLastDay/PipInstall/wiki/Choosing-reviews-domain) - Internet Markets;
 - we gathered dataset from Yandex.Market;
 - we evaluated our dataset (1 assessor per 1 review) and split it into paid and good categories;
 - we brainstormed machine learning [features](https://github.com/ItsLastDay/PipInstall/wiki/ML-features) that we'll use + did some [research](https://github.com/ItsLastDay/PipInstall/wiki/Research-papers) of existing work.  
Overall, our team gave solid performance on day 1.

### Our progress on day 2
 - we implemented most of the planned [features](https://github.com/ItsLastDay/PipInstall/wiki/ML-features) (i.e. feature extraction functions);
 - we employed various [libraries](https://github.com/ItsLastDay/PipInstall/wiki/Libraries) to do ML- and text-work for us;
 - we more or less chose a way to get {f1|accuracy}-score using sklearn classifiers and computed features;
 - we got our first results! Using 10-fold cross-validation, we have obtained 0.55-0.60 accuracy score with RandomForest.  
Overall, on day 2 we dived into code writing and finally got a feeling of the problem at hand.

### Our progress on day 3
 - we analyzed our features and selected the most effective ones;
 - we implemented a method for obtaining more labeled reviews using seed labeled reviews + raw unlabeled reviews;
 - we re-labeled our data, so that each review is labeled by 3 assessors;
 - finally, we used reviews with >= 2 assessor agreement as seed reviews and obtained a training set with more than 1000 reviews. We trained RandomForest on this set and measured classifier performance on held-out data, achieving ~70% accuracy!  
After three days of work, we got to the desired result - something that can predict truthfulness of a given review. Application of this result is questionable, because measuring review truthfulness proved to be harder than we expected.

## How to use
First, you need to split our labeled data into training and testing sets. Only reviews, for which >= 2 of 3 
assessors agree on its label, are used.  
This can be done via following commands:  
`cd ./data`  
`python3 split_data_into_train_test.py <N>`  
where `<N>` is the number (e.g. `50`) of reviews from each class (paid, good), that will be put into testing set.

Second, you need to start a "co-training" routine: it labels raw reviews using our labeled training set, and include new reviews back into the training set. As a consequence, our training set expands beyond
its initial size. This routine is done in a loop. After each iteration, the program prints some statistics: how many reviews
of each type were added, size of raw data set, examples of added paid reviews.  
Assuming that you are now in main directory, type:  
`cd ./test_model`  
`python3 cotraining.py [--break-before-iter N]`  
The optional `--break-before-iter N` argument specifies the maximum number of loop iterations (e.g. `N = 0` means "do not expand our initial training set").  
This step is **required**, even if you don't want to refine the initial training set (in this case, run with `--break-before-iter 0`).

Now, you may want to start the classifier or perform the testing.  
*Testing*. Assuming you are in `test_model` folder, type:  
`python3 final_test.py`  
This will train the classifier on obtained training set, and then run it on the testing set. The script outputs the achieved accuracy score, predicted classes (0 for good reviews, 1 for paid ones) and desired classes.  
*Using the classifier*. Assuming you are in `test_model` folder, type:  
`python3 human_interface.py`  
This will train the classifier on our training set (it can take a while). Then the script will prompt you to enter  
 - shop id
 - page number
 - sort method  
 
When you provide needed information, the script will gather 10 reviews about the given shop (using provided parameters) and 
will output classifier verdicts for each of them. The above process (except training phase) is looped until the program is closed.
