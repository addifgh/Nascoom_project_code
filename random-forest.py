
from utilities import *

args = get_args()
traning_data = args['traning_data']
testing_data = args['testing_data']

# Get training features and labeles
training_features, traning_labels = get_data_details(traning_data)

# Get testing features and labels
testing_features, testing_labels = get_data_details(testing_data)

# LOGISTIC REGRESSION CLASSIFIER
print ("\n\n=-=-=-=-=-=-=- Random forest Classifier -=-=-=-=-=-\n")

attack_classifier = RandomForestClassifier(n_estimators = 1000, random_state = 42)
attack_classifier.fit(training_features, traning_labels)

predictions = attack_classifier.predict(testing_features)
print ("The precision of the Random Forest is: " + str(get_occuracy(testing_labels,predictions, 1)) + "%")
