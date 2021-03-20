import os
import json
import pandas as pd
import glob

# load json into python, assign bangkok.json to 'bkk'
# load for all cities

# with open('bangkok.json') as file:
#    bkk = json.load(file)

all_json = []
for json_file in glob.glob("*.json"):
    with open(json_file, "rb") as file:
        all_json.append(json.load(file))

print(all_json[0])  # sample print Chiangmai

for x, y in all_json[0].items():
    print(x)

# html_attributions
# next_page_token
# results  <---- we want this key
# status

# step 1

a1 = []
a2 = []
a3 = []
a4 = []
a5 = []

# step 2

for dct in all_json:
    for d in dct['results']:
        a1.append(d['name'])
        a2.append(d['geometry']['location']['lat'])
        a3.append(d['geometry']['location']['lng'])
        a4.append(d['vicinity'])
        try:
            a5.append(d['plus_code']['compound_code'])
        except:
            a5.append("none")

# step 2
table = dict()

# step 2a
table['name'] = a1
table['lat'] = a2
table['lng'] = a3
table['vicinity'] = a4
table['city'] = a5

# step 3
df_table = pd.DataFrame(table)
