# Pankaj shukla  intrusion dection detection 

# Web attacks detection with machine learning
Machine learning algorithms applied on HTTP logs analysis to detect intrusions and suspicious activities.

## How to use
### Encode your http logs and save the result into a csv file
<code> $ python label-raw-data.py -l ./raw-http-logs-samples/access-2018-12-15.log -d ./labeled-data-samples/access-2018-12-15.csv</code>

### Train a model and test the prediction
<code> $ python logistic-regression-classifier.py -t ./labeled-data-samples/all.csv  -v ./labeled-data-samples/feb_2017.csv </code>

