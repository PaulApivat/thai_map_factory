import json

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
    print(d['name'], d['geometry']['location'], d['vicinity'])
