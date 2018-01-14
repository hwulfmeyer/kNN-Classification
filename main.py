"""
This file is for executing everything together
"""
import filehandling as fiha
import knn


filepathnames = "datasets/cardaten/carnames.data"
filepathdata = "datasets/cardaten/car.data"

# read data
classes, attributes, attribute_values = fiha.read_data_names(filepath=filepathnames)
instances = fiha.read_data(filepath=filepathdata)
print("Number of Classes: " + str(len(classes)))
print("Number of Attributes: " + str(len(attributes)))
train_data, test_data = fiha.separation(instances)
print("Number of Training Instances: " + str(len(train_data)))
print("Number of Test Instances: " + str(len(test_data)))


# the code below is copied from the naive bayes algorithm main.py and still needs to be adapted
"""
test_error = knn.calculate_error(testdata_classes)
print("Error rate: " + str(test_error))

# get mean error over k samples
mean_error = 0
k = 100
for x in range(k):
    train_data, test_data = fiha.separation(instances)
    testdata_classes = knn.get_classes(...)
    mean_error += knn.calculate_error(testdata_classes)
mean_error = mean_error / k
print("Mean Error over " + str(k) + " samples: " + str(mean_error))

confusion_matrix = knn.get_confusion_matrix(classes, testdata_classes)
print("\nConfusion Matrix:")
for x in confusion_matrix:
    print(x)

"""

numeraldata = fiha.modify(instances)
train_data, test_data = fiha.separation(numeraldata)
checklist = knn.search_nearest(train_data, test_data[0], 5)
print(knn.getting_class(checklist, classes))
