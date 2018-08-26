#!/usr/bin/env python3

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def preprocess(X):

    # Map strings into numericals
    sex_map = {'male': 0, 'female': 1}
    embark_map = {'C': 0, 'Q': 1, 'S': 2}
    X = X.replace({'Sex': sex_map})
    X = X.replace({'Embarked': embark_map})

    # Fill missing values
    X = X.fillna(X.mean())

    # Normalize (No need for Decision Tree)
    # X = (X - X.mean()) / X.std()

    return X


def main():

    titatic_data = pd.read_csv('train.csv')

    # Feature selection
    X = titatic_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked']]
    y = titatic_data[['Survived']]

    X = preprocess(X)

    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Test
    titatic_test = pd.read_csv('test.csv')
    X_test = titatic_test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked']]
    X_test = preprocess(X_test)

    predictions = clf.predict(X_test)
    indices = titatic_test['PassengerId']
    predictions = pd.DataFrame(data=predictions, index=indices, columns=['Survived'])

    predictions.to_csv('titanic _submission.csv')


if __name__ == '__main__':
    main()