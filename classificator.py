import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from training_data import data


def categorize(article):
    # Define the training data

    # Create a CountVectorizer object to convert the text into a matrix of word counts
    vectorizer = CountVectorizer()

    # Transform the training data into a matrix of word counts
    X_train = vectorizer.fit_transform(np.concatenate(list(data.values())))

    # Create a label array for the training data
    y_train = np.concatenate([[label] * len(texts) for label, texts in data.items()])

    # Train a Multinomial Naive Bayes classifier on the training data
    clf = MultinomialNB().fit(X_train, y_train)

    # Convert the new text into a matrix of word counts
    X_new = vectorizer.transform([article])

    # Use the trained classifier to predict the category of the new text
    predicted_category = clf.predict(X_new)[0]

    return predicted_category
