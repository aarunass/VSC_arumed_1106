
import random
from ascii import *

praeitas_ilgis = 0

#zodziu sarasas is failo:
file_obj = open("zodziu_sarasas.txt", "r")

for zodis in file_obj.readlines():
    ilgiausias_zodis = len(zodis[:-1])
    if praeitas_ilgis < ilgiausias_zodis:
        praeitas_ilgis = ilgiausias_zodis

def lygio_nustatymas():
    file_obj = open("zodziu_sarasas.txt", "r")
    lygis = 0
    a = True
    while a:
        if 2 <= lygis <= praeitas_ilgis:
            a = False
        else:
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
    vienodu_raidziu_skaicius = 0
    pasleptas_zodis = "_" * len(zodis_kuri_reikia_atspeti)
    print pasleptas_zodis

    #zaidejas turi pasirinkt kiek kartu jis suklys (nuo 3 iki 6):
    a = True
    kiek_kartu_suklys = 0
    while a:
        if 3 <= kiek_kartu_suklys <= 6:
            a = False
        else:
            kiek_kartu_suklys = input("ivesk nuo 3 iki 6 ")
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
        #zaidejas negali ivesti skaiciu spejant raide:
        raide_kuria_reikia_atspeti = raw_input("spek raide ")
        if raide_kuria_reikia_atspeti.isdigit() == True:    #This method returns true if all characters in the string are digits and there is at least one character, false otherwise.
            print "tai ne raide, ivesk rade"
        else:
            spejimu_listas.append(raide_kuria_reikia_atspeti)
            #Programa turi leisti zaidejui suklysti viena karta spejant raide kuria jau spejo:
            spejimu_listas_naujas = spejimu_listas[:-1]
            for i in spejimu_listas_naujas:
                if i == raide_kuria_reikia_atspeti and leidimas_suklysti == 1:
                    print "suklydai! raide {} jau spejai, si karta dovanosim".format(raide_kuria_reikia_atspeti)
                    if suklydimu_kartai > 0:
                        suklydimu_kartai = suklydimu_kartai - 1
                    leidimas_suklysti = leidimas_suklysti - 1
                    print suklydimu_kartai, "suklydimu kartai dovanojus"
                if i == raide_kuria_reikia_atspeti:
                    vienodu_raidziu_skaicius = vienodu_raidziu_skaicius + 1
            if raide_kuria_reikia_atspeti in zodis_kuri_reikia_atspeti and vienodu_raidziu_skaicius < 2:
                paslepto_zodzio_listas = list(pasleptas_zodis)
                for index, raide in enumerate(zodis_kuri_reikia_atspeti):
                    if raide == raide_kuria_reikia_atspeti:
                        paslepto_zodzio_listas[index] = raide_kuria_reikia_atspeti
                        pasleptas_zodis = "".join(paslepto_zodzio_listas)
                        print "atspejai rade", pasleptas_zodis
            elif vienodu_raidziu_skaicius > 2:
                print "suklydai, sia raide speji jau kelinta karta"
                suklydimu_kartai = suklydimu_kartai + 1
                print suklydimu_kartai, "suklydimu kartai"
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
            #Programa turi leisti zaidejui pasirinkti koki kita zodi septi:
            #Programa turi leist pasirinkti vartotojui zaidimo lygi pries kiekviena zaidima:
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