"""
This file is for the methods concerning everything from file reading to file writing
"""
import re
import random


def read_data_names(filepath: str):
    """
    function to read class names & attributes

    :param filepath: the relative path to the file containing the specifications of the attribute_values
    :return: a tuple of lists
        classes: is a one-dimensional list containing the class names
        attributes: is a one-dimensional list containing the attribute names
        attribute_values: is a two-dimensional list where each row respresents
            one attribute(in the order of 'attributes') and the possible values
    """
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    classes = re.sub(r'^' + re.escape("class values: "), '', lines.pop(0))
    classes = classes.split(", ")
    attributes = re.sub(r'^' + re.escape("attributes: "), '', lines.pop(0))
    attributes = attributes.split(", ")

    attribute_values = []
    for i in range(0, len(attributes)):
        values = re.sub(r'^' + re.escape(attributes[i] + ": "), '', lines.pop(0))
        attribute_values.append(values.split(", "))

    return classes, attributes, attribute_values


def read_data(filepath: str):
    """
    function to read the actual data

    :param filepath: the relative path to the file containing the specifications of the data
    :return: the data in filepath as a two-dimensional list where each row represents one instance and
        its values
    """

    with open(filepath, "r") as f:
        lines = f.read().splitlines()
    data = []
    for line in lines:
        data.append(line.split(","))
    return data


def separation(instances):
    """
    function to separate data to 2 sets: training and test
    :param instances: lest of instances
    :return: two lists with data
    """
    size_train = int((len(instances)) * 2 / 3)
    train_dataset = []
    test_set = list(instances)  # copy the full list
    while len(train_dataset) < size_train:
        index = random.randrange(len(test_set))  # find the random index to append in train data set
        train_dataset.append(test_set.pop(index))  # reduce the size of test set and increase and add the inctances in trainset
    return train_dataset, test_set


def modify(instances: list):
    """
    the function to modify all string attributes to numbers
    :param instances: the list of instances with the rough data
    :return: the list of already modified data
    """
    final_list=[[0 for x in range(7)] for y in range(len(instances))]
    for i in range(len(instances)):
            final_list[i] = transforming(instances[i])
    return final_list


def transforming(inputvector: list):
    """
    function that transforms single input vector for satisfying condition
    :param inputvector: vectro to transform
    :return: the vector with numbers
    """
    dict_of_params = {"vhigh": 3, "high": 2, "med": 1, "low": 0, "2": 0, "3": 1, "4": 2, "5more": 3, "more": 4,
                      "small": 1, "big": 3}
    dict_of_classes = {"unacc": 0, "acc": 1, "good": 2, "vgood": 3}
    final_vector = [0 for i in range(7)]
    for i in range(6):
        final_vector[i] = dict_of_params.get(inputvector[i])
        final_vector[6] = dict_of_classes.get(inputvector[6])
    return final_vector
