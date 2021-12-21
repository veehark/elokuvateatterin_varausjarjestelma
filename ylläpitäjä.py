import main

# avataan tiedostot

main.kirjasto_avaus(main.elokuvavalikoima, "elokuvat.csv")
main.kirjasto_avaus(main.varaustiedot, "varaukset.csv")


# muokataan tiedostoja
while True:
    valinta = input("Elokuvat: 1\nVaraukset: 2\nLopeta: 0\n")
    if valinta == "0":
        break
    elif valinta == "1":
        valinta_elokuva = int(input("Lisää: 1\nSelaa: 2\nPoista: 3\n"))
        if valinta_elokuva == 1:
            main.elokuvan_lisays()
        elif valinta_elokuva == 2:
            main.elokuvan_selailu()
        elif valinta_elokuva == 3:
            main.elokuvan_poisto()
    elif valinta == "2":
        valinta_varaus = int(input("Lisää: 1\nSelaa: 2\nPoista: 3\n"))
        if valinta_varaus == 1:
            main.varauksen_lisays()
        elif valinta_varaus == 2:
            main.varauksen_selailu()    
        elif valinta_varaus == 3:
            main.varauksen_poisto()

#päivitetään muokkaukset tiedostoihin

main.kirjasto_tiedostoon(main.elokuvavalikoima, "elokuvat.csv")
main.kirjasto_tiedostoon(main.varaustiedot, "varaukset.csv")
