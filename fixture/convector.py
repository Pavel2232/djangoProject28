# importing the required libraries 
import csv
import json




# defining the function to convert CSV file to JSON file
def convjson(csvFilename, jsonFilename,model):
    # creating a dictionary
    mydata = []


    # reading the data from CSV file
    with open(csvFilename, encoding='utf-8') as csvfile:
        csvRead = csv.DictReader(csvfile)

        # Converting rows into dictionary and adding it to data
        for row in csvRead:
            to_add = {'model':model, 'pk': int(row['Id'])}
            if 'Id' in row:
                del row['Id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            mydata.append(to_add)


            # dumping the data
        with open(jsonFilename, 'w', encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(mydata, indent=4,ensure_ascii= False))

# filenames


csvAds = r'ads.csv'
jsonAds = r'ads.json'

csvCatigories = r'categories.csv'
jsonCatigories = r'categories.json'


# Calling the convjson function


convjson(csvAds, jsonAds, 'ads.ad')
convjson(csvCatigories, jsonCatigories, 'categories.categorie')
