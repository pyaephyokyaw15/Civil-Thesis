# All complete
# 2003 to 2022
import math
import data
import AD_test
import KS_test
import chi_square
import RMSE

# constants
TOTAL_YEAR = 20
A = 1.1589
B = 0.1919
C = 1.1


def calcualte_total_Wi(Wi_list):
    return round(sum(Wi_list), 3)

def calculate_average_Wi(total_Wi):
    return round(total_Wi / TOTAL_YEAR, 3)

def calculate_Sw(Wi_list, average_Wi):
    total = 0
    for Wi in Wi_list:
        total += (Wi - average_Wi)**2
    Sw = math.sqrt(total / (TOTAL_YEAR-1))
    return round(Sw, 3)

def calculate_beta(Sw):
    return round((math.sqrt(6)/math.pi)*Sw, 3)

def calculate_alpha(average_Wi, beta):
    return round(average_Wi-0.577215*beta, 3)


def calculate_Yt(t):
    return round(-(math.log((-math.log((1-(1/t)),math.e)),math.e)), 3)


def calaulate_SE(t, beta):
    Yt = calculate_Yt(t)
    return round((beta/(20)**0.5) * (A + B*Yt + C*Yt**2)**0.5, 3)


def calculate_Wt(t, alpha, beta):
    Yt = calculate_Yt(t)
    return round(alpha + Yt * beta, 3)

print("=========================== Method Of Moment =======================")
print()

# =======================  Magway 3 SECOND ==================================================
print("=======================  Magway 3 SECOND =====================")
magway_3_sec_total_Wi = calcualte_total_Wi(data.MAGWAY_3_SECOND_WIND_SPEED)
print("MAGWAY_3_SECOND_WIND_SPEED :: Total Wi = ", magway_3_sec_total_Wi)

magway_3_sec_average_Wi = calculate_average_Wi(magway_3_sec_total_Wi)
print("MAGWAY_3_SECOND_WIND_SPEED :: Average Wi = ", magway_3_sec_average_Wi)

magway_3_sec_Sw = calculate_Sw(data.MAGWAY_3_SECOND_WIND_SPEED, magway_3_sec_average_Wi)
print("MAGWAY_3_SECOND_WIND_SPEED :: Sw = ", magway_3_sec_Sw)

magway_3_sec_beta = calculate_beta(magway_3_sec_Sw)
print("MAGWAY_3_SECOND_WIND_SPEED :: Beta = ", magway_3_sec_beta)

magway_3_sec_alpha = calculate_alpha(magway_3_sec_average_Wi, magway_3_sec_beta)
print("MAGWAY_3_SECOND_WIND_SPEED :: Alpha = ", magway_3_sec_alpha)

pauk_3_sec_SE_list = []
print()
for T in data.T:
    SE = calaulate_SE(T, magway_3_sec_beta)
    print("SE for " + str(T) + " =  " + str(SE))
    pauk_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, magway_3_sec_alpha, magway_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("PAUK_3_SECOND_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()

print("PAUK_3_SECOND_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()


print("PAUK_3_SECOND_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MAGWAY_3_SECOND_WIND_SPEED, magway_3_sec_alpha, magway_3_sec_beta))
print()