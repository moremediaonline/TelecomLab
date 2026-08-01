import re

def normaliseer_nummer(nummer):

    if nummer.startswith("06"):
        nummer ="+31" + nummer[1:]

    elif nummer.startswith("0031"):
        nummer = "+" + nummer[2:]

    return nummer

#einde funtie

nummers = [
    "0612345678",
    "0031612345678",
    "+31612345678",
    "+493012345678"
]

for nummers in nummers:
    print(nummer)

nummer = nummer.strip()
nummer = nummer.replace(" ", "")
nummer = normaliseer_nummer(nummer)

# Nederlandse omzettingen


if nummer.startswith("06"):
        nummer ="+31" + nummer[1:]

if nummer.startswith("0031"):
        nummer = "+" + nummer[2:]



# E.164 controle
patroon = r"^\+[1-9][0-9]{1,14}$"

print()
print("genormaliseerd nummer:", nummer)

if re.match(patroon, nummer):
    print("[OK] Geldig E.164 nummer")

    if nummer.startswith("+31"):
        print("nl Nederlands nummer")

        if nummer.startswith("+316"):
            print("[MOBILE] Nederlands mobiel nummer")
        else:
            print("[FIXED] Nederlands vast nummer")

    elif nummer.startswith("+49"):
       print("de Duitsland")

    elif nummer.startswith("+32"):
       print("be Belgie")

    elif nummer.startswith("+33"):
       print("fr Frankrijk")

    else:
       print("[WARN] Onbekende landcode")

else:
     print("[ERROR] Ongeldig  E.164 nummer")









