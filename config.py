# -*-coding:Latin-1 -*
from Fkanban.Fkanban import *
from Fkanban.ui_Fkanban import *
from FUTIL.my_logging import *

olfa = place("Olfa") # not use!!!

from tkinter import *

impression = workshop("Impression")
impregnation = workshop("Impregnation")
presses = workshop("Presses")
montage = workshop("Montage")
peinture = workshop("Peinture")
expeditions = workshop("Expeditions")

AR1146SM = item("7AR1179SM",\
	[ operation(impression,[], "IMPRESSION DECORS 1179 SIEGE", 5, 8), \
	  operation(impregnation, [], "IMPREGNATION DECORS 1179 SIEGE", 60, 4 ), \
	  operation(presses, [], "PRESSE SIEGE DECORS 1179", 12, 4), \
	  operation(peinture, [], "PEINTURE MAT", 720, 10)])
	  
AR1146SM_l = fab_kloop(name = "7AR1179SM", item = AR1146SM, batch = 12, customer_shop = montage, kanbans_nb = 2, kanbans_qty = 6, red_zone = 1)

AR1146CM = item("7AR1179CM",\
	[ operation(impression,[], "IMPRESSION DECORS 1179 COUV", 5, 8), \
	  operation(impregnation, [], "IMPREGNATION DECORS 1179 COUV", 60, 4 ), \
	  operation(presses, [], "PRESSE COUV DECORS 1179", 12, 4), \
	  operation(peinture, [], "PEINTURE MAT", 720, 10)])
AR1146CM_l = fab_kloop(name = "7AR1179CM", item = AR1146CM, batch = 12, customer_shop = montage, kanbans_nb = 2, kanbans_qty = 6, red_zone = 1)

#AR1179 NDA
AR11790701 = item("7AR11790701", \
	[operation(montage,[nomenclature_link(AR1146SM,1), \
						nomenclature_link(AR1146CM, 1)], \
						"Montage AR11790701",50, .25)])
AR11790701_l = fab_kloop(name = "7AR11790701", item = AR11790701, batch = 1, customer_shop = expeditions, kanbans_nb = 1, kanbans_qty = 1)

sorties_AR11790701 = item("Expeditions", [operation(expeditions, [nomenclature_link(AR11790701,1)], "Conso :")])
sorties_AR11790701_l = customer_kloop(name = "Conso AR11790701", item = sorties_AR11790701, workshop = expeditions, period = 8, qty = 6, period_alea_rate = 0.1, qty_alea_range = .9)

# AR1179 DA
AR11794101 = item("7AR11794101", \
	[operation(montage,[nomenclature_link(AR1146SM,1), \
						nomenclature_link(AR1146CM, 1)], \
						"Montage AR117941²01",50, .25)])
AR11794101_l = fab_kloop(name = "7AR11794101", item = AR11794101, batch = 1, customer_shop = expeditions, kanbans_nb = 1, kanbans_qty = 1)

sorties_AR11794101 = item("Expeditions", [operation(expeditions, [nomenclature_link(AR11794101,1)], "Conso :")])
sorties_AR11794101_l = customer_kloop(name = "Conso AR11794101", item = sorties_AR11794101, workshop = expeditions, period = 8, qty = 5, period_alea_rate = 0.1, qty_alea_range = .9)

mes_ateliers = [impression, impregnation, presses, peinture, montage]


logging.debug("Creation of loops ...")

mes_boucles = [AR1146SM_l, AR1146CM_l, AR11790701_l,sorties_AR11790701_l,AR11794101_l,sorties_AR11794101_l]


app = ui_Fkanban(mes_ateliers, mes_boucles, speed = 15, multi_tk = False)
