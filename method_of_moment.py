import math
import data


# constants
TOTAL_YEAR = 20

def calcualte_total_Wi(Wi_list):
    return sum(Wi_list)

def calculate_average_Wi(total_Wi):
    return total_Wi / TOTAL_YEAR

def calculate_Sw(Wi_list, average_Wi):
    total = 0
    for Wi in Wi_list:
        total += (Wi - average_Wi)**2
    Sw = math.sqrt(total / (TOTAL_YEAR-1))
    return Sw

def calculate_beta(Sw):
    return (math.sqrt(6)/math.pi)*Sw

def calculate_alpha(average_Wi, beta):
    return average_Wi-0.577215*beta


# =======================  Magway 10 MINUTE ==================================================
magway_10_min_total_Wi = calcualte_total_Wi(data.MAGWAY_10_MINUTE_WIND_SPEED)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Total Wi = ", magway_10_min_total_Wi)

magway_10_min_average_Wi = calculate_average_Wi(magway_10_min_total_Wi)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Average Wi = ", magway_10_min_average_Wi)

magway_10_min_Sw = calculate_Sw(data.MAGWAY_10_MINUTE_WIND_SPEED, magway_10_min_average_Wi)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Sw = ", magway_10_min_Sw)

magway_10_min_beta = calculate_beta(magway_10_min_Sw)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Beta = ", magway_10_min_beta)

magway_10_min_alpha = calculate_alpha(magway_10_min_average_Wi, magway_10_min_beta)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Alpha = ", magway_10_min_alpha)



# =======================  Minbu 10 MINUTE ==================================================
minbu_10_min_total_Wi = calcualte_total_Wi(data.MINBU_10_MINUTE_WIND_SPEED)
print("MINBU_10_MINUTE_WIND_SPEED :: Total Wi = ", minbu_10_min_total_Wi)

minbu_10_min_average_Wi = calculate_average_Wi(minbu_10_min_total_Wi)
print("MINBU_10_MINUTE_WIND_SPEED :: Average Wi = ", minbu_10_min_average_Wi)

minbu_10_min_Sw = calculate_Sw(data.MINBU_10_MINUTE_WIND_SPEED, minbu_10_min_average_Wi)
print("MINBU_10_MINUTE_WIND_SPEED :: Sw = ", minbu_10_min_Sw)

minbu_10_min_beta = calculate_beta(minbu_10_min_Sw)
print("MINBU_10_MINUTE_WIND_SPEED :: Beta = ", minbu_10_min_beta)

minbu_10_min_alpha = calculate_alpha(minbu_10_min_average_Wi, minbu_10_min_beta)
print("MINBU_10_MINUTE_WIND_SPEED :: Alpha = ", minbu_10_min_alpha)


# =======================  Chauk 10 MINUTE ==================================================
chauk_10_min_total_Wi = calcualte_total_Wi(data.CHAUK_10_MINUTE_WIND_SPEED)
print("CHAUK_10_MINUTE_WIND_SPEED :: Total Wi = ", chauk_10_min_total_Wi)

chauk_10_min_average_Wi = calculate_average_Wi(chauk_10_min_total_Wi)
print("CHAUK_10_MINUTE_WIND_SPEED :: Average Wi = ", chauk_10_min_average_Wi)

chauk_10_min_Sw = calculate_Sw(data.CHAUK_10_MINUTE_WIND_SPEED, chauk_10_min_average_Wi)
print("CHAUK_10_MINUTE_WIND_SPEED :: Sw = ", chauk_10_min_Sw)

chauk_10_min_beta = calculate_beta(chauk_10_min_Sw)
print("CHAUK_10_MINUTE_WIND_SPEED :: Beta = ", chauk_10_min_beta)

chauk_10_min_alpha = calculate_alpha(chauk_10_min_average_Wi, chauk_10_min_beta)
print("CHAUK_10_MINUTE_WIND_SPEED :: Alpha = ", chauk_10_min_alpha)


# =======================  Aunglan 10 MINUTE ==================================================
aunglan_10_min_total_Wi = calcualte_total_Wi(data.AUNGLAN_10_MINUTE_WIND_SPEED)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Total Wi = ", aunglan_10_min_total_Wi)

aunglan_10_min_average_Wi = calculate_average_Wi(aunglan_10_min_total_Wi)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Average Wi = ", aunglan_10_min_average_Wi)

aunglan_10_min_Sw = calculate_Sw(data.AUNGLAN_10_MINUTE_WIND_SPEED, aunglan_10_min_average_Wi)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Sw = ", aunglan_10_min_Sw)

aunglan_10_min_beta = calculate_beta(aunglan_10_min_Sw)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Beta = ", aunglan_10_min_beta)

aunglan_10_min_alpha = calculate_alpha(aunglan_10_min_average_Wi, aunglan_10_min_beta)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Alpha = ", aunglan_10_min_alpha)


# =======================  Pakokku 10 MINUTE ==================================================
pakokku_10_min_total_Wi = calcualte_total_Wi(data.PAKOKKU_10_MINUTE_WIND_SPEED)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Total Wi = ", pakokku_10_min_total_Wi)

pakokku_10_min_average_Wi = calculate_average_Wi(pakokku_10_min_total_Wi)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Average Wi = ", pakokku_10_min_average_Wi)

pakokku_10_min_Sw = calculate_Sw(data.PAKOKKU_10_MINUTE_WIND_SPEED, pakokku_10_min_average_Wi)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Sw = ", pakokku_10_min_Sw)

pakokku_10_min_beta = calculate_beta(pakokku_10_min_Sw)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Beta = ", pakokku_10_min_beta)

pakokku_10_min_alpha = calculate_alpha(pakokku_10_min_average_Wi, pakokku_10_min_beta)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Alpha = ", pakokku_10_min_alpha)


# =======================  Sinphyukyun 10 MINUTE ==================================================
sinphyukyun_10_min_total_Wi = calcualte_total_Wi(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Total Wi = ", sinphyukyun_10_min_total_Wi)

sinphyukyun_10_min_average_Wi = calculate_average_Wi(sinphyukyun_10_min_total_Wi)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Average Wi = ", sinphyukyun_10_min_average_Wi)

sinphyukyun_10_min_Sw = calculate_Sw(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED, sinphyukyun_10_min_average_Wi)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Sw = ", sinphyukyun_10_min_Sw)

sinphyukyun_10_min_beta = calculate_beta(sinphyukyun_10_min_Sw)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Beta = ", sinphyukyun_10_min_beta)

sinphyukyun_10_min_alpha = calculate_alpha(sinphyukyun_10_min_average_Wi, sinphyukyun_10_min_beta)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Alpha = ", sinphyukyun_10_min_alpha)


# =======================  Taungdwingyi 10 MINUTE ==================================================
taungdwingyi_10_min_total_Wi = calcualte_total_Wi(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Total Wi = ", taungdwingyi_10_min_total_Wi)

taungdwingyi_10_min_average_Wi = calculate_average_Wi(taungdwingyi_10_min_total_Wi)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Average Wi = ", taungdwingyi_10_min_average_Wi)

taungdwingyi_10_min_Sw = calculate_Sw(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED, taungdwingyi_10_min_average_Wi)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Sw = ", taungdwingyi_10_min_Sw)

taungdwingyi_10_min_beta = calculate_beta(taungdwingyi_10_min_Sw)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Beta = ", taungdwingyi_10_min_beta)

taungdwingyi_10_min_alpha = calculate_alpha(taungdwingyi_10_min_average_Wi, taungdwingyi_10_min_beta)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Alpha = ", taungdwingyi_10_min_alpha)


# =======================  Gangaw 10 MINUTE ==================================================
gangaw_10_min_total_Wi = calcualte_total_Wi(data.GANGAW_10_MINUTE_WIND_SPEED)
print("GANGAW_10_MINUTE_WIND_SPEED :: Total Wi = ", gangaw_10_min_total_Wi)

gangaw_10_min_average_Wi = calculate_average_Wi(gangaw_10_min_total_Wi)
print("GANGAW_10_MINUTE_WIND_SPEED :: Average Wi = ", gangaw_10_min_average_Wi)

gangaw_10_min_Sw = calculate_Sw(data.GANGAW_10_MINUTE_WIND_SPEED, gangaw_10_min_average_Wi)
print("GANGAW_10_MINUTE_WIND_SPEED :: Sw = ", gangaw_10_min_Sw)

gangaw_10_min_beta = calculate_beta(gangaw_10_min_Sw)
print("GANGAW_10_MINUTE_WIND_SPEED :: Beta = ", gangaw_10_min_beta)

gangaw_10_min_alpha = calculate_alpha(gangaw_10_min_average_Wi, gangaw_10_min_beta)
print("GANGAW_10_MINUTE_WIND_SPEED :: Alpha = ", gangaw_10_min_alpha)


# =======================  Pauk 10 MINUTE ==================================================
pauk_10_min_total_Wi = calcualte_total_Wi(data.PAUK_10_MINUTE_WIND_SPEED)
print("PAUK_10_MINUTE_WIND_SPEED :: Total Wi = ", pauk_10_min_total_Wi)

pauk_10_min_average_Wi = calculate_average_Wi(pauk_10_min_total_Wi)
print("PAUK_10_MINUTE_WIND_SPEED :: Average Wi = ", pauk_10_min_average_Wi)

pauk_10_min_Sw = calculate_Sw(data.PAUK_10_MINUTE_WIND_SPEED, pauk_10_min_average_Wi)
print("PAUK_10_MINUTE_WIND_SPEED :: Sw = ", pauk_10_min_Sw)

pauk_10_min_beta = calculate_beta(pauk_10_min_Sw)
print("PAUK_10_MINUTE_WIND_SPEED :: Beta = ", pauk_10_min_beta)

pauk_10_min_alpha = calculate_alpha(pauk_10_min_average_Wi, pauk_10_min_beta)
print("PAUK_10_MINUTE_WIND_SPEED :: Alpha = ", pauk_10_min_alpha)


# =======================  Magway 3 SECOND ==================================================
magway_3_sec_total_Wi = calcualte_total_Wi(data.MAGWAY_3_SECOND_WIND_SPEED)
print("MAGWAY_3_SECOND_WIND_SPEED :: Total Wi = ", magway_3_sec_total_Wi)

magway_3_sec_average_Wi = calculate_average_Wi(magway_3_sec_total_Wi)
print("MAGWAY_3_SECOND_WIND_SPEED :: Average Wi = ", magway_3_sec_average_Wi)

magway_3_sec_Sw = calculate_Sw(data.MAGWAY_3_SECOND_WIND_SPEED, magway_3_sec_average_Wi)
print("MAGWAY_3_SECOND_WIND_SPEED :: Sw = ", magway_3_sec_Sw)

magway_3_sec_beta = calculate_beta(magway_3_sec_Sw)
print("MAGWAY_3_SECOND_WIND_SPEED :: Beta = ", magway_3_sec_beta)

magway_3_sec_alpha = calculate_alpha(magway_3_sec_average_Wi, magway_3_sec_beta)
print("MAGWAY_3_SECOND_WIND_SPEED :: Alpha = ", magway_10_min_alpha)



# =======================  Minbu 3 SECOND ==================================================
minbu_3_sec_total_Wi = calcualte_total_Wi(data.MINBU_3_SECOND_WIND_SPEED)
print("MINBU_3_SECOND_WIND_SPEED :: Total Wi = ", minbu_3_sec_total_Wi)

minbu_3_sec_average_Wi = calculate_average_Wi(minbu_3_sec_total_Wi)
print("MINBU_3_SECOND_WIND_SPEED :: Average Wi = ", minbu_3_sec_average_Wi)

minbu_3_sec_Sw = calculate_Sw(data.MINBU_3_SECOND_WIND_SPEED, minbu_3_sec_average_Wi)
print("MINBU_3_SECOND_WIND_SPEED :: Sw = ", minbu_3_sec_Sw)

minbu_3_sec_beta = calculate_beta(minbu_3_sec_Sw)
print("MINBU_3_SECOND_WIND_SPEED :: Beta = ", minbu_3_sec_beta)

minbu_3_sec_alpha = calculate_alpha(minbu_3_sec_average_Wi, minbu_3_sec_beta)
print("MINBU_3_SECOND_WIND_SPEED :: Alpha = ", minbu_3_sec_alpha)


# =======================  Chauk 3 SECOND ==================================================
chauk_3_sec_total_Wi = calcualte_total_Wi(data.CHAUK_3_SECOND_WIND_SPEED)
print("CHAUK_3_SECOND_WIND_SPEED :: Total Wi = ", chauk_3_sec_total_Wi)

chauk_3_sec_average_Wi = calculate_average_Wi(chauk_3_sec_total_Wi)
print("CHAUK_3_SECOND_WIND_SPEED :: Average Wi = ", chauk_3_sec_average_Wi)

chauk_3_sec_Sw = calculate_Sw(data.CHAUK_3_SECOND_WIND_SPEED, chauk_3_sec_average_Wi)
print("CHAUK_3_SECOND_WIND_SPEED :: Sw = ", chauk_3_sec_Sw)

chauk_3_sec_beta = calculate_beta(chauk_3_sec_Sw)
print("CHAUK_3_SECOND_WIND_SPEED :: Beta = ", chauk_3_sec_beta)

chauk_3_sec_alpha = calculate_alpha(chauk_3_sec_average_Wi, chauk_3_sec_beta)
print("CHAUK_3_SECOND_WIND_SPEED :: Alpha = ", chauk_3_sec_alpha)


# =======================  Aunglan 3 SECOND ==================================================
aunglan_3_sec_total_Wi = calcualte_total_Wi(data.AUNGLAN_3_SECOND_WIND_SPEED)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Total Wi = ", aunglan_3_sec_total_Wi)

aunglan_3_sec_average_Wi = calculate_average_Wi(aunglan_3_sec_total_Wi)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Average Wi = ", aunglan_3_sec_average_Wi)

aunglan_3_sec_Sw = calculate_Sw(data.AUNGLAN_3_SECOND_WIND_SPEED, aunglan_3_sec_average_Wi)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Sw = ", aunglan_3_sec_Sw)

aunglan_3_sec_beta = calculate_beta(aunglan_3_sec_Sw)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Beta = ", aunglan_3_sec_beta)

aunglan_3_sec_alpha = calculate_alpha(aunglan_3_sec_average_Wi, aunglan_3_sec_beta)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Alpha = ", aunglan_3_sec_alpha)


# =======================  Pakokku 3 SECOND ==================================================
pakokku_3_sec_total_Wi = calcualte_total_Wi(data.PAKOKKU_3_SECOND_WIND_SPEED)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Total Wi = ", pakokku_3_sec_total_Wi)

pakokku_3_sec_average_Wi = calculate_average_Wi(pakokku_3_sec_total_Wi)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Average Wi = ", pakokku_3_sec_average_Wi)

pakokku_3_sec_Sw = calculate_Sw(data.PAKOKKU_3_SECOND_WIND_SPEED, pakokku_3_sec_average_Wi)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Sw = ", pakokku_3_sec_Sw)

pakokku_3_sec_beta = calculate_beta(pakokku_3_sec_Sw)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Beta = ", pakokku_3_sec_beta)

pakokku_3_sec_alpha = calculate_alpha(pakokku_3_sec_average_Wi, pakokku_3_sec_beta)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Alpha = ", pakokku_3_sec_alpha)


# =======================  Sinphyukyun 3 SECOND ==================================================
sinphyukyun_3_sec_total_Wi = calcualte_total_Wi(data.SINPHYUKYUN_3_SECOND_WIND_SPEED)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Total Wi = ", sinphyukyun_3_sec_total_Wi)

sinphyukyun_3_sec_average_Wi = calculate_average_Wi(sinphyukyun_3_sec_total_Wi)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Average Wi = ", sinphyukyun_3_sec_average_Wi)

sinphyukyun_3_sec_Sw = calculate_Sw(data.SINPHYUKYUN_3_SECOND_WIND_SPEED, sinphyukyun_3_sec_average_Wi)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Sw = ", sinphyukyun_3_sec_Sw)

sinphyukyun_3_sec_beta = calculate_beta(sinphyukyun_3_sec_Sw)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Beta = ", sinphyukyun_3_sec_beta)

sinphyukyun_3_sec_alpha = calculate_alpha(sinphyukyun_3_sec_average_Wi, sinphyukyun_3_sec_beta)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Alpha = ", sinphyukyun_3_sec_alpha)


# =======================  Taungdwingyi 3 SECOND ==================================================
taungdwingyi_3_sec_total_Wi = calcualte_total_Wi(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Total Wi = ", taungdwingyi_3_sec_total_Wi)

taungdwingyi_3_sec_average_Wi = calculate_average_Wi(taungdwingyi_3_sec_total_Wi)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Average Wi = ", taungdwingyi_3_sec_average_Wi)

taungdwingyi_3_sec_Sw = calculate_Sw(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED, taungdwingyi_3_sec_average_Wi)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Sw = ", taungdwingyi_3_sec_Sw)

taungdwingyi_3_sec_beta = calculate_beta(taungdwingyi_3_sec_Sw)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Beta = ", taungdwingyi_3_sec_beta)

taungdwingyi_3_sec_alpha = calculate_alpha(taungdwingyi_3_sec_average_Wi, taungdwingyi_3_sec_beta)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Alpha = ", taungdwingyi_10_min_alpha)


# =======================  Gangaw 3 SECOND ==================================================
gangaw_3_sec_total_Wi = calcualte_total_Wi(data.GANGAW_3_SECOND_WIND_SPEED)
print("GANGAW_3_SECOND_WIND_SPEED :: Total Wi = ", gangaw_3_sec_total_Wi)

gangaw_3_sec_average_Wi = calculate_average_Wi(gangaw_3_sec_total_Wi)
print("GANGAW_3_SECOND_WIND_SPEED :: Average Wi = ", gangaw_3_sec_average_Wi)

gangaw_3_sec_Sw = calculate_Sw(data.GANGAW_3_SECOND_WIND_SPEED, gangaw_3_sec_average_Wi)
print("GANGAW_3_SECOND_WIND_SPEED :: Sw = ", gangaw_3_sec_Sw)

gangaw_3_sec_beta = calculate_beta(gangaw_3_sec_Sw)
print("GANGAW_3_SECOND_WIND_SPEED :: Beta = ", gangaw_3_sec_beta)

gangaw_3_sec_alpha = calculate_alpha(gangaw_3_sec_average_Wi, gangaw_3_sec_beta)
print("GANGAW_3_SECOND_WIND_SPEED :: Alpha = ", gangaw_10_min_alpha)


# =======================  Pauk 3 SECOND ==================================================
pauk_3_sec_total_Wi = calcualte_total_Wi(data.PAUK_3_SECOND_WIND_SPEED)
print("PAUK_3_SECOND_WIND_SPEED :: Total Wi = ", pauk_3_sec_total_Wi)

pauk_3_sec_average_Wi = calculate_average_Wi(pauk_3_sec_total_Wi)
print("PAUK_3_SECOND_WIND_SPEED :: Average Wi = ", pauk_3_sec_average_Wi)

pauk_3_sec_Sw = calculate_Sw(data.PAUK_3_SECOND_WIND_SPEED, pauk_3_sec_average_Wi)
print("PAUK_3_SECOND_WIND_SPEED :: Sw = ", pauk_3_sec_Sw)

pauk_3_sec_beta = calculate_beta(pauk_3_sec_Sw)
print("PAUK_3_SECOND_WIND_SPEED :: Beta = ", pauk_10_min_beta)

pauk_3_sec_alpha = calculate_alpha(pauk_3_sec_average_Wi, pauk_3_sec_beta)
print("PAUK_3_SECOND_WIND_SPEED :: Alpha = ", pauk_3_sec_alpha)

