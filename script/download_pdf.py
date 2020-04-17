import urllib.request
import sys

gores_blu = (
	("04_17_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu17042020_9.pdf"),
	("04_16_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu16042020_9.pdf"),
	("04_15_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu15042020_9.pdf"),
	("04_14_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu14042020_9.pdf"),
	("04_13_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu13042020_9.pdf"),
	("04_12_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu12042020_9.pdf"),
	("04_11_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu11042020_9.pdf"),
	("04_10_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu10042020_9.pdf"),
	("04_09_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu09042020_9.pdf"),
	("04_08_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu08042020_9.pdf"),
	("04_07_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu07042020_9.pdf"),
	("04_06_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu06042020_9.pdf"),
	("04_05_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu05042020_9.pdf"),
	("04_04_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu04042020_9.pdf"),
	("04_03_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu03042020_9.pdf"),
	("04_02_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu02042020_9.pdf"),
	("04_01_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu01042020_9.pdf"),
	("03_31_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu31032020_9.pdf"),
	("03_30_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu30032020_9.pdf"),
	("03_29_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu29032020_9.pdf"),
	("03_28_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu28032020_9.pdf"),
	("03_27_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu27032020_9.pdf"),
	("03_26_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu26032020_9.pdf"),
	("03_25_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu25032020_9.pdf"),
	("03_24_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu24032020_9.pdf"),
	("03_23_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Goresblu%2023032020.pdf"),
	("03_22_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu22032020_9.pdf"),
	("03_21_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu21032020_9.pdf"),
	("03_20_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu20022020_9.pdf"),
	("03_19_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES-blu-19032020_ore9.pdf"),
	("03_18_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/17-03-2020%20schedaBluOre9.pdf"),
	("03_17_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES%20BLU%2017-03%20progressione%20foglio%20di%20implementazione%20rev.pdf"),
	("03_16_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_blu_16-03-2020_ore9.pdf"),
	("03_15_2020.pdf", "http://www.regione.marche.it/Portals/0/Salute/Coronavirus/GORESblu15-03-2020_ore09.pdf"),
	("03_14_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu14-03-2020_ore09.pdf"),
	("03_13_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/progressione%20tamponi%20al%2013-03-20_ore9.pdf"),
	("03_12_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu12-03-20_ore9.pdf")
)

gores_giallo = (
	("04_17_2020.pdf", ""),
	("04_16_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo16042020_12.pdf"),
	("04_15_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/3Report%20schema%20sintetico%20monitoraggio%20agg%2015%20aprile%202020.xls.pdf"),
	("04_14_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo14042020_12.pdf"),
	("04_13_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo13042020_12.pdf"),
	("04_12_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo12042020_12.pdf"),
	("04_11_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo11042020_12.pdf"),
	("04_10_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo10042020_12.pdf"),
	("04_09_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GoresGiallo9Aprile.pdf"),
	("04_08_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/corrReport_schema_sintetico_monitoraggio_agg_8_APRILE_2020.pdf"),
	("04_07_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo07042020_12.pdf"),
	("04_06_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo06042020_12.pdf"),
	("04_05_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo05042020_12.pdf"),
	("04_04_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo04042020_12.pdf"),
	("04_03_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo03042020_12.pdf"),
	("04_02_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/2Report%20schema%20sintetico%20monitoraggio%20agg%202%20APRILE%202020%20(3)(1).xls.pdf"),
	("04_01_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo01042020_12.pdf"),
	("03_31_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo31032020_12.pdf"),
	("03_30_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Repport_schema_sintetico_monitoraggio_agg.30marzo2020.pdf"),
	("03_29_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo29032020_12.pdf"),
	("03_28_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_28marzo_schema_sintetico_monitoraggio_Marche_ORE_12.pdf"),
	("03_27_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo27032020_12.pdf"),
	("03_26_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Report%2026marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
	("03_25_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Report%2025marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.xls.pdf"),
	("03_24_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo24032020_12.pdf"),
	("03_23_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo23032020_12.pdf"),
	("03_22_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo22032020_12.pdf"),
	("03_21_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo210320_12_ag"),
	("03_20_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo20032020_12.pdf"),
	("03_19_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES-giallo-19032020_ore12.pdf"),
	("03_18_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_giallo_18032020_ore12.pdf"),
	("03_17_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/N%20report%2017%20marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
	("03_16_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/report%2016%20marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
	("03_15_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_gialla_15032020_ore12.pdf"),
	("03_14_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgialla_14-03-20_ore12.pdf"),
	("03_13_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/r%2013%20marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
	("03_12_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgialla120320_12.pdf"),
	("03_11_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_110320_12.pdf"),
	("03_10_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES10032020_1730.pdf"),
	("03_09_2020.pdf", "http://www.regione.marche.it/Portals/0/Salute/Coronavirus/GORES_tabgialla09-03-2020_10.30.pdf"),
	("03_08_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_tabGialla_08032020-1230.pdf"),
	("03_07_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES%207%20marzo%20ore%2013%20Scheda%20Ufficiale%20monitoraggio.pdf"),
	("03_06_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/06-03-2020%20gores%20ore%2010.pdf"),
	("03_05_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/05-03-2020%20gores%20ore%2013.30.pdf")
)

gores_arancio = (
	("04_17_2020.pdf", ""),
	("04_16_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio16042020_18.pdf"),
	("04_15_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESARANCIO%2015042020.pdf"),
	("04_14_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REPORT_sint_DECESSI_COVID19_aggiorn_14_APRILE_ore%2018.pdf"),
	("04_13_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio13042020_18.pdf"),
	("04_12_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio12042020_18.pdf"),
	("04_11_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio11042020_18.pdf"),
	("04_10_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Reportdecessi10aprile.pdf"),
	("04_09_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REPORT_sint_DECESSI_COVID19_aggiorn_9_APRILE_ore_18.pdf"),
	("04_08_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio08042020_18.pdf"),
	("04_07_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/decessi7aprile.pdf"),
	("04_06_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio06042020_18.pdf"),
	("04_05_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio05042020_18.pdf"),
	("04_04_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio04042020_18.pdf"),
	("04_03_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio03042020_18.pdf"),
	("04_02_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/2REP_sint_DECESSI_COVID19_aggiorn_2aprile_ore18.pdf"),
	("04_01_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REPORT_sint_DECESSI_COVID19_aggiorn_1_APRILE_ore18.pdf"),
	("03_31_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REP_sint_DECESSI_COVID19_aggiorn_31marzo_ore18.pdf"),
	("03_30_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio30022020_18.pdf"),
	("03_29_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio29032020_18.pdf"),
	("03_28_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio28032020_18.pdf"),
	("03_27_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio27032020_18.pdf"),
	("03_26_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancione26032020_18.pdf"),
	("03_25_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio25032020_18.pdf"),
	("03_24_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Goresarancio240320.pdf"),
	("03_23_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio23032020_18.pdf"),
	("03_22_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio22032020_18.pdf"),
	("03_21_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio21032020_18.pdf"),
	("03_20_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio20032020_18_agg.pdf"),
	("03_19_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresarancio190320_18.pdf"),
	("03_18_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_arancione_18-03-2020_ore18_agg.pdf"),
	("03_17_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_arancione_17032020_ore18.pdf"),
	("03_16_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES-arancione_160320_ore18.pdf"),
	("03_15_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancione15032020_ore18.pdf"),
	("03_14_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_arancione_14-03-2020_ore18.pdf"),
	("03_13_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/13-03-2020%20TABELLA%20ARANCIONE%20-%20DECESSI.pdf"),
	("03_12_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/12-03-2020%20TABELLA%20ARANCIONE%20DECESSI.pdf"),
	("03_11_2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/11-03-2020%20TABELLA%20ARANCIONE%20-%20DECESSI.pdf")
)

if sys.argv[1] == '-blu':
	for x in gores_blu:
		print('Download PDF Blu del: ' + x[0][:-4])
		urllib.request.urlretrieve(x[1], '../data/PDF/GORES_Blu/'+x[0])
elif sys.argv[1] == '-giallo':
	for x in gores_giallo:
		print('Download PDF Giallo del: ' + x[0][:-4])
		urllib.request.urlretrieve(x[1], '../data/PDF/GORES_Giallo/'+x[0])
elif sys.argv[1] == '-arancio':
	for x in gores_arancio:
		print('Download PDF Arancio del: ' + x[0][:-4])
		urllib.request.urlretrieve(x[1], '../data/PDF/GORES_Arancio/'+x[0])
else:
	print('\n- Eseguire lo script con un parametro specifico: -blu | -giallo | -arancio')