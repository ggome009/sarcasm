from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import csv

data = []
data_labels = []

with open("./sarcasm_oneliners/data_train_sarcasm.csv") as f:
    csvreader = csv.reader(f)
    
    
    for row in csvreader:
        data.append(row[1])
        label = row[0]

        if label == '0':
            data_labels.append('neg')
        else:
            data_labels.append('pos')

vectorizer = CountVectorizer(analyzer = 'word', lowercase = False)

features = vectorizer.fit_transform(data)

features_nd = features.toarray()

X_train, X_test, y_train, y_test = train_test_split(
    features_nd,
    data_labels,
    test_size=0.20,
    train_size=0.80,
    random_state=1234
)

from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)
y_pred = log_model.predict(X_test)