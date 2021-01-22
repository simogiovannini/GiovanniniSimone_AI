from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
import math
import numpy as np

# indicano per ogni dataset e per ogni algoritmo il valore, da dare al peso della classe 1, che massimizza il roc_auc_score
class1_weight = {0.7: [[1, 2, 1.5], [1, 2, 2]],
                 0.75: [[1.2, 3, 2.5], [2, 2.5, 3]],
                 0.8: [[3, 3.5, 3], [2, 4, 3]],
                 0.85: [[5, 4, 4.5], [2, 6, 5]],
                 0.9: [[8, 9, 8], [3, 10, 11]],
                 0.95: [[15, 17, 10], [15, 15, 18]],
                 0.975: [[20, 25, 20], [21, 20, 25]],
                 0.99: [[25, 30, 25], [24, 25, 35]]
                 }


def getScores(data_train, target_train, data_test, target_test, proportion, dataset):
    scores = [0, 0, 0]
    scores[0] = getPerceptronScore(data_train, target_train, data_test, target_test, proportion, dataset)
    scores[1] = getDecisionTreeScore(data_train, target_train, data_test, target_test, proportion, dataset)
    scores[2] = getRandomForestScore(data_train, target_train, data_test, target_test, proportion, dataset)
    return scores


# Provo erceptron, ritorna lo score AUC-ROC
def getPerceptronScore(data_train, target_train, data_test, target_test, proportion, dataset):
    perceptron = Perceptron(class_weight={0: 1, 1: class1_weight[proportion][dataset][0]})
    perceptron.fit(data_train, target_train.values.ravel())
    predP = perceptron.predict(data_test)
    score = roc_auc_score(target_test, predP)
    score = round(score * 100, 1)
    return score


# Provo DecisionTree, ritorna lo score AUC-ROC
def getDecisionTreeScore(data_train, target_train, data_test, target_test, proportion, dataset):
    tree = DecisionTreeClassifier(criterion='entropy', class_weight={0: 1, 1: class1_weight[proportion][dataset][1]}, random_state=0)
    tree.fit(data_train, target_train.values.ravel())
    score = roc_auc_score(target_test, tree.predict_proba(data_test)[:, 1])
    score = round(score * 100, 1)
    return score


# Provo RandomForest, ritorna lo score AUC-ROC
def getRandomForestScore(data_train, target_train, data_test, target_test, proportion, dataset):
    forest = RandomForestClassifier(criterion='entropy', class_weight={0: 1, 1: class1_weight[proportion][dataset][2]}, random_state=0)
    forest.fit(data_train, target_train.values.ravel())
    score = roc_auc_score(target_test, forest.predict_proba(data_test)[:, 1])
    score = round(score * 100, 1)
    return score
