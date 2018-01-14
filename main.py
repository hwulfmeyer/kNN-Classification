"""
This file is for executing everything together
"""
import filehandling as fiha
import knn
import sys

knn_parameter = 1
filepathnames = "datasets/cardaten/carnames.data"
filepathdata = "datasets/cardaten/car.data"

if __name__ == "__main__":
    # console program
    knn_parameter = 1
    if len(sys.argv) >= 2:
        knn_parameter = int(sys.argv[1])
    classes, attributes, attribute_values = fiha.read_data_names(filepath=filepathnames)
    instances = fiha.read_data(filepath=filepathdata)
    numeraldata = fiha.modify(instances, attribute_values)
    print("Number of Classes: " + str(len(classes)))
    print("Number of Attributes: " + str(len(attributes)))
    train_data, test_data = fiha.separation(numeraldata)
    print("Number of Training Instances: " + str(len(train_data)))
    print("Number of Test Instances: " + str(len(test_data)))

    print("Beginning kNN Algorithm with k=" + str(knn_parameter))
    testdata_classes = knn.get_predictions(train_data, test_data, knn_parameter, classes)
    test_error = knn.calculate_error(testdata_classes)
    print("Error rate: " + str(test_error))
    confusion_matrix = knn.get_confusion_matrix(classes, testdata_classes)
    print("\nConfusion Matrix:")
    for x in confusion_matrix:
        print(x)
    # get mean error over k samples
    mean_error = 0
    i = 100
    print("")
    print("Calulating mean error over " + str(i) + " samples...")
    for x in range(i):
        train_data, test_data = fiha.separation(numeraldata)
        testdata_classes = knn.get_predictions(train_data, test_data, knn_parameter, classes)
        mean_error += knn.calculate_error(testdata_classes)
    mean_error = mean_error / i
    print("Mean Error over " + str(i) + " samples: " + str(mean_error))



