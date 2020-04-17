import glob
import json
import os

JSONfiles = glob.glob('../data/JSON/*.json')

data = {}
data['report'] = []

for json_file in JSONfiles:
	print('Read: '+ os.path.basename(json_file))
	with open(json_file) as file:
		data['report'].append(json.load(file))

with open('../covid-19-marche.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
    print('File written!')