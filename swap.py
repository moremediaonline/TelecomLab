3 def normaliseer_nummer(nummer):
 4
 5     if nummer.startswith("06"):
 6         nummer ="+31" + nummer[1:]
 7
 8     elif nummer.startswith("0031"):
 9         nummer = "+" + nummer[2:]
10
11     return nummer
12
13 #einde funtie







genormaliseerd nummer: +31612345678
Resultaat: +31612345678
[OK] Geldig E.164 nummer
nl Nederlands nummer
[MOBILE] Nederlands mobiel nummer

genormaliseerd nummer: +31612345678
Resultaat: +31612345678
[OK] Geldig E.164 nummer
nl Nederlands nummer
[MOBILE] Nederlands mobiel nummer

genormaliseerd nummer: +31612345678
Resultaat: +31612345678
[OK] Geldig E.164 nummer
nl Nederlands nummer
[MOBILE] Nederlands mobiel nummer

genormaliseerd nummer: +493012345678
Resultaat: +493012345678
[OK] Geldig E.164 nummer
[FIXED] Nederlands vast nummer
[ERROR] Ongeldig  E.164 nummer
