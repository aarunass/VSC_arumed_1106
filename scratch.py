import random

file_obj = open("zodziu_sarasas.txt", "r")

praeitas_ilgis = 0

for zodis in file_obj.readlines():
    ilgiausias_zodis = len(zodis[:-1])
    if praeitas_ilgis < ilgiausias_zodis:
        praeitas_ilgis = ilgiausias_zodis

lygis = input("ivesk zaidimo lygi 2-{} ".format(praeitas_ilgis))

#if lygis != int():
  #  print "ne skaicius"


file_obj = open("zodziu_sarasas.txt", "r")
zodziu_sarasas = []

for zodis in file_obj.readlines():
    zodzio_ilgis = len(zodis[:-1])
    if zodzio_ilgis == lygis:
        zodziu_sarasas.append(zodis[:-1])

zodis_kuri_reikia_atspeti = random.choice(zodziu_sarasas)
print zodis_kuri_reikia_atspeti

pasleptas_zodis = "_" * len(zodis_kuri_reikia_atspeti)

print pasleptas_zodis

zodis_neatspetas = True

while zodis_neatspetas:
    raide_kuria_reikia_atspeti = raw_input("spek raide ")
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





def zaidimas(b):
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