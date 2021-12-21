import random

salidata = {}
elokuvavalikoima = {}
varaustiedot = {}


def kirjasto_avaus(kirjasto, tiedosto):
    with open(tiedosto, "r") as tiedosto:
        if kirjasto == varaustiedot:
            for rivi in tiedosto:
                rivi = rivi.replace("\n","").split(",")
                kirjasto[str(rivi[0])] = list(rivi[1:])
        else:
            for rivi in tiedosto:
                rivi = rivi.replace("\n","").split(",")
                kirjasto[str(rivi[0])] = tuple((rivi[1:]))
             

def elokuvan_lisays():
    while True:
        avaimet = list(elokuvavalikoima.keys())
        uusi_avain = str(random.randint(100,999))
        if uusi_avain in avaimet:
            continue
        else:
            break
    nimi = input("Anna elokuvan nimi: ")
    ohjaaja = input(f"Anna elokuvan {nimi} ohjaaja: ")
    vuosi = input(f"Anna elokuvan {nimi} julkaisuvuosi: ")
    kestoh = input(f"Anna elokuvan kesto tunteina: ")
    elokuvavalikoima[uusi_avain] = tuple((nimi, ohjaaja, vuosi, kestoh))
    print("Elokuva", nimi, "on nyt lisätty valikoimaan.")


def varausten_paallekkaisyys(uusi_avain):
    avaimet = list(varaustiedot.keys())
    uusi_data = varaustiedot[uusi_avain]
    uusi_paiva = uusi_data[1]
    uusi_kello = uusi_data[2]
    uusi_kesto = uusi_data[3]
    uusi_sali = uusi_data[4]
    for avain in avaimet:
        vanha_data = varaustiedot[avain]
        vanha_paiva = vanha_data[1]
        vanha_kello = vanha_data[2]
        vanha_kesto = vanha_data[3]
        vanha_sali = vanha_data[4]
        if vanha_paiva == uusi_paiva and vanha_sali == uusi_sali and avain != uusi_avain:
            for i in range(int(uusi_kello),int(uusi_kello)+int(uusi_kesto)):
                for j in range(int(vanha_kello),int(vanha_kello)+int(vanha_kesto)):
                    if i == j:
                        print(f"Uusi varaus {uusi_avain} on päällekäinen varauksen {avain} kanssa joten varausta ei voida tehdä.")
                        return True
    return False


def varauksen_lisays():
    while True:
        avaimet = list(varaustiedot.keys())
        uusi_avain = str(random.randint(1000,9999))
        if uusi_avain in avaimet:
            continue
        else:
            break
    lista_elokuvista = input("Haluatko nähdä listan elokuvien tunnuksista? (y/n) ")
    elokuva_avaimet = elokuvavalikoima.keys()
    if lista_elokuvista == "y":
        for i in elokuva_avaimet:
            print(elokuvavalikoima[i][0], "=", i)
    tunniste = input("Anna varauksen elokuvan tunnus: ")
    if not tunniste in elokuva_avaimet: 
        print("Tunnisteella ei löytynyt elokuvaa.")
        return
    paiva = input("Anna varauksen päivämäärä muodossa vvvv-kk-pp: ")
    kello = input("Anna varauksen kellonaika tasatuntina: ")
    sali = input("Anna salin numero: ")
    kesto = elokuvavalikoima[tunniste][3]
    varaustiedot[uusi_avain] = [tunniste, paiva, kello, kesto, sali, ""]
    pallekkaisyys = varausten_paallekkaisyys(uusi_avain)
    if pallekkaisyys:
        del varaustiedot[uusi_avain]
    else:
        print("Varaus on nyt tallennettu varausnumerolla:", uusi_avain)


def elokuvan_selailu():
    avaimet = list(elokuvavalikoima.keys())
    haku = int(input("Haluatko hakea elokuvia tunnuksella (1) vai hakusanalla (2)? "))
    if haku == 1:
        tunnus = input("Haku tunnuksella: ")
        if tunnus in avaimet:
            print(f"{tunnus}: {elokuvavalikoima[tunnus]}")
    elif haku == 2:
        hakusana = input("Anna hakusana: ")
        for avain in avaimet:
            tiedot = list(elokuvavalikoima[avain])
            if any(hakusana in tieto for tieto in tiedot):
                print(f"{avain}: {elokuvavalikoima[avain]}")


def varauksen_selailu():
    avaimet = list(varaustiedot.keys())
    haku = input("Haluatko hakea varauksia varausnumeron (1), elokuvan tunnuksen (2),\n"
                 "salinumeron (3) vai päivämäärän (4) perusteella? ")
    if haku == "1":
        varausnro = input("Haku varausnumerolla: ")
        if varausnro in avaimet:
            print(f"{varausnro}: {varaustiedot[varausnro]}")
            return
    elokuvatunnus = ""
    salinro = ""
    paiva = ""
    if haku == "2":
        elokuvatunnus = input("Haku elokuvan tunnuksella: ")
    elif haku == "3":
        salinro = input("Haku salinumerolla: ")
    elif haku == "4":
        paiva = input("Haku päivämäärällä (annetaan muodossa vvvv-kk-pp): ")
    for avain in avaimet:
        if elokuvatunnus == varaustiedot[avain][0] or salinro == varaustiedot[avain][4] or paiva == varaustiedot[avain][1]:
            print(f"{avain}: {varaustiedot[avain]}")


def elokuvan_poisto():
    avain = input("Anna poistettavan elokuvan tunnus: ")
    print(f"Elokuva {elokuvavalikoima[avain][0]} poistettu.")
    del elokuvavalikoima[avain]


def varauksen_poisto():
    avain = input("Anna poistettavan varauksen tunnus: ")
    print(f"Varaus {avain} poistettu.")
    del varaustiedot[avain]


def kirjasto_tiedostoon(kirjasto, tiedosto):
    with open(tiedosto, "w") as tiedosto:
        avaimet = list(kirjasto.keys())
        for i in avaimet:
            jono = ""
            jono += i
            for j in range(len(kirjasto[i])):
                jono += ","
                tiedot = kirjasto[i]
                jono += str(tiedot[j])
            jono += "\n"
            tiedosto.write(jono)


def lista_elokuvista():
    avaimet = list(elokuvavalikoima.keys())
    avaimet.remove("tunnus")
    print("Elokuvavalikoima:")
    print("\n" + "{:<25} {:<25} {:<20} {:<18}".format("Elokuva", "Ohjaaja", "Julkaisuvuosi", "kesto") + "\n")
    for avain in avaimet:
        print("{:<25} {:<25} {:<20} {:<18}".format(elokuvavalikoima[avain][0], elokuvavalikoima[avain][1], elokuvavalikoima[avain][2], elokuvavalikoima[avain][3] + " tuntia"))
    print("\n")

def lista_naytoksista(valinta, indeksi):
    avaimet_elokuva = list(elokuvavalikoima.keys())
    avaimet_varaus = list(varaustiedot.keys())
    elokuva_tunnus = ""
    if indeksi == 0:
        for avain in avaimet_elokuva:
            elokuva = elokuvavalikoima[avain][0]
            if elokuva == valinta:
                elokuva_tunnus = avain
                break
    for avain in avaimet_varaus:
        if varaustiedot[avain][indeksi] == elokuva_tunnus or varaustiedot[avain][indeksi] == valinta: # jos tulee error niin tod näk elokuvan nimi tai päivämäärä kirjoitettu väärin
            print(f"Elokuvan {elokuvavalikoima[varaustiedot[avain][0]][0]} näytös {avain} esitetään {varaustiedot[avain][1]} klo {varaustiedot[avain][2]}-{int(varaustiedot[avain][2])+int(varaustiedot[avain][3])} salissa {varaustiedot[avain][4]}.")


def paikka_valinta(naytos):
    sali = varaustiedot[naytos][4]
    varatut_paikat = varaustiedot[naytos][5].split(";")
    print(varaustiedot[naytos][5])
    salikartta = ""
    for paikka in range(int(salidata[sali][0]),0,-1):
        if paikka % int(salidata[sali][1]) == 0:
            salikartta += "\n"
        if str(paikka) in varatut_paikat:
            jono = "[XX]"
        else:
            if len(str(paikka)) == 1:
                jono = "[" + "0" + str(paikka) + "]"
            else:
                jono = "[" + str(paikka) + "]"
        salikartta += jono
    print(salikartta)
    valinta = str(int(input("Valitse paikka: "))) # str(int()) koska jos käyttäjä antaa esim 01 niin nolla poistuu
    while valinta in varatut_paikat:
        valinta = input("Valitsemasi paikka on varattu, valitse toinen paikka: ")
    varatut_paikat.append(valinta)
    print(f"Olet varannut paikan nro {valinta}. Kiitos!")
    varaustiedot[naytos][5] = ";".join(varatut_paikat)
    

def lista_paivista():
     varaukset = varaustiedot.values()
     set_paivat = sorted(set([varaus[1] for varaus in varaukset if varaus[1] != "paiva"]))
     for paiva in set_paivat:
         print(paiva)
