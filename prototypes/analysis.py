import json
import pandas as pd

# load json into python, assign bangkok.json to 'bkk'

with open('bangkok.json') as file:
    bkk = json.load(file)


# Exploring bkk dictionary

len(bkk)  # 4
type(bkk)  # dict

# key + value pairs in the dictionary

# html_attributions
# next_page_token
# results
# status

# NOTE: all content of interest is stored in the
# 'results' key
for x, y in bkk.items():
    print(x)

type(bkk['results'])  # list of dictionaries
len(bkk['results'])   # 20

# loop through list of 20 dict (in bkk['results'])
# for each dict, print out the key
for d in bkk['results']:
    for x, y in d.items():
        print(x)

# KEY values

# business_status
# geometry
# icon
# name
# opening_hours
# place_id
# plus_code
# rating
# reference
# scope
# types
# user_ratings_total
# vicinity

# Print specific Keys
for d in bkk['results']:
    print(d['name'], d['geometry']['location']['lat'],
          d['geometry']['location']['lng'], d['vicinity'])

# NEED TO FIGURE OUT ---> d['plus_code']['compound_code'],

# To convert necessary information into data frame
# step 1: create 4 lists
# step 1a: execute loop & append to empty lists
# step 2: create dictionary
# step 2a: append dictionary with 4 corresponding list
# step 3: convert dictionary into dataframe

# step 1

a1 = []
a2 = []
a3 = []
a4 = []


# step 1a
for d in bkk['results']:
    a1.append(d['name'])
    a2.append(d['geometry']['location']['lat'])
    a3.append(d['geometry']['location']['lng'])
    a4.append(d['vicinity'])

# step 2
table = dict()

# step 2a
table['name'] = a1
table['lat'] = a2
table['lng'] = a3
table['vicinity'] = a4

# step 3
df_table = pd.DataFrame(table)
