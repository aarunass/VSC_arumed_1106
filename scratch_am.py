
import random

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

suklydimu_kartai = 0
spejimu_listas = list()
def leidimas_suklysti(a):
    spejimu_listas.append(a)
    spejimu_listas_naujas = spejimu_listas[:-1]
    global suklydimu_kartai
    for i in spejimu_listas_naujas:
        if i == a:
            print "suklydai! raide {} jau spejai".format(a)
            suklydimu_kartai = suklydimu_kartai + 1
            if suklydimu_kartai == 2:
                print "Game over! antra karta ivedei raide kuria jau spejai"
                kartojimas = raw_input("Ar noresi kartoti zaidima? y/n")
                if kartojimas == "y":
                    zodis_kuri_reikia_atspeti = lygio_nustatymas()
                    zaidimas(zodis_kuri_reikia_atspeti)
                else:
                    quit()




zodis_neatspetas = True
def zaidimas(zodis_kuri_reikia_atspeti):
    pasleptas_zodis = "_" * len(zodis_kuri_reikia_atspeti)
    print pasleptas_zodis
    while zodis_neatspetas:
        raide_kuria_reikia_atspeti = raw_input("spek raide ")
        if raide_kuria_reikia_atspeti.isdigit() == True:
            print "tai ne raide, ivesk rade"
        else:
            leidimas_suklysti(raide_kuria_reikia_atspeti)
            if raide_kuria_reikia_atspeti in zodis_kuri_reikia_atspeti:
                paslepto_zodzio_listas = list(pasleptas_zodis)
                for index, raide in enumerate(zodis_kuri_reikia_atspeti):
                    if raide == raide_kuria_reikia_atspeti:
                        paslepto_zodzio_listas[index] = raide_kuria_reikia_atspeti
                        pasleptas_zodis = "".join(paslepto_zodzio_listas)
                        print "atspejai rade", pasleptas_zodis
            else:
                print "rades nera"
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