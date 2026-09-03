import math
def pitsa(halkaisija,hinta):
    halk_metrinä = halkaisija  / 100
    neljöt = math.pi * (halk_metrinä / 2) ** 2
    return neljöt / hinta
pitsa_1_halk = int(input("anna pitsan halkaisija: "))
pitsa_1_hinta = int(input("anna pitsan hinta: "))
pitsa_2_halk = int(input("anna toisen pitsan halkaisija: "))
pitsa_2_hinta = int(input("anna toisen pitsan hinta: "))
vastaus_1 = pitsa(pitsa_1_halk, pitsa_1_hinta)
vastaus_2 = pitsa(pitsa_2_halk, pitsa_2_hinta)
if vastaus_1 > vastaus_2:
    print("eka pitsa parempi massille.")
else:
    print("toka pitsa parempi massille.")
