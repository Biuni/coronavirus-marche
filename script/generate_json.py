import glob
import json
import os

JSONfiles = glob.glob('../data/JSON/*.json')

data = {}
data['report'] = []

def generate(out=True):
	for json_file in JSONfiles:
		print('Inserito: '+ os.path.basename(json_file)) if out else None
		with open(json_file) as file:
			data['report'].append(json.load(file))

	with open('../covid-19-marche.json', 'w') as outfile:
			json.dump(data, outfile, indent=2)
			print('\nFile "covid-19-marche.json" generato!')

if __name__ == '__main__':
	generate()