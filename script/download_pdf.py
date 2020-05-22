import urllib.request
import sys


class bcolors:
    HEADER = '\033[95m'
    BLU = '\033[94m'
    YELLOW = '\033[93m'
    ORANGE = '\033[91m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


gores_blu = (
    ("05-22-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu22052020_9.pdf"),
    ("05-21-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu21052020_9.pdf"),
    ("05-20-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu20052020_9.pdf"),
    ("05-19-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu19052020_9.pdf"),
    ("05-18-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu18052020_9.pdf"),
    ("05-17-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu17052020_9.pdf"),
    ("05-16-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu16052020_9.pdf"),
    ("05-15-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu15052020_9.pdf"),
    ("05-14-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu14052020_9.pdf"),
    ("05-13-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresblu13maggio.pdf"),
    ("05-12-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Goresblu12052020.pdf"),
    ("05-11-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu11052020_9.pdf"),
    ("05-10-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu10052020_9.pdf"),
    ("05-09-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu09052020_9.pdf"),
    ("05-08-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu08052020_9.pdf"),
    ("05-07-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu07052020_9.pdf"),
    ("05-06-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu06052020_9.pdf"),
    ("05-05-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu05052020_9.pdf"),
    ("05-04-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu04052020_9.pdf"),
    ("05-03-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu03052020_9.pdf"),
    ("05-02-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblus02052020_9.pdf"),
    ("05-01-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu01052020_9.pdf"),
    ("04-30-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu30042020_9.pdf"),
    ("04-29-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu29042020_9.pdf"),
    ("04-28-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu28042020_9.pdf"),
    ("04-27-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu27042020_9.pdf"),
    ("04-26-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu26042020_9.pdf"),
    ("04-25-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu25042020_9.pdf"),
    ("04-24-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu24042020_9.pdf"),
    ("04-23-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu23042020_9.pdf"),
    ("04-22-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu22042020_9.pdf"),
    ("04-21-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu21042020_9.pdf"),
    ("04-20-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu20042020_9.pdf"),
    ("04-19-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu19042020_9.pdf"),
    ("04-18-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu18042020_9.pdf"),
    ("04-17-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu17042020_9.pdf"),
    ("04-16-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu16042020_9.pdf"),
    ("04-15-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu15042020_9.pdf"),
    ("04-14-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu14042020_9.pdf"),
    ("04-13-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu13042020_9.pdf"),
    ("04-12-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu12042020_9.pdf"),
    ("04-11-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu11042020_9.pdf"),
    ("04-10-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu10042020_9.pdf"),
    ("04-09-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu09042020_9.pdf"),
    ("04-08-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu08042020_9.pdf"),
    ("04-07-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu07042020_9.pdf"),
    ("04-06-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu06042020_9.pdf"),
    ("04-05-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu05042020_9.pdf"),
    ("04-04-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu04042020_9.pdf"),
    ("04-03-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu03042020_9.pdf"),
    ("04-02-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESblu02042020_9.pdf"),
    ("04-01-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu01042020_9.pdf"),
    ("03-31-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu31032020_9.pdf"),
    ("03-30-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu30032020_9.pdf"),
    ("03-29-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu29032020_9.pdf"),
    ("03-28-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu28032020_9.pdf"),
    ("03-27-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu27032020_9.pdf"),
    ("03-26-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu26032020_9.pdf"),
    ("03-25-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu25032020_9.pdf"),
    ("03-24-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu24032020_9.pdf"),
    ("03-23-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Goresblu%2023032020.pdf"),
    ("03-22-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu22032020_9.pdf"),
    ("03-21-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu21032020_9.pdf"),
    ("03-20-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu20022020_9.pdf"),
    ("03-19-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES-blu-19032020_ore9.pdf"),
    ("03-18-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/17-03-2020%20schedaBluOre9.pdf"),
    ("03-17-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES%20BLU%2017-03%20progressione%20foglio%20di%20implementazione%20rev.pdf"),
    ("03-16-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_blu_16-03-2020_ore9.pdf"),
    ("03-15-2020.pdf", "http://www.regione.marche.it/Portals/0/Salute/Coronavirus/GORESblu15-03-2020_ore09.pdf"),
    ("03-14-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu14-03-2020_ore09.pdf"),
    ("03-13-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/progressione%20tamponi%20al%2013-03-20_ore9.pdf"),
    ("03-12-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESblu12-03-20_ore9.pdf")
)

gores_giallo = (
    ("05-22-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo22052020_12.pdf"),
    ("05-21-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo21maggio.pdf"),
    ("05-20-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo20maggio.pdf"),
    ("05-19-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo19maggio.pdf"),
    ("05-18-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo18maggio.pdf"),
    ("05-17-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo17052020_12.pdf"),
    ("05-16-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_schema_sintetico_monitoraggio_agg_16maggio_ore12.pdf"),
    ("05-15-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo15052020_12.pdf"),
    ("05-14-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo14maggio.pdf"),
    ("05-13-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo13052020_12.pdf"),
    ("05-12-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GoresGiallo12052020.pdf"),
    ("05-11-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo11maggio.pdf"),
    ("05-10-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo10052020_12.pdf"),
    ("05-09-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo9maggio.pdf"),
    ("05-08-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo08052020_12.pdf"),
    ("05-07-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo07052020_12.pdf"),
    ("05-06-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_schema_sintetico_monitoraggio_agg06-05-2020_ore12.pdf"),
    ("05-05-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresgiallo5maggio.pdf"),
    ("05-04-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo04052020_12.pdf"),
    ("05-03-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo03052020_12.pdf"),
    ("05-02-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo02052020_12.pdf"),
    ("05-01-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo01052020_12.pdf"),
    ("04-30-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESGIALLO30APRILE.pdf"),
    ("04-29-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_schema_sintetico_monitoraggio_agg_29aprile2020.pdf"),
    ("04-28-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo28042020_12.pdf"),
    ("04-27-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo27042020_12.pdf"),
    ("04-26-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo26042020_12.pdf"),
    ("04-25-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo25042020_12.pdf"),
    ("04-24-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_schema_sintetico_monitoraggio_agg_24aprile2020_ore12.pdf"),
    ("04-23-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo23042020_12.pdf"),
    ("04-22-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GoresGiallo22aprile.pdf"),
    ("04-21-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_schema_sintetico_monitoraggio_agg_21aprile2020.pdf"),
    ("04-20-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo20042020_12.pdf"),
    ("04-19-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo19042020_12.pdf"),
    ("04-18-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_schema_sintetico_monitoraggio_agg_18aprile2020.pdf"),
    ("04-17-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/2Report%20schema%20sintetico%20monitoraggio%20agg%2017%20aprile%202020.pdf"),
    ("04-16-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo16042020_12.pdf"),
    ("04-15-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/3Report%20schema%20sintetico%20monitoraggio%20agg%2015%20aprile%202020.xls.pdf"),
    ("04-14-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo14042020_12.pdf"),
    ("04-13-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo13042020_12.pdf"),
    ("04-12-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo12042020_12.pdf"),
    ("04-11-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo11042020_12.pdf"),
    ("04-10-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo10042020_12.pdf"),
    ("04-09-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GoresGiallo9Aprile.pdf"),
    ("04-08-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/corrReport_schema_sintetico_monitoraggio_agg_8_APRILE_2020.pdf"),
    ("04-07-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo07042020_12.pdf"),
    ("04-06-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo06042020_12.pdf"),
    ("04-05-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo05042020_12.pdf"),
    ("04-04-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo04042020_12.pdf"),
    ("04-03-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESgiallo03042020_12.pdf"),
    ("04-02-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/2Report%20schema%20sintetico%20monitoraggio%20agg%202%20APRILE%202020%20(3)(1).xls.pdf"),
    ("04-01-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo01042020_12.pdf"),
    ("03-31-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo31032020_12.pdf"),
    ("03-30-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Repport_schema_sintetico_monitoraggio_agg.30marzo2020.pdf"),
    ("03-29-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo29032020_12.pdf"),
    ("03-28-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_28marzo_schema_sintetico_monitoraggio_Marche_ORE_12.pdf"),
    ("03-27-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo27032020_12.pdf"),
    ("03-26-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Report%2026marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
    ("03-25-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Report%2025marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.xls.pdf"),
    ("03-24-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo24032020_12.pdf"),
    ("03-23-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo23032020_12.pdf"),
    ("03-22-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo22032020_12.pdf"),
    ("03-21-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo210320_12_agg.pdf"),
    ("03-20-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgiallo20032020_12.pdf"),
    ("03-19-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES-giallo-19032020_ore12.pdf"),
    ("03-18-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_giallo_18032020_ore12.pdf"),
    ("03-17-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/N%20report%2017%20marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
    ("03-16-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/report%2016%20marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
    ("03-15-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_gialla_15032020_ore12.pdf"),
    ("03-14-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgialla_14-03-20_ore12.pdf"),
    ("03-13-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/r%2013%20marzo%20schema%20sintetico%20monitoraggio%20Marche%20ORE%2012.pdf"),
    ("03-12-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESgialla120320_12.pdf"),
    ("03-11-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_110320_12.pdf"),
    ("03-10-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES10032020_1730.pdf"),
    ("03-09-2020.pdf", "http://www.regione.marche.it/Portals/0/Salute/Coronavirus/GORES_tabgialla09-03-2020_10.30.pdf"),
    ("03-08-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_tabGialla_08032020-1230.pdf"),
    ("03-07-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES%207%20marzo%20ore%2013%20Scheda%20Ufficiale%20monitoraggio.pdf"),
    ("03-06-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/06-03-2020%20gores%20ore%2010.pdf"),
    ("03-05-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/05-03-2020%20gores%20ore%2013.30.pdf")
)

gores_arancio = (
    ("05-22-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessi_COVID19_agg22maggio_ore18.pdf"),
    ("05-21-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Report_sint_decessi_COVID19_agg%2021maggio-ore18.pdf"),
    ("05-20-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessi_COVID19_agg20maggio_ore18.pdf"),
    ("05-19-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessi_COVID19_agg_19maggio-ore18.pdf"),
    ("05-18-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessi_COVID19_agg_18maggio2020_ore18.pdf"),
    ("05-17-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio17052020.pdf"),
    ("05-16-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio16052020_18.pdf"),
    ("05-15-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessiCOVID19_agg_15maggio_ore18.pdf"),
    ("05-14-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESARANCIO14052020.pdf"),
    ("05-13-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio13052020_18.pdf"),
    ("05-12-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio12052020_18.pdf"),
    ("05-11-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessi_COVID19_agg_11maggio2020_ore18.pdf"),
    ("05-10-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio10052020_18.pdf"),
    ("05-09-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio09052020_18.pdf"),
    ("05-08-2020.pdf", "https://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio08052020_18.pdf"),
    ("05-07-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio07052020_18.pdf"),
    ("05-06-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessi_COVID19_agg_06-05-2020.pdf"),
    ("05-05-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio05052020_18.pdf"),
    ("05-04-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio04052020_18.pdf"),
    ("05-03-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio03052020_18.pdf"),
    ("05-02-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio02052020_18.pdf"),
    ("05-01-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio01052020_18.pdf"),
    ("04-30-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio30042020_18.pdf"),
    ("04-29-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/decessi29aprile.pdf"),
    ("04-28-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/report_sint_decessi_COVID19_agg_28aprile2020ore18.pdf"),
    ("04-27-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/Report_sint_decessi_COVID19_agg_27aprile2020ore18.pdf"),
    ("04-26-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio26042020_18.pdf"),
    ("04-25-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio25042020_18.pdf"),
    ("04-24-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio24042020_18.pdf"),
    ("04-23-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio23042020_18.pdf"),
    ("04-22-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio22042020_18.pdf"),
    ("04-21-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio21042020_18.pdf"),
    ("04-20-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Report%20decessi%2020aprile.pdf"),
    ("04-19-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio19042020_18.pdf"),
    ("04-18-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio18042020_18.pdf"),
    ("04-17-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio17042020_18.pdf"),
    ("04-16-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio16042020_18.pdf"),
    ("04-15-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESARANCIO%2015042020.pdf"),
    ("04-14-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REPORT_sint_DECESSI_COVID19_aggiorn_14_APRILE_ore%2018.pdf"),
    ("04-13-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio13042020_18.pdf"),
    ("04-12-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio12042020_18.pdf"),
    ("04-11-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio11042020_18.pdf"),
    ("04-10-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Reportdecessi10aprile.pdf"),
    ("04-09-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REPORT_sint_DECESSI_COVID19_aggiorn_9_APRILE_ore_18.pdf"),
    ("04-08-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio08042020_18.pdf"),
    ("04-07-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/decessi7aprile.pdf"),
    ("04-06-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio06042020_18.pdf"),
    ("04-05-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio05042020_18.pdf"),
    ("04-04-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio04042020_18.pdf"),
    ("04-03-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/GORESarancio03042020_18.pdf"),
    ("04-02-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/2REP_sint_DECESSI_COVID19_aggiorn_2aprile_ore18.pdf"),
    ("04-01-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REPORT_sint_DECESSI_COVID19_aggiorn_1_APRILE_ore18.pdf"),
    ("03-31-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/DatiGORES/REP_sint_DECESSI_COVID19_aggiorn_31marzo_ore18.pdf"),
    ("03-30-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio30022020_18.pdf"),
    ("03-29-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio29032020_18.pdf"),
    ("03-28-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio28032020_18.pdf"),
    ("03-27-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio27032020_18.pdf"),
    ("03-26-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancione26032020_18.pdf"),
    ("03-25-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio25032020_18.pdf"),
    ("03-24-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/Goresarancio240320.pdf"),
    ("03-23-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio23032020_18.pdf"),
    ("03-22-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio22032020_18.pdf"),
    ("03-21-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio21032020_18.pdf"),
    ("03-20-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancio20032020_18_agg.pdf"),
    ("03-19-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/goresarancio190320_18.pdf"),
    ("03-18-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_arancione_18-03-2020_ore18_agg.pdf"),
    ("03-17-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_arancione_17032020_ore18.pdf"),
    ("03-16-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES-arancione_160320_ore18.pdf"),
    ("03-15-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORESarancione15032020_ore18.pdf"),
    ("03-14-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/GORES_arancione_14-03-2020_ore18.pdf"),
    ("03-13-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/13-03-2020%20TABELLA%20ARANCIONE%20-%20DECESSI.pdf"),
    ("03-12-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/12-03-2020%20TABELLA%20ARANCIONE%20DECESSI.pdf"),
    ("03-11-2020.pdf", "http://www.regione.marche.it/portals/0/Salute/CORONAVIRUS/11-03-2020%20TABELLA%20ARANCIONE%20-%20DECESSI.pdf")
)

n_argv = len(sys.argv)
color = None
day = None

if n_argv < 2:
    print('\n- Per scaricare tutti i report di un determinato colore, eseguire:')
    print(bcolors.HEADER + '\t$ py download_pdf.py -blu' + bcolors.ENDC)
    print(bcolors.HEADER + '\t$ py download_pdf.py -giallo' + bcolors.ENDC)
    print(bcolors.HEADER + '\t$ py download_pdf.py -arancio\n' + bcolors.ENDC)
    print('- Per scaricare uno specifico report, eseguire:')
    print(
        bcolors.HEADER +
        '\t$ py download_pdf.py -blu|-giallo|-arancio MM-DD-YYYY\n' +
        bcolors.ENDC)
    print(
        bcolors.UNDERLINE +
        'INFO: MM corrisponde al mese, DD al giorno e YYYY all\'anno.' +
        bcolors.ENDC)
elif n_argv == 2:
    color = sys.argv[1]
elif n_argv == 3:
    color = sys.argv[1]
    day = sys.argv[2]

if color == '-blu' and color is not None:
    for x in gores_blu:
        if day == x[0][:-4] or day is None:
            urllib.request.urlretrieve(x[1], '../data/PDF/GORES_Blu/' + x[0])
            print('- ' + bcolors.BLU + 'Report Blu' +
                  bcolors.ENDC + ' del ' + x[0][:-4] + ' scaricato!')
elif color == '-giallo' and color is not None:
    for x in gores_giallo:
        if day == x[0][:-4] or day is None:
            urllib.request.urlretrieve(
                x[1], '../data/PDF/GORES_Giallo/' + x[0])
            print('- ' + bcolors.YELLOW + 'Report Giallo' +
                  bcolors.ENDC + ' del ' + x[0][:-4] + ' scaricato!')
elif color == '-arancio' and color is not None:
    for x in gores_arancio:
        if day == x[0][:-4] or day is None:
            urllib.request.urlretrieve(
                x[1], '../data/PDF/GORES_Arancio/' + x[0])
            print('- ' + bcolors.ORANGE + 'Report Arancio' +
                  bcolors.ENDC + ' del ' + x[0][:-4] + ' scaricato!')
