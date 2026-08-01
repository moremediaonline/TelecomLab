20
21 # Nederlandse omzettingen
22
23
24 if nummer.startswith("06"):
25         nummer ="+31" + nummer[1:]
26
27     if nummer.startswith("0031"):
28         nummer = "+" + nummer[2:]
29
30
31
32 # E.164 controle
33 patroon = r"^\+[1-9][0-9]{1,14}$"
34
35 print()

