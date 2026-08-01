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







         if nummer.startswith("+31"):
42             print("nl Nederlands nummer")
43
44             if nummer.startswith("+316"):
45                 print("[MOBILE] Nederlands mobiel nummer")
46             else:
47                 print("[FIXED] Nederlands vast nummer")
48
49         elif nummer.startswith("+49"):
50             print("de Duitsland")
51
52         elif nummer.startswith("+32"):
53            print("be Belgie")
54
55         elif nummer.startswith("+33"):
56            print("fr Frankrijk")
57
58     else:
59        print("[WARN] Onbekende landcode")
60
61 else:
62     print("[ERROR] Ongeldig  E.164 nummer")
63



