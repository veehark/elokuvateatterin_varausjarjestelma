import main

# avataan tiedostot
main.kirjasto_avaus(main.varaustiedot, "varaukset.csv")
main.kirjasto_avaus(main.salidata, "salitiedot.csv")
main.kirjasto_avaus(main.elokuvavalikoima, "elokuvat.csv")


valinta = input("Haluatko etsiä näytöksiä elokuvan (1) vai päivän (2) perustella? ")

if valinta == "1":
    main.lista_elokuvista()
    elokuva_valinta = input("Valitse elokuva: ")
    main.lista_naytoksista(elokuva_valinta, 0)
elif valinta == "2":
    main.lista_paivista()
    paiva_valinta = input("Valitse päivä: ")
    main.lista_naytoksista(paiva_valinta, 1)
else:
    print("Valinnan tulee olla 1 tai 2.")

naytos_valinta = input("Valitse näytös: ")
main.paikka_valinta(naytos_valinta)


# suljetaan tiedostot
main.kirjasto_tiedostoon(main.varaustiedot, "varaukset.csv")
main.kirjasto_tiedostoon(main.salidata, "salitiedot.csv")
main.kirjasto_tiedostoon(main.elokuvavalikoima, "elokuvat.csv")
