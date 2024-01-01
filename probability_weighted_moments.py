import math
import data


# constants
TOTAL_YEAR = 20

def calcualte_total_Wi(Wi_list):
    return sum(Wi_list)


def calculate_total_Wi_square(Wi_list):
    total = 0
    for wi in Wi_list:
        total += wi**2
    return total


def calculate_Pi(i):
    Pi = (i-0.44) / (TOTAL_YEAR+0.12)
    return Pi


def calculate_deno_1(Wi_list):
    total = 0
    for i in range(1, TOTAL_YEAR+1):
        total += Wi_list[i-1] * math.log(-math.log(calculate_Pi(i), math.e), math.e)
    result = TOTAL_YEAR * total
    return result


def calculate_deno_2(Wi_list):
    total_Wi = calcualte_total_Wi(Wi_list)
    total = 0
    for i in range(1, TOTAL_YEAR+1):
        total += math.log(-math.log(calculate_Pi(i), math.e), math.e)
    result = total_Wi * total
    return result


def calculate_average_Wi(total_Wi):
    return total_Wi / TOTAL_YEAR


def calculate_M100(total_Wi):
    return calculate_average_Wi(total_Wi)

def calculate_M101(Wi_list):
    return calculate_numerator(Wi_list) / calculate_denomerator()

def calculate_numerator(Wi_list):
    total = 0
    for i in range(1,TOTAL_YEAR+1):
        total += Wi_list[i-1] * (TOTAL_YEAR-i)
    return total

def calculate_denomerator():
    return TOTAL_YEAR * (TOTAL_YEAR-1)


def calculate_beta(Wi_list):
    return ((calculate_M100(sum(Wi_list)) - 2*calculate_M101(Wi_list)) / math.log(2,math.e))

def calcualte_alpha(beta, Wi_list):
    return calculate_M100(sum(Wi_list)) - 0.5772157 * calculate_beta(Wi_list)

def calculate_alpha(average_Wi, beta):
    total = 0
    for i in range(1, TOTAL_YEAR+1):
        total += math.log(-math.log(calculate_Pi(i), math.e), math.e)
    numerator = total * beta
    result = average_Wi + ((numerator) / TOTAL_YEAR)
    return result


# =======================  Magway 10 MINUTE ==================================================
print()
print("======================  MAGWAY 10 MINUTE WIND SPEED  ==================")
magway_10_min_total_Wi = calcualte_total_Wi(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Total Wi = ", magway_10_min_total_Wi)

magway_10_min_average_Wi = calculate_average_Wi(magway_10_min_total_Wi)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", magway_10_min_average_Wi)


magway_10_min_M101 = calculate_M101(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING)
print("MAGWAY_10_MINUTE_WIND_SPEED :: M101 = ", magway_10_min_M101)

magway_10_min_beta = calculate_beta(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Beta = ", magway_10_min_beta)

magway_10_min_alpha = calculate_alpha(magway_10_min_average_Wi, magway_10_min_beta)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Alpha = ", magway_10_min_alpha)


# =======================  Minbu 10 MINUTE ==================================================
print()
print("======================  MINBU 10 MINUTE WIND SPEED  ==================")
minbu_10_min_total_Wi = calcualte_total_Wi(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING)
print("MINBU_10_MINUTE_WIND_SPEED :: Total Wi = ", minbu_10_min_total_Wi)

minbu_10_min_average_Wi = calculate_average_Wi(minbu_10_min_total_Wi)
print("MINBU_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", minbu_10_min_average_Wi)

minbu_10_min_M101 = calculate_M101(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING)
print("MINBU_10_MINUTE_WIND_SPEED :: M101 = ", minbu_10_min_M101)

minbu_10_min_beta = calculate_beta(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING)
print("MINBU_10_MINUTE_WIND_SPEED :: Beta = ", minbu_10_min_beta)

minbu_10_min_alpha = calculate_alpha(minbu_10_min_average_Wi, minbu_10_min_beta)
print("MINBU_10_MINUTE_WIND_SPEED :: Alpha = ", minbu_10_min_alpha)


# =======================  Chauk 10 MINUTE ==================================================
print()
print("======================  CHAUK 10 MINUTE WIND SPEED  ==================")
chauk_10_min_total_Wi = calcualte_total_Wi(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING)
print("CHAUK_10_MINUTE_WIND_SPEED :: Total Wi = ", chauk_10_min_total_Wi)

chauk_10_min_average_Wi = calculate_average_Wi(chauk_10_min_total_Wi)
print("CHAUK_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", chauk_10_min_average_Wi)

chauk_10_min_M101 = calculate_M101(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING)
print("CHAUK_10_MINUTE_WIND_SPEED :: M101 = ", chauk_10_min_M101)

chauk_10_min_beta = calculate_beta(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING)
print("CHAUK_10_MINUTE_WIND_SPEED :: Beta = ", chauk_10_min_beta)

chauk_10_min_alpha = calculate_alpha(chauk_10_min_average_Wi, chauk_10_min_beta)
print("CHAUK_10_MINUTE_WIND_SPEED :: Alpha = ", chauk_10_min_alpha)


# =======================  AungLan 10 MINUTE ==================================================
print()
print("======================  AUNGLAN 10 MINUTE WIND SPEED  ==================")
aunglan_10_min_total_Wi = calcualte_total_Wi(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Total Wi = ", aunglan_10_min_total_Wi)

aunglan_10_min_average_Wi = calculate_average_Wi(aunglan_10_min_total_Wi)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", aunglan_10_min_average_Wi)

aunglan_10_min_M101 = calculate_M101(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: M101 = ", aunglan_10_min_M101)

aunglan_10_min_beta = calculate_beta(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Beta = ", aunglan_10_min_beta)

aunglan_10_min_alpha = calculate_alpha(aunglan_10_min_average_Wi, aunglan_10_min_beta)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Alpha = ", aunglan_10_min_alpha)


# =======================  Pakokku 10 MINUTE ==================================================
print()
print("======================  PAKOKKU 10 MINUTE WIND SPEED  ==================")
pakokku_10_min_total_Wi = calcualte_total_Wi(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Total Wi = ", aunglan_10_min_total_Wi)

pakokku_10_min_average_Wi = calculate_average_Wi(pakokku_10_min_total_Wi)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", pakokku_10_min_average_Wi)

pakokku_10_min_M101 = calculate_M101(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: M101 = ", pakokku_10_min_M101)

pakokku_10_min_beta = calculate_beta(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Beta = ", pakokku_10_min_beta)

pakokku_10_min_alpha = calculate_alpha(pakokku_10_min_average_Wi, pakokku_10_min_beta)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Alpha = ", pakokku_10_min_alpha)


# =======================  Sinpgyukyun 10 MINUTE ==================================================
print()
print("======================  Sinpgyukyun 10 MINUTE WIND SPEED  ==================")
sinpgyukyun_10_min_total_Wi = calcualte_total_Wi(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING)
print("SINPGYUKYUN_10_MINUTE_WIND_SPEED :: Total Wi = ", sinpgyukyun_10_min_total_Wi)

sinpgyukyun_10_min_average_Wi = calculate_average_Wi(sinpgyukyun_10_min_total_Wi)
print("SINPGYUKYUN_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", sinpgyukyun_10_min_average_Wi)

sinpgyukyun_10_min_M101 = calculate_M101(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING)
print("SINPGYUKYUN_10_MINUTE_WIND_SPEED :: M101 = ", sinpgyukyun_10_min_M101)

sinpgyukyun_10_min_beta = calculate_beta(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING)
print("SINPGYUKYUN_10_MINUTE_WIND_SPEED :: Beta = ", sinpgyukyun_10_min_beta)

sinpgyukyun_10_min_alpha = calculate_alpha(sinpgyukyun_10_min_average_Wi, sinpgyukyun_10_min_beta)
print("SINPGYUKYUN_10_MINUTE_WIND_SPEED :: Alpha = ", sinpgyukyun_10_min_alpha)


# =======================  TaungDwinGyi 10 MINUTE ==================================================
print()
print("======================  TaungDwinGyi 10 MINUTE WIND SPEED  ==================")
taungdwingyi_10_min_total_Wi = calcualte_total_Wi(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Total Wi = ", taungdwingyi_10_min_total_Wi)

taungdwingyi_10_min_average_Wi = calculate_average_Wi(taungdwingyi_10_min_total_Wi)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", taungdwingyi_10_min_average_Wi)

taungdwingyi_10_min_M101 = calculate_M101(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: M101 = ", taungdwingyi_10_min_M101)

taungdwingyi_10_min_beta = calculate_beta(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Beta = ", taungdwingyi_10_min_beta)

taungdwingyi_10_min_alpha = calculate_alpha(taungdwingyi_10_min_average_Wi, taungdwingyi_10_min_beta)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Alpha = ", taungdwingyi_10_min_alpha)


# =======================  Gangaw 10 MINUTE ==================================================
print()
print("======================  Gangaw 10 MINUTE WIND SPEED  ==================")
gangaw_10_min_total_Wi = calcualte_total_Wi(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING)
print("GANGAW_10_MINUTE_WIND_SPEED :: Total Wi = ", gangaw_10_min_total_Wi)

gangaw_10_min_average_Wi = calculate_average_Wi(gangaw_10_min_total_Wi)
print("GANGAW_10_MINUTE_WIND_SPEED :: Average Wi(M100) = ", gangaw_10_min_average_Wi)

gangaw_10_min_M101 = calculate_M101(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING)
print("GANGAW_10_MINUTE_WIND_SPEED :: M101 = ", gangaw_10_min_M101)

gangaw_10_min_beta = calculate_beta(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING)
print("GANGAW_10_MINUTE_WIND_SPEED :: Beta = ", gangaw_10_min_beta)

gangaw_10_min_alpha = calculate_alpha(gangaw_10_min_average_Wi, gangaw_10_min_beta)
print("GANGAW_10_MINUTE_WIND_SPEED :: Alpha = ", gangaw_10_min_alpha)
