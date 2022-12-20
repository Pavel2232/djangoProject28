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
            to_add = {'model':model, 'pk': int(row['id'])}
            if 'id' in row:
                del row['id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'price' in row:
                row['price'] = int(row['price'])

            if 'age' in row:
                row['age'] = int(row['age'])

            if 'lat' in row:
                row['lat'] = float(row['lat'])

            if 'lng' in row:
                row['lng'] = float(row['lng'])

            if 'author_id' in row:
                row['author_id'] = int(row['author_id'])

            if 'category_id' in row:
                row['category_id'] = int(row['category_id'])

            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']


            to_add['fields'] = row
            mydata.append(to_add)


            # dumping the data
        with open(jsonFilename, 'w', encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(mydata, indent=4,ensure_ascii= False))

# filenames


csvAd = r'ad.csv'
jsonAd = r'ad.json'

csvCat = r'category.csv'
jsonCat = r'category.json'

csvLocation = r'location.csv'
jsonLocation = r'location.json'

csvUser = r'user.csv'
jsonUser = r'user.json'


# Calling the convjson function


convjson(csvAd, jsonAd, 'ads.ad')
convjson(csvCat, jsonCat, 'categories.categorie')
convjson(csvLocation, jsonLocation, 'location.location')
convjson(csvUser, jsonUser, 'user.user')
