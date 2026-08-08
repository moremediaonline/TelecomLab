with open("nummers.txt", "r" ) as bestand:
    for regel in bestand:
        nummer = regel.strip()
        print("\nControle van:", nummer)

        nummer = normaliseer_nummer(nummer)

        if nummer:
            valideer_nummer(nummer) 
