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
