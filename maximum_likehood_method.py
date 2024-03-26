import math
import data
import AD_test
import chi_square
import RMSE
import KS_test
from sympy import symbols, Eq, solve
from scipy.optimize import fsolve
# TO DECIMAL 3

# Define the variable
x = symbols('x')
initial_guess = 1.0

# constants
TOTAL_YEAR = 20
A = 1.1589
B = 0.1919
C = 1.1

def calcualte_total_Wi(Wi_list):
    return round(sum(Wi_list), 3)

def calculate_average_Wi(total_Wi):
    return round(total_Wi / TOTAL_YEAR, 3)

def calculate_Yt(t):
    return round(-(math.log((-math.log((1-(1/t)),math.e)),math.e)), 3)


def calaulate_SE(t, beta):
    Yt = calculate_Yt(t)
    return round((beta/(20)**0.5) * (A + B*Yt + C*Yt**2)**0.5, 3)

def calculate_Wt(t, alpha, beta):
    Yt = calculate_Yt(t)
    return round(alpha + Yt * beta, 3)

def calculate_beta(Wi_list, average_Wi):
    numerator = 0
    for Wi in Wi_list:
        numerator += (Wi * (math.e ** (-Wi)))

    denomerator = 0
    for Wi in Wi_list:
        denomerator += (math.e ** (-Wi))

    answer = average_Wi - (numerator / denomerator)
    return round(answer, 3)


def calculate_alpha(Wi_list, beta):
    sum = 0
    for Wi in Wi_list:
        sum += (math.e ** (-Wi / beta))
    alpha = -beta * math.log(sum/TOTAL_YEAR)
    return round(alpha, 3)


print("===================== Maximum Likelihood Method ======================")
print()

# =======================  Magway 10 MINUTE ==================================================
print("=======================  Magway 10 MINUTE ====================================")
magway_10_min_total_Wi = calcualte_total_Wi(data.MAGWAY_10_MINUTE_WIND_SPEED)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Total Wi = ", magway_10_min_total_Wi)

magway_10_min_average_Wi = calculate_average_Wi(magway_10_min_total_Wi)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Average Wi = ", magway_10_min_average_Wi)

magway_10_min_beta = calculate_beta(data.MAGWAY_10_MINUTE_WIND_SPEED, magway_10_min_average_Wi)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Beta = ", magway_10_min_beta)

magway_10_min_alpha = calculate_alpha(data.MAGWAY_10_MINUTE_WIND_SPEED, magway_10_min_beta)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Alpha = ", magway_10_min_alpha)

print()
magway_10_min_SE_list = []
for T in data.T:
    SE = calaulate_SE(T, magway_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    magway_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, magway_10_min_alpha, magway_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("MAGWAY_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING, magway_10_min_alpha, magway_10_min_beta))
print()

print("MAGWAY_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING, magway_10_min_alpha, magway_10_min_beta))
print()

print("MAGWAY_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(magway_10_min_SE_list))
print()

print("MAGWAY_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING, magway_10_min_alpha, magway_10_min_beta))
print()

# =======================  Minbu 10 MINUTE ==================================================
print("=======================  Minbu 10 MINUTE ==================================")
minbu_10_min_total_Wi = calcualte_total_Wi(data.MINBU_10_MINUTE_WIND_SPEED)
print("MINBU_10_MINUTE_WIND_SPEED :: Total Wi = ", minbu_10_min_total_Wi)

minbu_10_min_average_Wi = calculate_average_Wi(minbu_10_min_total_Wi)
print("MINBU_10_MINUTE_WIND_SPEED :: Average Wi = ", minbu_10_min_average_Wi)

minbu_10_min_beta = calculate_beta(data.MINBU_10_MINUTE_WIND_SPEED, minbu_10_min_average_Wi)
print("MINBU_10_MINUTE_WIND_SPEED :: Beta = ", minbu_10_min_beta)

minbu_10_min_alpha = calculate_alpha(data.MINBU_10_MINUTE_WIND_SPEED, minbu_10_min_beta)
print("MINBU_10_MINUTE_WIND_SPEED :: Alpha = ", minbu_10_min_alpha)

minbu_10_min_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, minbu_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    minbu_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, minbu_10_min_alpha, minbu_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("MINBU_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING, minbu_10_min_alpha, minbu_10_min_beta))
print()

print("MINBU_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING, minbu_10_min_alpha, minbu_10_min_beta))
print()

print("MINBU_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(minbu_10_min_SE_list))
print()

print("MINBU_10_MINUTE_WIND_SPEED  :: RMSE = ", RMSE.calculate_RMSE(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING, minbu_10_min_alpha, minbu_10_min_beta))
print()

# =======================  Chauk 10 MINUTE ==================================================
print("=======================  Chauk 10 MINUTE ==========================================")
chauk_10_min_total_Wi = calcualte_total_Wi(data.CHAUK_10_MINUTE_WIND_SPEED)
print("CHAUK_10_MINUTE_WIND_SPEED :: Total Wi = ", chauk_10_min_total_Wi)

chauk_10_min_average_Wi = calculate_average_Wi(chauk_10_min_total_Wi)
print("CHAUK_10_MINUTE_WIND_SPEED :: Average Wi = ", chauk_10_min_average_Wi)

chauk_10_min_beta = calculate_beta(data.CHAUK_10_MINUTE_WIND_SPEED, chauk_10_min_average_Wi)
print("CHAUK_10_MINUTE_WIND_SPEED :: Beta = ", chauk_10_min_beta)

chauk_10_min_alpha = calculate_alpha(data.CHAUK_10_MINUTE_WIND_SPEED, chauk_10_min_beta)
print("CHAUK_10_MINUTE_WIND_SPEED :: Alpha = ", chauk_10_min_alpha)


chauk_10_min_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, chauk_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    chauk_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, chauk_10_min_alpha, chauk_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING, chauk_10_min_alpha, chauk_10_min_beta))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING, chauk_10_min_alpha, chauk_10_min_beta))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(chauk_10_min_SE_list))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING, chauk_10_min_alpha, chauk_10_min_beta))
print()

# =======================  Aunglan 10 MINUTE ==================================================
print("=======================  Aunglan 10 MINUTE =======================================")
aunglan_10_min_total_Wi = calcualte_total_Wi(data.AUNGLAN_10_MINUTE_WIND_SPEED)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Total Wi = ", aunglan_10_min_total_Wi)

aunglan_10_min_average_Wi = calculate_average_Wi(aunglan_10_min_total_Wi)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Average Wi = ", aunglan_10_min_average_Wi)

aunglan_10_min_beta = calculate_beta(data.AUNGLAN_10_MINUTE_WIND_SPEED, aunglan_10_min_average_Wi)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Beta = ", aunglan_10_min_beta)

aunglan_10_min_alpha = calculate_alpha(data.AUNGLAN_10_MINUTE_WIND_SPEED, aunglan_10_min_beta)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Alpha = ", aunglan_10_min_alpha)

aunglan_10_min_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, aunglan_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    aunglan_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, aunglan_10_min_alpha, aunglan_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("AUNGLAN_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING, aunglan_10_min_alpha, aunglan_10_min_beta))
print()

print("AUNGLAN_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING, aunglan_10_min_alpha, aunglan_10_min_beta))
print()

print("AUNGLAN_10_MINUTE_WIND_SPEED  :: chi_square = ", chi_square.calculate_chi_square(aunglan_10_min_SE_list))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING, aunglan_10_min_alpha, aunglan_10_min_beta))
print()

# =======================  Pakokku 10 MINUTE ==================================================
print("=======================  Pakokku 10 MINUTE ==============================")
pakokku_10_min_total_Wi = calcualte_total_Wi(data.PAKOKKU_10_MINUTE_WIND_SPEED)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Total Wi = ", pakokku_10_min_total_Wi)

pakokku_10_min_average_Wi = calculate_average_Wi(pakokku_10_min_total_Wi)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Average Wi = ", pakokku_10_min_average_Wi)

pakokku_10_min_beta = calculate_beta(data.PAKOKKU_10_MINUTE_WIND_SPEED, pakokku_10_min_average_Wi)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Beta = ", pakokku_10_min_beta)

pakokku_10_min_alpha = calculate_alpha(data.PAKOKKU_10_MINUTE_WIND_SPEED, pakokku_10_min_beta)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Alpha = ", pakokku_10_min_alpha)

print()
pakokku_10_min_SE_list = []
for T in data.T:
    SE = calaulate_SE(T, pakokku_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    pakokku_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, pakokku_10_min_alpha, pakokku_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("PAKOKKU_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING, pakokku_10_min_alpha, pakokku_10_min_beta))
print()

print("PAKOKKU_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING, pakokku_10_min_alpha, pakokku_10_min_beta))
print()

print("PAKOKKU_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(pakokku_10_min_SE_list))
print()

print("PAKOKKU_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING, pakokku_10_min_alpha, pakokku_10_min_beta))
print()

# =======================  Sinphyukyun 10 MINUTE ==================================================
print("=======================  Sinphyukyun 10 MINUTE ====================================")
sinphyukyun_10_min_total_Wi = calcualte_total_Wi(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Total Wi = ", sinphyukyun_10_min_total_Wi)

sinphyukyun_10_min_average_Wi = calculate_average_Wi(sinphyukyun_10_min_total_Wi)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Average Wi = ", sinphyukyun_10_min_average_Wi)

sinphyukyun_10_min_beta = calculate_beta(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED, sinphyukyun_10_min_average_Wi)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Beta = ", sinphyukyun_10_min_beta)

sinphyukyun_10_min_alpha = calculate_alpha(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED, sinphyukyun_10_min_beta)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Alpha = ", sinphyukyun_10_min_alpha)

print()
sinphyukyun_10_min_SE_list = []
for T in data.T:
    SE = calaulate_SE(T, sinphyukyun_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    sinphyukyun_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta))
print()

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta))
print()

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(sinphyukyun_10_min_SE_list))
print()

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED  :: RMSE = ", RMSE.calculate_RMSE(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta))
print()


# =======================  Taungdwingyi 10 MINUTE ==================================================
print("=======================  Taungdwingyi 10 MINUTE =======================================")
taungdwingyi_10_min_total_Wi = calcualte_total_Wi(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Total Wi = ", taungdwingyi_10_min_total_Wi)

taungdwingyi_10_min_average_Wi = calculate_average_Wi(taungdwingyi_10_min_total_Wi)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Average Wi = ", taungdwingyi_10_min_average_Wi)

taungdwingyi_10_min_beta = calculate_beta(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED, taungdwingyi_10_min_average_Wi)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Beta = ", taungdwingyi_10_min_beta)

taungdwingyi_10_min_alpha = calculate_alpha(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED, taungdwingyi_10_min_beta)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Alpha = ", taungdwingyi_10_min_alpha)

print()
taungdwingyi_10_min_SE_list = []
for T in data.T:
    SE = calaulate_SE(T, taungdwingyi_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    taungdwingyi_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta))
print()

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta))
print()

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(taungdwingyi_10_min_SE_list))
print()

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta))
print()


# =======================  Gangaw 10 MINUTE ==================================================
print("=======================  Gangaw 10 MINUTE ========================================")
gangaw_10_min_total_Wi = calcualte_total_Wi(data.GANGAW_10_MINUTE_WIND_SPEED)
print("GANGAW_10_MINUTE_WIND_SPEED :: Total Wi = ", gangaw_10_min_total_Wi)

gangaw_10_min_average_Wi = calculate_average_Wi(gangaw_10_min_total_Wi)
print("GANGAW_10_MINUTE_WIND_SPEED :: Average Wi = ", gangaw_10_min_average_Wi)

gangaw_10_min_beta = calculate_beta(data.GANGAW_10_MINUTE_WIND_SPEED, gangaw_10_min_average_Wi)
print("GANGAW_10_MINUTE_WIND_SPEED :: Beta = ", gangaw_10_min_beta)

gangaw_10_min_alpha = calculate_alpha(data.GANGAW_10_MINUTE_WIND_SPEED, gangaw_10_min_beta)
print("GANGAW_10_MINUTE_WIND_SPEED :: Alpha = ", gangaw_10_min_alpha)

print()
gangaw_10_min_SE_list = []
for T in data.T:
    SE = calaulate_SE(T, gangaw_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    gangaw_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, gangaw_10_min_alpha, gangaw_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("GANGAW_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING, gangaw_10_min_alpha, gangaw_10_min_beta))
print()

print("GANGAW_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING, gangaw_10_min_alpha, gangaw_10_min_beta))
print()

print("GANGAW_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(gangaw_10_min_SE_list))
print()

print("GANGAW_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING, gangaw_10_min_alpha, gangaw_10_min_beta))
print()

# =======================  Pauk 10 MINUTE ==================================================
print("=======================  Pauk 10 MINUTE =========================================")
pauk_10_min_total_Wi = calcualte_total_Wi(data.PAUK_10_MINUTE_WIND_SPEED)
print("PAUK_10_MINUTE_WIND_SPEED :: Total Wi = ", pauk_10_min_total_Wi)

pauk_10_min_average_Wi = calculate_average_Wi(pauk_10_min_total_Wi)
print("PAUK_10_MINUTE_WIND_SPEED :: Average Wi = ", pauk_10_min_average_Wi)

pauk_10_min_beta = calculate_beta(data.PAUK_10_MINUTE_WIND_SPEED, pauk_10_min_average_Wi)
print("PAUK_10_MINUTE_WIND_SPEED :: Beta = ", pauk_10_min_beta)

pauk_10_min_alpha = calculate_alpha(data.PAUK_10_MINUTE_WIND_SPEED, pauk_10_min_beta)
print("PAUK_10_MINUTE_WIND_SPEED :: Alpha = ", pauk_10_min_alpha)

pauk_10_min_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, pauk_10_min_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    pauk_10_min_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, pauk_10_min_alpha, pauk_10_min_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("PAUK_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.PAUK_10_MINUTE_WIND_SPEED_ASCENDING, pauk_10_min_alpha, pauk_10_min_beta))
print()

print("PAUK_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.PAUK_10_MINUTE_WIND_SPEED_ASCENDING, pauk_10_min_alpha, pauk_10_min_beta))
print()

print("PAUK_10_MINUTE_WIND_SPEED :: chi_sqaure = ", chi_square.calculate_chi_square(pauk_10_min_SE_list))
print()

print("PAUK_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAUK_10_MINUTE_WIND_SPEED_ASCENDING, pauk_10_min_alpha, pauk_10_min_beta))
print()

# =======================  Magway 3 SECOND ==================================================
print("=======================  Magway 3 SECOND ========================================")
magway_3_sec_total_Wi = calcualte_total_Wi(data.MAGWAY_3_SECOND_WIND_SPEED)
print("MAGWAY_3_SECOND_WIND_SPEED :: Total Wi = ", magway_3_sec_total_Wi)

magway_3_sec_average_Wi = calculate_average_Wi(magway_3_sec_total_Wi)
print("MAGWAY_3_SECOND_WIND_SPEED :: Average Wi = ", magway_3_sec_average_Wi)

magway_3_sec_beta = calculate_beta(data.MAGWAY_3_SECOND_WIND_SPEED, magway_3_sec_average_Wi)
print("MAGWAY_3_SECOND_WIND_SPEED :: Beta = ", magway_3_sec_beta)

magway_3_sec_alpha = calculate_alpha(data.MAGWAY_3_SECOND_WIND_SPEED, magway_3_sec_beta)
print("MAGWAY_3_SECOND_WIND_SPEED :: Alpha = ", magway_10_min_alpha)

magway_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, magway_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    magway_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, magway_3_sec_alpha, magway_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("MAGWAY_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.MAGWAY_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()

print("MAGWAY_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.MAGWAY_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()

print("MAGWAY_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(magway_3_sec_SE_list))
print()

print("MAGWAY_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MAGWAY_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()

# =======================  Minbu 3 SECOND ==================================================
print("=======================  Minbu 3 SECOND ======================================")
minbu_3_sec_total_Wi = calcualte_total_Wi(data.MINBU_3_SECOND_WIND_SPEED)
print("MINBU_3_SECOND_WIND_SPEED :: Total Wi = ", minbu_3_sec_total_Wi)

minbu_3_sec_average_Wi = calculate_average_Wi(minbu_3_sec_total_Wi)
print("MINBU_3_SECOND_WIND_SPEED :: Average Wi = ", minbu_3_sec_average_Wi)

minbu_3_sec_beta = calculate_beta(data.MINBU_3_SECOND_WIND_SPEED, minbu_3_sec_average_Wi)
print("MINBU_3_SECOND_WIND_SPEED :: Beta = ", minbu_3_sec_beta)

minbu_3_sec_alpha = calculate_alpha(data.MINBU_3_SECOND_WIND_SPEED, minbu_3_sec_beta)
print("MINBU_3_SECOND_WIND_SPEED :: Alpha = ", minbu_3_sec_alpha)

minbu_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, minbu_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    minbu_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, minbu_3_sec_alpha, minbu_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("MINBU_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.MINBU_3_SECOND_WIND_SPEED_ASCENDING, minbu_3_sec_alpha, minbu_3_sec_beta))
print()

print("MINBU_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.MINBU_3_SECOND_WIND_SPEED_ASCENDING, minbu_3_sec_alpha, minbu_3_sec_beta))
print()

print("MINBU_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(minbu_3_sec_SE_list))
print()

print("MINBU_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MINBU_3_SECOND_WIND_SPEED_ASCENDING, minbu_3_sec_alpha, minbu_3_sec_beta))
print()

# =======================  Chauk 3 SECOND ==================================================
print("=======================  Chauk 3 SECOND =========================================")
chauk_3_sec_total_Wi = calcualte_total_Wi(data.CHAUK_3_SECOND_WIND_SPEED)
print("CHAUK_3_SECOND_WIND_SPEED :: Total Wi = ", chauk_3_sec_total_Wi)

chauk_3_sec_average_Wi = calculate_average_Wi(chauk_3_sec_total_Wi)
print("CHAUK_3_SECOND_WIND_SPEED :: Average Wi = ", chauk_3_sec_average_Wi)

chauk_3_sec_beta = calculate_beta(data.CHAUK_3_SECOND_WIND_SPEED,chauk_3_sec_average_Wi)
print("CHAUK_3_SECOND_WIND_SPEED :: Beta = ", chauk_3_sec_beta)

chauk_3_sec_alpha = calculate_alpha(data.CHAUK_3_SECOND_WIND_SPEED, chauk_3_sec_beta)
print("CHAUK_3_SECOND_WIND_SPEED :: Alpha = ", chauk_3_sec_alpha)

chauk_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, chauk_3_sec_beta)
    chauk_3_sec_SE_list.append(SE)
    print("SE for " + str(T) + " =  " + str(SE))
print()

for T in data.T:
    WT = calculate_Wt(T, chauk_3_sec_alpha, chauk_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("CHAUK_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.CHAUK_3_SECOND_WIND_SPEED_ASCENDING, chauk_3_sec_alpha, chauk_3_sec_beta))
print()

print("CHAUK_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.CHAUK_3_SECOND_WIND_SPEED_ASCENDING, chauk_3_sec_alpha, chauk_3_sec_beta))
print()

print("CHAUK_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(chauk_3_sec_SE_list))
print()

print("CHAUK_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.CHAUK_3_SECOND_WIND_SPEED_ASCENDING, chauk_3_sec_alpha, chauk_3_sec_beta))
print()


# =======================  Aunglan 3 SECOND ==================================================
print("=======================  Aunglan 3 SECOND ========================")
aunglan_3_sec_total_Wi = calcualte_total_Wi(data.AUNGLAN_3_SECOND_WIND_SPEED)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Total Wi = ", aunglan_3_sec_total_Wi)

aunglan_3_sec_average_Wi = calculate_average_Wi(aunglan_3_sec_total_Wi)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Average Wi = ", aunglan_3_sec_average_Wi)

aunglan_3_sec_beta = calculate_beta(data.AUNGLAN_3_SECOND_WIND_SPEED, aunglan_3_sec_average_Wi)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Beta = ", aunglan_3_sec_beta)

aunglan_3_sec_alpha = calculate_alpha(data.AUNGLAN_3_SECOND_WIND_SPEED, aunglan_3_sec_beta)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Alpha = ", aunglan_3_sec_alpha)

aunglan_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, aunglan_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    aunglan_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, aunglan_3_sec_alpha, aunglan_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("AUNGLAN_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.AUNGLAN_3_SECOND_WIND_SPEED_ASCENDING, aunglan_3_sec_alpha, aunglan_3_sec_beta))
print()

print("AUNGLAN_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.AUNGLAN_3_SECOND_WIND_SPEED_ASCENDING, aunglan_3_sec_alpha, aunglan_3_sec_beta))
print()

print("AUNGLAN_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(aunglan_3_sec_SE_list))
print()

print("AUNGLAN_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.AUNGLAN_3_SECOND_WIND_SPEED_ASCENDING, aunglan_3_sec_alpha, aunglan_3_sec_beta))
print()


# =======================  Pakokku 3 SECOND ==================================================
print("=======================  Pakokku 3 SECOND =====================================")
pakokku_3_sec_total_Wi = calcualte_total_Wi(data.PAKOKKU_3_SECOND_WIND_SPEED)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Total Wi = ", pakokku_3_sec_total_Wi)

pakokku_3_sec_average_Wi = calculate_average_Wi(pakokku_3_sec_total_Wi)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Average Wi = ", pakokku_3_sec_average_Wi)

pakokku_3_sec_beta = calculate_beta(data.PAKOKKU_3_SECOND_WIND_SPEED, pakokku_3_sec_average_Wi)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Beta = ", pakokku_3_sec_beta)

pakokku_3_sec_alpha = calculate_alpha(data.PAKOKKU_3_SECOND_WIND_SPEED, pakokku_3_sec_beta)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Alpha = ", pakokku_3_sec_alpha)

pakokku_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, pakokku_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    pakokku_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, pakokku_3_sec_alpha, pakokku_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("PAKOKKU_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.PAKOKKU_3_SECOND_WIND_SPEED_ASCENDING, pakokku_3_sec_alpha, pakokku_3_sec_beta))
print()

print("PAKOKKU_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.PAKOKKU_3_SECOND_WIND_SPEED_ASCENDING, pakokku_3_sec_alpha, pakokku_3_sec_beta))
print()

print("PAKOKKU_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(pakokku_3_sec_SE_list))
print()

print("PAKOKKU_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAKOKKU_3_SECOND_WIND_SPEED_ASCENDING, pakokku_3_sec_alpha, pakokku_3_sec_beta))
print()

# =======================  Sinphyukyun 3 SECOND ==================================================
print("=======================  Sinphyukyun 3 SECOND ========================================")
sinphyukyun_3_sec_total_Wi = calcualte_total_Wi(data.SINPHYUKYUN_3_SECOND_WIND_SPEED)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Total Wi = ", sinphyukyun_3_sec_total_Wi)

sinphyukyun_3_sec_average_Wi = calculate_average_Wi(sinphyukyun_3_sec_total_Wi)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Average Wi = ", sinphyukyun_3_sec_average_Wi)

sinphyukyun_3_sec_beta = calculate_beta(data.SINPHYUKYUN_3_SECOND_WIND_SPEED, sinphyukyun_3_sec_average_Wi)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Beta = ", sinphyukyun_3_sec_beta)

sinphyukyun_3_sec_alpha = calculate_alpha(data.SINPHYUKYUN_3_SECOND_WIND_SPEED, sinphyukyun_3_sec_beta)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Alpha = ", sinphyukyun_3_sec_alpha)

sinphyukyun_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, sinphyukyun_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    sinphyukyun_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.SINPHYUKYUN_3_SECOND_WIND_SPEED_ASCENDING, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta))
print()

print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.SINPHYUKYUN_3_SECOND_WIND_SPEED_ASCENDING, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta))
print()

print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(sinphyukyun_3_sec_SE_list))
print()

print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.SINPHYUKYUN_3_SECOND_WIND_SPEED_ASCENDING, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta))
print()

# =======================  Taungdwingyi 3 SECOND ==================================================
print("=======================  Taungdwingyi 3 SECOND =======================================")
taungdwingyi_3_sec_total_Wi = calcualte_total_Wi(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Total Wi = ", taungdwingyi_3_sec_total_Wi)

taungdwingyi_3_sec_average_Wi = calculate_average_Wi(taungdwingyi_3_sec_total_Wi)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Average Wi = ", taungdwingyi_3_sec_average_Wi)

taungdwingyi_3_sec_beta = calculate_beta(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED, taungdwingyi_3_sec_average_Wi)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Beta = ", taungdwingyi_3_sec_beta)

taungdwingyi_3_sec_alpha = calculate_alpha(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED, taungdwingyi_3_sec_beta)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Alpha = ", taungdwingyi_10_min_alpha)

taungdwingyi_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, taungdwingyi_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    taungdwingyi_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED_ASCENDING, taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta))
print()

print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED_ASCENDING, taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta))
print()

print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(taungdwingyi_3_sec_SE_list))
print()

print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED_ASCENDING,taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta))
print()

# =======================  Gangaw 3 SECOND ==================================================
print("=======================  Gangaw 3 SECOND ======================================")
gangaw_3_sec_total_Wi = calcualte_total_Wi(data.GANGAW_3_SECOND_WIND_SPEED)
print("GANGAW_3_SECOND_WIND_SPEED :: Total Wi = ", gangaw_3_sec_total_Wi)

gangaw_3_sec_average_Wi = calculate_average_Wi(gangaw_3_sec_total_Wi)
print("GANGAW_3_SECOND_WIND_SPEED :: Average Wi = ", gangaw_3_sec_average_Wi)

gangaw_3_sec_beta = calculate_beta(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED, taungdwingyi_3_sec_average_Wi)
print("GANGAW_3_SECOND_WIND_SPEED :: Beta = ", gangaw_3_sec_beta)

gangaw_3_sec_alpha = calculate_alpha(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED, gangaw_3_sec_beta)
print("GANGAW_3_SECOND_WIND_SPEED :: Alpha = ", gangaw_10_min_alpha)

gangaw_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, gangaw_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    gangaw_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, gangaw_3_sec_alpha, gangaw_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("GANGAW_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.GANGAW_3_SECOND_WIND_SPEED_ASCENDING, gangaw_3_sec_alpha, gangaw_3_sec_beta))
print()

print("GANGAW_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.GANGAW_3_SECOND_WIND_SPEED_ASCENDING, gangaw_3_sec_alpha, gangaw_3_sec_beta))
print()

print("GANGAW_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(gangaw_3_sec_SE_list))
print()

print("GANGAW_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.GANGAW_3_SECOND_WIND_SPEED_ASCENDING, gangaw_3_sec_alpha, gangaw_3_sec_beta))
print()

# =======================  Pauk 3 SECOND ==================================================
print("=======================  Pauk 3 SECOND =====================================")
pauk_3_sec_total_Wi = calcualte_total_Wi(data.PAUK_3_SECOND_WIND_SPEED)
print("PAUK_3_SECOND_WIND_SPEED :: Total Wi = ", pauk_3_sec_total_Wi)

pauk_3_sec_average_Wi = calculate_average_Wi(pauk_3_sec_total_Wi)
print("PAUK_3_SECOND_WIND_SPEED :: Average Wi = ", pauk_3_sec_average_Wi)

pauk_3_sec_beta = calculate_beta(data.PAUK_3_SECOND_WIND_SPEED, pauk_3_sec_average_Wi)
print("PAUK_3_SECOND_WIND_SPEED :: Beta = ", pauk_10_min_beta)

pauk_3_sec_alpha = calculate_alpha(data.PAUK_3_SECOND_WIND_SPEED, pauk_3_sec_beta)
print("PAUK_3_SECOND_WIND_SPEED :: Alpha = ", pauk_3_sec_alpha)

pauk_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, pauk_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    pauk_3_sec_SE_list.append(SE)
print()

for T in data.T:
    WT = calculate_Wt(T, pauk_3_sec_alpha, pauk_3_sec_beta)
    print("WT for " + str(T) + " =  " + str(WT))
print()

print("PAUK_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, pauk_3_sec_alpha, pauk_3_sec_beta))
print()

print("PAUK_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, pauk_3_sec_alpha, pauk_3_sec_beta))
print()

print("PAUK_3_SECOND_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(pauk_3_sec_SE_list))
print()

print("PAUK_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, pauk_3_sec_alpha, pauk_3_sec_beta))
print()
