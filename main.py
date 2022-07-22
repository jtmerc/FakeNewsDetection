# run jupyter lab

# import modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# [1] Read the data
df = pd.read_csv('./news.csv')
# Get shape and head
df.shape
df.head()

# [2] Get the labels
labels = df.label
labels.head()

# [3] Split the dataset
x_train, x_test, y_train, y_test = train_test_split(df['text'], labels,
                                                    test_size=0.2, random_state=7)
# [4] Initialize a TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
# Fit and transform train set, transform test set
tfidf_train = tfidf_vectorizer.fit_transform(x_train)
tfidf_test = tfidf_vectorizer.transform(x_test)

# [5] Initialize a Passive Aggressive Classifier
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)
# Predict on the test set and calculate accuracy
y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f'Accuracy: {round(score*100,2)}%')

# [6] Build confusion matrix
confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])
print(confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL']))
# [true_positives, false negatives][false positives, true negatives]
