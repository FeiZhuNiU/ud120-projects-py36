#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
cnt = 0

# if isinstance(enron_data, dict):
#     print(enron_data.keys())
# print(enron_data['Lay']['total_payments'])
for name in enron_data:
    if enron_data[name]['total_payments'] == 'NaN':
        cnt += 1
    print(enron_data[name])
print(cnt)
print(len(enron_data))
