
import random
from ascii import *




praeitas_ilgis = 0
file_obj = open("zodziu_sarasas.txt", "r")

for zodis in file_obj.readlines():
    ilgiausias_zodis = len(zodis[:-1])
    if praeitas_ilgis < ilgiausias_zodis:
        praeitas_ilgis = ilgiausias_zodis

def lygio_nustatymas():
    file_obj = open("zodziu_sarasas.txt", "r")
    lygis = input("ivesk zaidimo lygi 2-{} ".format(praeitas_ilgis))
    zodziu_sarasas = []
    for zodis in file_obj.readlines():
        zodzio_ilgis = len(zodis[:-1])
        if zodzio_ilgis == lygis:
            zodziu_sarasas.append(zodis[:-1])
    zodis_kuri_reikia_atspeti = random.choice(zodziu_sarasas)
    print zodis_kuri_reikia_atspeti
    return zodis_kuri_reikia_atspeti


spejimu_listas = list()
zodis_neatspetas = True
def zaidimas(zodis_kuri_reikia_atspeti):
    suklydimu_kartai = 0
    leidimas_suklysti = 1
    pasleptas_zodis = "_" * len(zodis_kuri_reikia_atspeti)
    print pasleptas_zodis
    kiek_kartu_suklys = input("kiek kartu nori suklysti? nuo 3 iki 6 ")
    while kiek_kartu_suklys < 3 and kiek_kartu_suklys < 6:
        kiek_kartu_suklys = input("bloga reiksme, ivesk nuo 3 iki 6 ")
    print kiek_kartu_suklys
    print HANGMANPICS[6-kiek_kartu_suklys]
    while zodis_neatspetas:
        if suklydimu_kartai == kiek_kartu_suklys:
            print "Game over"
            kartojimas = raw_input("Ar noresi kartoti zaidima? y/n")
            if kartojimas == "y":
                zodis_kuri_reikia_atspeti = lygio_nustatymas()
                zaidimas(zodis_kuri_reikia_atspeti)
            else:
                quit()
        raide_kuria_reikia_atspeti = raw_input("spek raide ")
        if raide_kuria_reikia_atspeti.isdigit() == True:
            print "tai ne raide, ivesk rade"
        else:
            spejimu_listas.append(raide_kuria_reikia_atspeti)
            spejimu_listas_naujas = spejimu_listas[:-1]
            for i in spejimu_listas_naujas:
                if i == raide_kuria_reikia_atspeti and leidimas_suklysti == 1:
                    print "suklydai! raide {} jau spejai, si karta dovanosim".format(raide_kuria_reikia_atspeti)
                    suklydimu_kartai = suklydimu_kartai - 1
                    leidimas_suklysti = leidimas_suklysti - 1
            if raide_kuria_reikia_atspeti in zodis_kuri_reikia_atspeti:
                paslepto_zodzio_listas = list(pasleptas_zodis)
                for index, raide in enumerate(zodis_kuri_reikia_atspeti):
                    if raide == raide_kuria_reikia_atspeti:
                        paslepto_zodzio_listas[index] = raide_kuria_reikia_atspeti
                        pasleptas_zodis = "".join(paslepto_zodzio_listas)
                        print "atspejai rade", pasleptas_zodis
            else:
                print "rades nera"
                suklydimu_kartai = suklydimu_kartai + 1
                print suklydimu_kartai, "kiek kartu suklydo"
                print kiek_kartu_suklys, "kiek karto nosi suklysti"
                paveikslelis = 6 - kiek_kartu_suklys + suklydimu_kartai

                print HANGMANPICS[paveikslelis]
                if kiek_kartu_suklys == suklydimu_kartai:
                    print "Game over"
                    kartojimas = raw_input("Ar noresi kartoti zaidima? y/n")
                    if kartojimas == "y":
                        zodis_kuri_reikia_atspeti = lygio_nustatymas()
                        zaidimas(zodis_kuri_reikia_atspeti)
                    else:
                        quit()
            if pasleptas_zodis == zodis_kuri_reikia_atspeti:
                print "zaidimas baigtas"
                kartojimas = raw_input("Ar noresi kartoti zaidima? y/n")
                if kartojimas == "y":
                    zodis_kuri_reikia_atspeti = lygio_nustatymas()
                    zaidimas(zodis_kuri_reikia_atspeti)
                else:
                    quit()

zodis_kuri_reikia_atspeti = lygio_nustatymas()
zaidimas(zodis_kuri_reikia_atspeti)