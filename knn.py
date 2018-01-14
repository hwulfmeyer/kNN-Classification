"""
This file is for the methods concerning everything naive bayes

TODO:
1. convert nominal values to numbers DONE!
2. 2/3 of the data is training data, rest is test DONE from previous!
3. k is specified at runtime ? DONE searching the nearest neighbors
4. majority vote between neighbors DONE
5. reverse trasform from number to class.
6. error rate? mean error over 100 samples?
7. confusion matrix?
"""
import math
from operator import itemgetter


def calculate_error(dataclasses: list):
    """
    calculates the error rate, = misclassified_data / total data
    :param dataclasses: a 1-dimensional list containg the orignal and predicted class of each instance in data
    :return: error rate ( <=1.0)
    """
    wrong = 0
    correct = 0

    for d in dataclasses:
            if d[0] == d[1]:
                correct += 1
            else:
                wrong += 1
    return wrong / (wrong+correct)


def get_confusion_matrix(classes: list, dataclasses: list):
    """
    creates a confusion matrix
    :param classes: is a one-dimensional list containing the class names
    :param dataclasses: a 1-dimensional list containg the orignal and predicted class of each instance in data
    :return: a 2-dimensional list with the first row being the actual class and every other row corresponding
        to the number of instances being predicted as class x
    """
    confmatrix = []
    for x in classes:
        line = [x]
        for y in classes:
            line.append(sum(x == inst[0] and y == inst[1] for inst in dataclasses))
        confmatrix.append(line)
    return confmatrix


def euclidean_distance(input1: list, input2: list):
    """
    fucntion that calculates the euclidean distance for our task and for 6 dimensions only
    :param input1: instance 1
    :param input2: instance 2
    :return: distance
    """
    distance = 0
    for i in range(len(input1)):
        distance += pow(input1[i] - input2[i], 2)
    distance = math.sqrt(distance)
    return distance


def search_nearest(trainingset: list, inputvector: list, k: int):
    """
    fucntion that searches for k nearest neighbors
    :param trainingset: already separated and transformed train set
    :param inputvector: input instance from test data
    :param k: the number of searched neighbors
    :return: k nearest neighbors
    """
    distances = []
    for inst in trainingset:
        distances.append([inst, euclidean_distance(inst, inputvector)])
    distances = sorted(distances, key=itemgetter(1))
    near_neighbours = []
    for i in range(k):
        near_neighbours.append(distances[k][0])
    return near_neighbours


def getting_class(list_of_neighbors: list, classes: list):
    """
    function that get a certain class from majority vote
    :param list_of_neighbors: list of vectors(neighbors)
    :param classes: is a one-dimensional list containing the class names
    :return: choosen class
    """
    print(list_of_neighbors)
    votecounter = []
    for k in range(len(classes)):
        votecounter.append([k, 0])
    for k in range(len(list_of_neighbors)):
        target = list_of_neighbors[k][-1]
        votecounter[target][1] += 1
    votecountersorted = sorted(votecounter, key=itemgetter(1), reverse=True)
    return classes[votecountersorted[0][0]]

