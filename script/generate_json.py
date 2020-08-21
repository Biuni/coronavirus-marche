import glob
import json

JSONfiles = glob.glob('../data/JSON/*.json')

data = {}
data['report'] = []


def generate(out=True):
    for json_file in JSONfiles:
        with open(json_file) as file:
            data['report'].append(json.load(file))

    with open('../covid-19-marche.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)
        print('\n\033[92m- File "covid-19-marche.json" generato!\033[0m') if out else None


if __name__ == '__main__':
    generate()
