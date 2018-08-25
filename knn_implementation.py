#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from random import randint
import math


class MykNN:

    def fit(self, X_train, y_train, k=3):
        self.X_train = X_train # Examples
        self.y_train = y_train # Labels
        self.m = len(y_train) # Number of examples
        assert(k > 0 and k < self.m)
        self.k = k

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            label = self.k_closest(x)
            predictions.append(label)
        return predictions

    def k_closest(self, target):
        k_closest_dist_idx = []
        for l in range(self.k):

            closest_dist_idx = self.initial_closest(k_closest_dist_idx)
            closest_dist = self.euclidean(target, self.X_train[closest_dist_idx])

            for i in range(1, self.m):
                distance = self.euclidean(target, self.X_train[i])
                if distance < closest_dist and i not in k_closest_dist_idx:
                    closest_dist = distance
                    closest_dist_idx = i

            k_closest_dist_idx.append(closest_dist_idx)

        votes = [self.y_train[x] for x in k_closest_dist_idx] # Get the labels
        majority_vote = max(set(votes), key=votes.count)
        return majority_vote

    def initial_closest(self, k_closest_dist_idx):
        closest_dist_idx = 0
        # Make sure it doesn't pick the same nearest neighbour
        while closest_dist_idx in k_closest_dist_idx:
            closest_dist_idx = randint(1, self.m - 1)
        return closest_dist_idx

    def euclidean(self, a, b):
        dist = 0
        for i in range(len(a)):
            dist += (a[i] - b[i])**2
        return math.sqrt(dist)


def main():

    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4)

    # clf = neighbors.KNeighborsClassifier()
    clf = MykNN()
    clf.fit(X_train, y_train)

    predictions = clf.predict(X_test)
    print(accuracy_score(y_test, predictions))


if __name__ == '__main__':
    main()