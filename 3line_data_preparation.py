# All complete

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


def calculate_total_Wi_square(Wi_list):
    total = 0
    for wi in Wi_list:
        total += wi**2
    return round(total, 3)


def calculate_Pi(i):
    Pi = (i-0.44) / (TOTAL_YEAR+0.12)
    return round(Pi, 3)


def calculate_deno_1(Wi_list):
    total = 0
    for i in range(1, TOTAL_YEAR+1):
        total += Wi_list[i-1] * math.log(-math.log(calculate_Pi(i), math.e), math.e)
    result = TOTAL_YEAR * total
    return round(result, 3)


def calculate_deno_2(Wi_list):
    total_Wi = calcualte_total_Wi(Wi_list)
    total = 0
    for i in range(1, TOTAL_YEAR+1):
        total += math.log(-math.log(calculate_Pi(i), math.e), math.e)
    result = total_Wi * total
    return round(result, 3)


def calculate_average_Wi(total_Wi):
    return round(total_Wi / TOTAL_YEAR, 3)


def calculate_M100(total_Wi):
    return round(calculate_average_Wi(total_Wi), 3)

def calculate_M101(Wi_list):
    return round(calculate_numerator(Wi_list) / calculate_denomerator(), 3)

def calculate_numerator(Wi_list):
    total = 0
    for i in range(1,TOTAL_YEAR+1):
        total += Wi_list[i-1] * (TOTAL_YEAR-i)
    return round(total, 3)

def calculate_denomerator():
    return round(TOTAL_YEAR * (TOTAL_YEAR-1), 3)


def calculate_beta(Wi_list):
    return round(((calculate_M100(sum(Wi_list)) - 2*calculate_M101(Wi_list)) / math.log(2,math.e)), 3)

def calcualte_alpha(beta, Wi_list):
    return round(calculate_M100(sum(Wi_list)) - 0.5772157 * calculate_beta(Wi_list), 3)

def calculate_alpha(average_Wi, beta):
    total = 0
    for i in range(1, TOTAL_YEAR+1):
        total += math.log(-math.log(calculate_Pi(i), math.e), math.e)
    numerator = total * beta
    result = average_Wi + ((numerator) / TOTAL_YEAR)
    return round(result, 3)


def calculate_Yt(t):
    return round(-(math.log((-math.log((1-(1/t)),math.e)),math.e)), 3)

def calculate_Wt(t, alpha, beta):
    Yt = calculate_Yt(t)
    return round(alpha + Yt * beta, 3)

def calaulate_SE(t, beta):
    Yt = calculate_Yt(t)
    return round((beta/(20)**0.5) * (A + B*Yt + C*Yt**2)**0.5, 3)


print("===================== Probability Weighted Moments =============================")
print()

print()
print("======================  PAKOKKU 3 SECOND WIND SPEED  ==================")
pakokku_3_sec_total_Wi = calcualte_total_Wi(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Total Wi = ", pakokku_3_sec_total_Wi)

pakokku_3_sec_average_Wi = calculate_average_Wi(pakokku_3_sec_total_Wi)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Average Wi(M100) = ", pakokku_3_sec_average_Wi)

pakokku_3_sec_M101 = calculate_M101(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING)
print("PAKOKKU_3_SECOND_WIND_SPEED :: M101 = ", pakokku_3_sec_M101)

pakokku_3_sec_beta = calculate_beta(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Beta = ", pakokku_3_sec_beta)

pakokku_3_sec_alpha = calculate_alpha(pakokku_3_sec_average_Wi, pakokku_3_sec_beta)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Alpha = ", pakokku_3_sec_alpha)

WT_list = []
for T in data.T:
    WT = calculate_Wt(T, pakokku_3_sec_alpha, pakokku_3_sec_beta)
    WT_list.append(WT)
print("WT_list: " , WT_list)


SE_list = []
for T in data.T:
    SE = calaulate_SE(T, pakokku_3_sec_beta)
    SE_list.append(SE)
print("SE_list: " , SE_list)

WT_plus_SE_list = []
for i in range(len(data.T)):
    WT_plus_SE_list.append(round(WT_list[i] + SE_list[i], 3))
print("WT_plus_SE_list: ", WT_plus_SE_list)

WT_plus_SE_divided_by_447_list = []
for i in range(len(data.T)):
    WT_plus_SE_divided_by_447_list.append(round(WT_plus_SE_list[i]/0.447, 3))
print("WT_plus_SE_divided_by_447_list: ", WT_plus_SE_divided_by_447_list)

UCL_95_list = []
for i in range(len(data.T)):
    UCL_95_list.append(round(WT_list[i]+1.96*SE_list[i], 3))
print("UCL_95_list: ", UCL_95_list)

LCL_95_list = []
for i in range(len(data.T)):
    LCL_95_list.append(round(WT_list[i]-1.96*SE_list[i], 3))
print("LCL_95_list: ", LCL_95_list)


