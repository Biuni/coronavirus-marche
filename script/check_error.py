import json
import glob


JSONfiles = glob.glob('../data/JSON/*.json')


def print_error(id):
    error_desc = {
        0: 'Il PDF locale blu (file_pdf.locale.blu) deve corrispondere al corretto colore del report e alla corretta data.',
        1: 'Il PDF locale giallo (file_pdf.locale.giallo) deve corrispondere al corretto colore del report e alla corretta data.',
        2: 'Il PDF locale arancio (file_pdf.locale.arancio) deve corrispondere al corretto colore del report e alla corretta data.',
        3: 'Il numero di malati totali (malati.totali.persone) deve corrispondere alla somma dei malati per ogni provincia (malati.totali.provincia).',
        4: 'La somma dei pazienti in isolamento domicialiare (malati.attivi.isolamento_domiciliare) e dei ricoverati (malati.attivi.ricoverati.totali) deve essere uguale al totale degli attualmente positivi (malati.attivi.persone).',
        5: 'La somma dei ricoveri in terapia intensiva nelle varie strutture (malati.attivi.ricoverati.terapia_intensiva.strutture) deve essere uguale al totale delle terapie intensive (malati.attivi.ricoverati.terapia_intensiva.totali).',
        6: 'La somma dei ricoveri in terapia semi intensiva nelle varie strutture (malati.attivi.ricoverati.semi_intensiva.strutture) deve essere uguale al totale delle terapie semi intensive (malati.attivi.ricoverati.semi_intensiva.totali).',
        7: 'La somma dei ricoveri in terapia post critica nelle varie strutture (malati.attivi.ricoverati.post_critica.strutture) deve essere uguale al totale delle terapie post critiche (malati.attivi.ricoverati.post_critica.totali).',
        8: 'La somma dei ricoveri in terapia non intesiva nelle varie strutture (malati.attivi.ricoverati.non_intensiva.strutture) deve essere uguale al totale delle terapie non intesive (malati.attivi.ricoverati.non_intensiva.totali).',
        9: 'La somma delle persone sintomatiche (malati.quarantena_domiciliare.attivi.sintomatici) ed asintomatiche (malati.quarantena_domiciliare.attivi.asintomatici) in quarantena domiciliare deve essere uguale al totale degli attualmente in quarantena domiciliare (malati.quarantena_domiciliare.attivi.totali).',
        10: 'La somma delle persone sintomatiche (malati.quarantena_domiciliare.provincia.[KEY].attivi.sintomatici) ed asintomatiche (malati.quarantena_domiciliare.provincia.[KEY].attivi.asintomatici) in quarantena domiciliare deve essere uguale al totale degli attualmente in quarantena domiciliare (malati.quarantena_domiciliare.provincia.[KEY].attivi.totali), per ogni provincia.',
        11: 'La somma dei casi diagnosticati di oggi (tamponi.odierni.casi_diagnosticati) e del totale dei casi diagnosticati ieri ([-1].tamponi.totali.casi_diagnosticati) deve essere uguale al totale dei casi diagnosticati oggi (tamponi.totali.casi_diagnosticati).',
        12: 'La somma dei casi positivi di oggi (tamponi.odierni.casi_positivi) e del totale dei casi positivi di ieri ([-1].tamponi.totali.casi_positivi) deve essere uguale al totale dei casi positivi di oggi (tamponi.totali.casi_positivi).',
        13: 'La somma dei decessi per sesso (decessi.totali.sesso.maschio + decessi.totali.sesso.femmina) deve essere uguale alla somma totale dei decessi (decessi.totali.decessi).',
        14: 'La somma dei decessi per provincia (decessi.totali.provincia) deve essere uguale alla somma totale dei decessi (decessi.totali.decessi).',
        15: 'La somma dei decessi odierni (decessi.odierni.decessi) e del totale dei decessi di ieri ([-1].decessi.totali.decessi) deve essere uguale al totale dei decessi di oggi (decessi.totali.decessi).',
        16: 'Gli ID (decessi.odierni.dettaglio.[].id) dei decessi devono essere incrementali ed univoci.',
        17: 'Il dettaglio dei decessi (decessi.odierni.dettaglio) non deve avere valori vuoti o non consistenti (es: sesso diverso da M/F o patologie pregresse diverso da 0/1).',
        18: 'La somma del dettaglio dei decessi (decessi.odierni.dettaglio) deve corrispondere al numero di decessi odierni (decessi.odierni.decessi).'}
    return '\033[91mERROR!\033[0m\n\033[93m{}\033[0m'.format(
        error_desc.get(id))


def static_test():
    error = False
    check_id = []

    data = {}
    data['report'] = []
    # Genero il JSON aggregato
    for json_file in JSONfiles:
        with open(json_file) as file:
            data['report'].append(json.load(file))

    # Tamponi di partenza
    prec_1 = data['report'][0]['tamponi']['totali']['casi_diagnosticati'] - \
        data['report'][0]['tamponi']['odierni']['casi_diagnosticati']
    # Casi positivi di partenza
    prec_2 = data['report'][0]['tamponi']['totali']['casi_positivi'] - \
        data['report'][0]['tamponi']['odierni']['casi_positivi']
    # Decessi di partenza
    prec_3 = data['report'][0]['decessi']['totali']['decessi'] - \
        data['report'][0]['decessi']['odierni']['decessi']

    for value in data['report']:

        # Ogni file PDF deve corrispondere al corretto colore del report e alla
        # corretta data.
        if value['file_pdf']['locale']['blu'] != './data/PDF/GORES_Blu/' + \
                value['data'] + '.pdf' and value['file_pdf']['locale']['blu'] != '':
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(0))
        if value['file_pdf']['locale']['giallo'] != './data/PDF/GORES_Giallo/' + \
                value['data'] + '.pdf' and value['file_pdf']['locale']['giallo'] != '':
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(1))
        if value['file_pdf']['locale']['arancio'] != './data/PDF/GORES_Arancio/' + \
                value['data'] + '.pdf' and value['file_pdf']['locale']['arancio'] != '':
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(2))

        # Il numero di malati totali deve corrispondere alla somma dei malati
        # per ogni provincia.
        total_1 = 0
        provincie = value['malati']['totali']['provincia']
        for key in provincie:
            total_1 += provincie[key]
        if value['malati']['totali']['persone'] != total_1:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(3))

        # La somma dei pazienti in isolamento domicialiare e dei ricoverati
        # deve essere uguale al totale degli attualmente positivi.
        if value['malati']['attivi']['persone'] != value['malati']['attivi']['isolamento_domiciliare'] + \
                value['malati']['attivi']['ricoverati']['totali']:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(4))

        # La somma dei ricoveri nei vari reparti di terapia intensiva delle
        # varie strutture deve essere uguale al totale delle terapie intensive.
        total_2 = 0
        strutture = value['malati']['attivi']['ricoverati']['terapia_intensiva']['strutture']
        for key in strutture:
            total_2 += strutture[key]
        if value['malati']['attivi']['ricoverati']['terapia_intensiva']['totali'] != total_2:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(5))

        # La somma dei ricoveri nei vari reparti di terapia semi intensiva
        # delle varie strutture deve essere uguale al totale delle terapie semi
        # intensive.
        total_3 = 0
        strutture = value['malati']['attivi']['ricoverati']['semi_intensiva']['strutture']
        for key in strutture:
            total_3 += strutture[key]
        if value['malati']['attivi']['ricoverati']['semi_intensiva']['totali'] != total_3:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(6))

        # La somma dei ricoveri nei vari reparti di terapia semi intensiva
        # delle varie strutture deve essere uguale al totale delle terapie semi
        # intensive.
        total_4 = 0
        strutture = value['malati']['attivi']['ricoverati']['post_critica']['strutture']
        for key in strutture:
            total_4 += strutture[key]
        if value['malati']['attivi']['ricoverati']['post_critica']['totali'] != total_4:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(7))

        # La somma dei ricoveri nei vari reparti di terapia non intensiva delle
        # varie strutture deve essere uguale al totale delle terapie non
        # intensive.
        total_4 = 0
        strutture = value['malati']['attivi']['ricoverati']['non_intensiva']['strutture']
        for key in strutture:
            total_4 += strutture[key]
        if value['malati']['attivi']['ricoverati']['non_intensiva']['totali'] != total_4:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(8))

        # La somma delle persone sintomatiche ed asintomatiche in quarantena
        # domiciliare deve essere uguale al totale degli attualmente in
        # quarantena domiciliare.
        total_5 = value['malati']['quarantena_domiciliare']['attivi']['sintomatici'] + \
            value['malati']['quarantena_domiciliare']['attivi']['asintomatici']
        if value['malati']['quarantena_domiciliare']['attivi']['totali'] != total_5:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(9))

        # La somma delle persone sintomatiche ed asintomatiche in quarantena
        # domiciliare deve essere uguale al totale degli attualmente in
        # quarantena domiciliare, per ogni provincia.
        total_6 = 0
        quarantena = value['malati']['quarantena_domiciliare']['provincia']
        for key in quarantena:
            total_6 = quarantena[key]['attivi']['sintomatici'] + \
                quarantena[key]['attivi']['asintomatici']
            if value['malati']['quarantena_domiciliare']['provincia'][key]['attivi']['totali'] != total_6:
                error = True
                print(
                    '\nFile: %s.json' %
                    value['data'],
                    '=> Provincia di',
                    key.upper(),
                    '=>',
                    print_error(10))

        # La somma dei casi diagnosticati oggi e del totale dei casi
        # diagnosticati ieri deve essere uguale al totale dei casi
        # diagnosticati oggi.
        if value['tamponi']['totali']['casi_diagnosticati'] != prec_1 + \
                value['tamponi']['odierni']['casi_diagnosticati']:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(11))
        prec_1 = value['tamponi']['totali']['casi_diagnosticati']

        # La somma dei casi positivi oggi e del totale dei casi positivi ieri
        # deve essere uguale al totale dei casi positivi oggi.
        if value['tamponi']['totali']['casi_positivi'] != prec_2 + \
                value['tamponi']['odierni']['casi_positivi']:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(12))
        prec_2 = value['tamponi']['totali']['casi_positivi']

        # La somma dei decessi per sesso deve essere uguale alla somma totale
        # dei decessi.
        if value['decessi']['totali']['decessi'] != value['decessi']['totali']['sesso']['maschio'] + \
                value['decessi']['totali']['sesso']['femmina']:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(13))

        # La somma dei decessi per provincia deve essere uguale alla somma
        # totale dei decessi.
        total_7 = 0
        provincie = value['decessi']['totali']['provincia']
        for key in provincie:
            total_7 += provincie[key]
        if value['decessi']['totali']['decessi'] != total_7:
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(14))

        # La somma dei decessi odierni e del totale dei decessi di ieri deve
        # essere uguale al totale dei decessi di oggi.
        if (value['decessi']['totali']['decessi'] != prec_3 + value['decessi']
                ['odierni']['decessi']) and (value['data'] != '05-29-2020') and (value['data'] != '06-25-2020'):
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(15))
        prec_3 = value['decessi']['totali']['decessi']

        # Gli ID dei decessi devono essere incrementali.
        if len(value['decessi']['odierni']['dettaglio']) > 0:
            for get_id in value['decessi']['odierni']['dettaglio']:
                check_id.append(get_id['id'])
            if list(range(min(check_id), max(check_id) + 1)) != check_id:
                error = True
                print('\nFile: %s.json' % value['data'], '=>', print_error(16))

        # Il dettaglio dei decessi non deve avere valori vuoti o non
        # consistenti.
        for dead in value['decessi']['odierni']['dettaglio']:
            if (dead['luogo_decesso'] == '' or (dead['sesso'] != 'M' and dead['sesso'] != 'F' and dead['sesso'] != 'ND') or
                dead['comune_domicilio'] == '' or dead['provincia_domicilio'] == '' or
                    (dead['pregresse_patologie'] != 1 and dead['pregresse_patologie'] != 0 and dead['pregresse_patologie'] != -1)):
                error = True
                print('\nFile: %s.json' % value['data'], '=>', print_error(17))

        # La somma del dettaglio dei decessi deve corrispondere al numero di
        # decessi odierni.
        total_8 = 0
        for dead in value['decessi']['odierni']['dettaglio']:
            total_8 = total_8 + 1
        if (value['decessi']['odierni']['decessi'] != total_8):
            error = True
            print('\nFile: %s.json' % value['data'], '=>', print_error(18))

    # Se non è stato trovato nessun errore stampo l'output
    if not error:
        print('\n\033[92m- Nessun errore trovato!\033[0m')


if __name__ == '__main__':
    static_test()
