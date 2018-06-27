__author__ = 'dimascio'
# edited 7/7/18 by YG

import requests
import json

# Replace YOUR_CLASSIFIER_ID, YOUR_CLASSIFIER_USERNAME, and YOUR_CLASSIFIER_PASSWORD
# with the information provided in your classifier's credentials object
def classify(s):
    return requests.post("https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/162c02x438-nlc-70/classify",
                      json.dumps({'text':s}),
                      auth=("c4e23e09-9a5a-456e-982a-a4207a191124", "vjdt2U2VRTeJ"),
                      headers={'Content-Type': 'application/json'})

# Read test data into test array

test = []
with open('data/Email-testingdata.json') as testData:
	test=json.load(testData);
	# Classify each test observation and store its prediction and label
	predictionsAndLabels = map(lambda o:  (classify(o['Text']).json(), o['Class'][0] ), test)

	# Calculate the classifier's accuracy by comparing:
	# Number of correct predictions / Number of test observations
	accuracy = 1.0 * len(filter(lambda x: x[0]['top_class'] == x[1], predictionsAndLabels)) / len(test)
	print "accuracy: %s" % accuracy
