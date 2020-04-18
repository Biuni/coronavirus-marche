import json

error = False

def print_error(id):
  error_desc = {
    0:  'Il PDF locale blu (file_pdf.locale.blu) deve corrispondere al corretto colore del report e alla corretta data.',
    1:  'Il PDF locale giallo (file_pdf.locale.giallo) deve corrispondere al corretto colore del report e alla corretta data.',
    2:  'Il PDF locale arancio (file_pdf.locale.arancio) deve corrispondere al corretto colore del report e alla corretta data.',
    3:  'Il numero di malati totali (malati.totali.persone) deve corrispondere alla somma dei malati per ogni provincia (malati.totali.provincia).',
    4:  'La somma dei pazienti in isolamento domicialiare (malati.attivi.isolamento_domiciliare) e dei ricoverati (malati.attivi.ricoverati.totali) deve essere uguale al totale degli attualmente positivi (malati.attivi.persone).',
    5:  'La somma dei ricoveri in terapia intensiva nelle varie strutture (malati.attivi.ricoverati.terapia_intensiva.strutture) deve essere uguale al totale delle terapie intensive (malati.attivi.ricoverati.terapia_intensiva.totali).',
    6:  'La somma dei ricoveri in terapia semi intensiva nelle varie strutture (malati.attivi.ricoverati.semi_intensiva.strutture) deve essere uguale al totale delle terapie semi intensive (malati.attivi.ricoverati.semi_intensiva.totali).',
    7:  'La somma dei ricoveri in terapia post critica nelle varie strutture (malati.attivi.ricoverati.post_critica.strutture) deve essere uguale al totale delle terapie post critiche (malati.attivi.ricoverati.post_critica.totali).',
    8:  'La somma dei ricoveri in terapia non intesiva nelle varie strutture (malati.attivi.ricoverati.non_intensiva.strutture) deve essere uguale al totale delle terapie non intesive (malati.attivi.ricoverati.non_intensiva.totali).',
    9:  'La somma delle persone sintomatiche (malati.quarantena_domiciliare.attivi.sintomatici) ed asintomatiche (malati.quarantena_domiciliare.attivi.asintomatici) in quarantena domiciliare deve essere uguale al totale degli attualmente in quarantena domiciliare (malati.quarantena_domiciliare.attivi.totali).',
    10: 'La somma delle persone sintomatiche (malati.quarantena_domiciliare.provincia.[KEY].attivi.sintomatici) ed asintomatiche (malati.quarantena_domiciliare.provincia.[KEY].attivi.asintomatici) in quarantena domiciliare deve essere uguale al totale degli attualmente in quarantena domiciliare (malati.quarantena_domiciliare.provincia.[KEY].attivi.totali), per ogni provincia.'
  }
  return '\033[91mERROR!\033[0m\n\033[93m{}\033[0m'.format(error_desc.get(id))

with open('../covid-19-marche.json') as file:
  data = json.load(file)

for value in data['report']:

  # Ogni file PDF deve corrispondere al corretto colore del report e alla corretta data.
  if value['file_pdf']['locale']['blu'] != './data/PDF/GORES_Blu/'+value['data']+'.pdf':
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(0))
  if value['file_pdf']['locale']['giallo'] != './data/PDF/GORES_Giallo/'+value['data']+'.pdf':
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(1))
  if value['file_pdf']['locale']['arancio'] != './data/PDF/GORES_Arancio/'+value['data']+'.pdf':
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(2))

  # Il numero di malati totali deve corrispondere alla somma dei malati per ogni provincia.
  total_1 = 0
  provincie = value['malati']['totali']['provincia']
  for key in provincie:
      total_1 += provincie[key]
  if value['malati']['totali']['persone'] != total_1:
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(3))

  # La somma dei pazienti in isolamento domicialiare e dei ricoverati deve essere uguale al totale degli attualmente positivi.
  if value['malati']['attivi']['persone'] != value['malati']['attivi']['isolamento_domiciliare'] + value['malati']['attivi']['ricoverati']['totali']:
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(4))

  # La somma dei ricoveri nei vari reparti di terapia intensiva delle varie strutture deve essere uguale al totale delle terapie intensive.
  total_2 = 0
  strutture = value['malati']['attivi']['ricoverati']['terapia_intensiva']['strutture']
  for key in strutture:
      total_2 += strutture[key]
  if value['malati']['attivi']['ricoverati']['terapia_intensiva']['totali'] != total_2:
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(5))

  # La somma dei ricoveri nei vari reparti di terapia semi intensiva delle varie strutture deve essere uguale al totale delle terapie semi intensive.
  total_3 = 0
  strutture = value['malati']['attivi']['ricoverati']['semi_intensiva']['strutture']
  for key in strutture:
      total_3 += strutture[key]
  if value['malati']['attivi']['ricoverati']['semi_intensiva']['totali'] != total_3:
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(6))

  # La somma dei ricoveri nei vari reparti di terapia semi intensiva delle varie strutture deve essere uguale al totale delle terapie semi intensive.
  total_4 = 0
  strutture = value['malati']['attivi']['ricoverati']['post_critica']['strutture']
  for key in strutture:
      total_4 += strutture[key]
  if value['malati']['attivi']['ricoverati']['post_critica']['totali'] != total_4:
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(7))

  # La somma dei ricoveri nei vari reparti di terapia non intensiva delle varie strutture deve essere uguale al totale delle terapie non intensive.
  total_4 = 0
  strutture = value['malati']['attivi']['ricoverati']['non_intensiva']['strutture']
  for key in strutture:
      total_4 += strutture[key]
  if value['malati']['attivi']['ricoverati']['non_intensiva']['totali'] != total_4:
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(8))

  # La somma delle persone sintomatiche ed asintomatiche in quarantena domiciliare deve essere uguale al totale degli attualmente in quarantena domiciliare.
  total_5 = value['malati']['quarantena_domiciliare']['attivi']['sintomatici'] + value['malati']['quarantena_domiciliare']['attivi']['asintomatici']
  if value['malati']['quarantena_domiciliare']['attivi']['totali'] != total_5:
    error = True
    print('\nFile: %s.json' % value['data'], '=>', print_error(9))

  # La somma delle persone sintomatiche ed asintomatiche in quarantena domiciliare deve essere uguale al totale degli attualmente in quarantena domiciliare, per ogni provincia.
  total_6 = 0
  quarantena = value['malati']['quarantena_domiciliare']['provincia']
  for key in quarantena:
    total_6 = quarantena[key]['attivi']['sintomatici'] + quarantena[key]['attivi']['asintomatici']
    if value['malati']['quarantena_domiciliare']['provincia'][key]['attivi']['totali'] != total_6:
      error = True
      print('\nFile: %s.json' % value['data'], '=> Provincia di', key.upper(), '=>' , print_error(10))

if not error:
  print('\n\033[92mNessun errore trovato!\033[0m')