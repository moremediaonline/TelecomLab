import re

def normaliseer_nummer(nummer):

    if nummer.startswith("06"):
        nummer ="+31" + nummer[1:]

    elif nummer.startswith("0031"):
        nummer = "+" + nummer[2:]

    return nummer

#einde funtie



patroon = r"^\+[1-9][0-9]{1,14}$"

totaal = 0
geldig = 0
ongeldig = 0

uitvoer = open("resultaat.csv", "w")
uitvoer. write("nummer,status,land\n")

nummer_teller = 0

with open("nummers.txt", "r" ) as bestand:
    for nummer in bestand:
        nummer_teller += 1
        totaal += 1


        nummer = nummer.strip()
        nummer = nummer.replace(" ", "")
        nummer = normaliseer_nummer(nummer)
        land = "Onbekend"

        print()
        print(f"nummer {nummer_teller}")
        print("genormaliseerd nummer:", nummer)


# Nederlandse omzettingen

        if re.match(patroon, nummer):
            geldig += 1
            print("[OK] Geldig E.164 nummer")


            if nummer.startswith("+31"):
                land = "Nederland"

                if nummer.startswith("+316"):
                    print("[MOBILE] Nederlands mobiel nummer")
                else:
                    print("[FIXED] Nederlands vast nummer")

            elif nummer.startswith("+49"):
                land = "Duitsland"

            elif nummer.startswith("+32"):
                land = "Belgie"

            elif nummer.startswith("+33"):
                land = "Frankrijk"

            else:

                print("[WARN] Onbekende landcode")

            uitvoer.write(f"{nummer}, Geldig,{land}\n")


        else:
            ongeldig += 1
            print("[ERROR] Ongeldig  E.164 nummer")
            uitvoer.write(f"{nummer}, Ongeldig,Onbekend\n")


            print()
            print("-----Samenvatting--------")
            print("Totaal gecontroleerd:", totaal)
            print("geldig:", geldig)
            print("ongeldig:", ongeldig)
uitvoer.close()






