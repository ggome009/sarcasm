# Takes in a CSV input and splits it into an even amount of lines that are
# categorized as 0 and 1.

from sklearn.feature_extraction.text import CountVectorizer

import csv
import json

data = []
data_labels = []
zero_cnt = 0
one_cnt = 0

# ^.*\\u(\d\w{3}).*$ <-- Finds entire line if it contains unicode characters

# Print out sarcasm rating,headline from a json file

# with open("./sarcasm_oneliners/Sarcasm_Headlines_Dataset.json") as f:
#     i = 0
#     for line in f:
#         data.append(json.loads(line))
#         print str(data[i]['is_sarcastic']) + ',' + data[i]['headline']
#         i += 1

# # Print out sarcasm rating,headline from a csv file

# with open("./sarcasm_oneliners/data_train_sarcasm.csv") as f:
with open("./sarcasm_oneliners/full_headlines.csv") as f:
    csvreader = csv.reader(f)
     
    for row in csvreader:
        data.append(row[1])
        label = row[0]
        if label == '0' and zero_cnt < 2000:
            print(row[0] + ',' + row[1]);
            zero_cnt += 1;
        elif label == '1' and one_cnt < 2000:
            print(row[0] + ',' + row[1]);
            one_cnt += 1;