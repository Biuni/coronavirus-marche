import generate_json
import pandas as pd
import json
import glob
import csv

JSONfiles = glob.glob('../data/JSON/*.json')


def _object_to_rows(obj, prefix=None):
    rows = []
    dot_prefix = prefix and (prefix + "_") or ""
    if isinstance(obj, dict):
        if not obj:
            rows.append(((prefix or ""), "{}"))
        else:
            for key, item in obj.items():
                rows.extend(_object_to_rows(item, prefix=dot_prefix + key))
    elif isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            rows.extend(_object_to_rows(item, prefix=dot_prefix + str(i)))
    elif obj is None:
        rows.append(((prefix or ""), "None"))
    elif isinstance(obj, bool):
        rows.append(((prefix or ""), str(obj)))
    elif isinstance(obj, int):
        rows.append(((prefix or ""), str(obj)))
    elif isinstance(obj, float):
        rows.append(((prefix or ""), str(obj)))
    else:
        rows.append((prefix, str(obj)))
    return rows


def flatten(obj):
    return dict(_object_to_rows(obj))


def generate():

    data = {}
    data['report'] = []
    # Genero il JSON aggregato
    for json_file in JSONfiles:
        with open(json_file) as file:
            data['report'].append(json.load(file))

    # Apre il file CSV da scrivere
    with open('../covid-19-marche.csv', 'w', newline='') as csvfile:
        # Header del CSV
        csv_columns = list(dict([(x, y) for x, y in flatten(data['report'][0]).items() if not (
            x.startswith('decessi_odierni_dettaglio') or x.startswith('file_pdf'))]).keys())
        # Prepara il file per essere scritto
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        # Scrive l'header
        writer.writeheader()
        for value in data['report']:
            # Appiattisce il JSON
            flat_json = flatten(value)
            # Rimuove il dettaglio dei decessi e i collegamenti ai file PDF
            res_json = dict([(x, y) for x, y in flat_json.items() if not (
                x.startswith('decessi_odierni_dettaglio') or x.startswith('file_pdf'))])
            # Scrivo la riga del CSV
            writer.writerow(res_json)

    print('\n\033[92m- File "covid-19-marche.csv" generato!\033[0m')

    # Apre il file CSV da scrivere
    with open('../data/CSV/dettagli_decessi.csv', 'w', newline='') as csvfile:
        # Header del CSV
        csv_columns = [
            'id',
            'luogo_decesso',
            'sesso',
            'eta',
            'comune_domicilio',
            'provincia_domicilio',
            'pregresse_patologie',
            'data']
        # Prepara il file per essere scritto
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        # Scrive l'header
        writer.writeheader()
        for value in data['report']:
            data_report = value['data']
            for row in value['decessi']['odierni']['dettaglio']:
                row['data'] = data_report
                # Scrive la riga del CSV
                writer.writerow(row)

    print('\033[92m- File "dettagli_decessi.csv" generato!\033[0m')


if __name__ == '__main__':
    generate()
