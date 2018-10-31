# CSV to Json
import csv, json

csvFilePath = "csvfile.csv"
jsonFilePath = "jsonfile.json"

# Read the csv and add the data to a dictionary
data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        keyid = csvRow("keyid")
        data[keyid] = csvRow


#Add data to a rood node
root = {}
root["rootnode"] = data

# Write data to a JSON file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(root, indent = 4))