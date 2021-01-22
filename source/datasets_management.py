import pandas as pd
import numpy as np
import math
import random


def readAustralian():
    australian = pd.read_csv('./datasets/australian.dat', delimiter=' ', header=None)
    australian.columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14',
                          'Target']
    australian_data = australian[
        ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14']]
    australian_target = australian[['Target']]
    return australian_data, australian_target


def readGerman():
    german = pd.read_csv('./datasets/german.data-numeric', delimiter=' ', header=None)
    german.columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15',
                      'A16',
                      'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'Target']
    german['Target'] = german['Target'] - 1
    german_data = german[
        ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
         'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24']]
    german_target = german[['Target']]
    return german_data, german_target


# Questo metodo calcola il numero necessario di esempi da eliminare per portare il dataset alla distribuzione indicata
# tramite l'attributo proportion e, successivamente, li elimina casualmente
def resizeDataset(data, target, proportion):
    n0 = np.count_nonzero(target.values == 0)
    n1 = np.count_nonzero(target.values == 1)
    toRemove = math.ceil(n1 + n0 - (n0 / proportion))
    indices = target.index[target['Target'] == 1].tolist()
    random.seed(0)
    elementsToRemove = random.sample(indices, toRemove)
    data = data.drop(elementsToRemove)
    target = target.drop(elementsToRemove)
    return data, target
