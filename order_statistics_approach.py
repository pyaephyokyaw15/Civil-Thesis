import data
import math
import AD_test
import chi_square
import KS_test
import RMSE

r_star = 0.25
r_ply = 0.063
An = 0.16665
Bn = 0.06798
Cn = 0.2314


def calculate_alpha(S, alpha_N):
    sum = 0
    for i in range(5):
        sum += alpha_N[i] * S[i]
    return round(r_star * sum, 3)


def calculate_beta(S, beta_N):
    sum = 0
    for i in range(5):
        sum += beta_N[i] * S[i]
    return round(r_star * sum, 3)

def calculate_Wt(t, alpha, beta):
    Yt = calculate_Yt(t)
    return round(alpha + Yt * beta, 3)


def calculaate_SE(beta, T):
    Wn = calculate_Wn(beta, T)
    return round(((r_star*Wn + r_ply*Wn) ** 0.5), 3)

# need to find Yt
def calculate_Yt(t):
    return round(-(math.log((-math.log((1-(1/t)),math.e)),math.e)), 3)

def calculate_Wn(beta, t):
    YT = calculate_Yt(t)
    return round(((An * YT**2 + Bn * YT + Cn) * beta ** 2), 3)


# =======================  MAGWAY 10 MINUTE  ==================================================
print("======================== Order Statistics Approach =============================")
print()
print("======================  MAGWAY 10 MINUTE WIND SPEED  ==================")
magway_10_min_beta = calculate_beta(data.MAGWAY_10_MINUTE_S, data.BETA_N)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Beta = ", magway_10_min_beta)

magway_10_min_alpha = calculate_alpha(data.MAGWAY_10_MINUTE_S, data.ALPHA_N)
print("MAGWAY_10_MINUTE_WIND_SPEED :: Alpha = ", magway_10_min_alpha)

magway_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=magway_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    magway_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, magway_10_min_alpha, magway_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("MAGWAY_10_MINUTE_WIND_SPEED :: AD = ", AD_test.calculate_AD(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING, magway_10_min_alpha, magway_10_min_beta))
print()

print("MAGWAY_10_MINUTE_WIND_SPEED :: KS = ", KS_test.calculate_KS(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING, magway_10_min_alpha, magway_10_min_beta))
print()

print("MAGWAY_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(magway_10_min_SE_list))
print()

print("MAGWAY_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MAGWAY_10_MINUTE_WIND_SPEED_ASCENDING, magway_10_min_alpha, magway_10_min_beta))
print()

# =======================  MINBU 10 MINUTE  ==================================================
print()
print("======================  MINBU 10 MINUTE WIND SPEED  ==================")
minbu_10_min_beta = calculate_beta(data.MINBU_10_MINUTE_S, data.BETA_N)
print("MINBU_10_MINUTE_WIND_SPEED :: Beta = ", minbu_10_min_beta)

minbu_10_min_alpha = calculate_alpha(data.MINBU_10_MINUTE_S, data.ALPHA_N)
print("MINBU_10_MINUTE_WIND_SPEED :: Alpha = ", minbu_10_min_alpha)

minbu_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=minbu_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    minbu_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, minbu_10_min_alpha, minbu_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("MINBU_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING, minbu_10_min_alpha, minbu_10_min_beta))
print()

print("MINBU_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING, minbu_10_min_alpha, minbu_10_min_beta))
print()

print("MINBU_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(minbu_10_min_SE_list))
print()

print("MINBU_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MINBU_10_MINUTE_WIND_SPEED_ASCENDING, minbu_10_min_alpha, minbu_10_min_beta))
print()

# =======================  CHAUK 10 MINUTE  ==================================================
print()
print("======================  CHAUK 10 MINUTE WIND SPEED  ==================")
chauk_10_min_beta = calculate_beta(data.CHAUK_10_MINUTE_S, data.BETA_N)
print("CHAUK_10_MINUTE_WIND_SPEED :: Beta = ", chauk_10_min_beta)

chauk_10_min_alpha = calculate_alpha(data.CHAUK_10_MINUTE_S, data.ALPHA_N)
print("CHAUK_10_MINUTE_WIND_SPEED :: Alpha = ", chauk_10_min_alpha)

chauk_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=chauk_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    chauk_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, chauk_10_min_alpha, chauk_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("CHAUK_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING, chauk_10_min_alpha, chauk_10_min_beta))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING, chauk_10_min_alpha, chauk_10_min_beta))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(chauk_10_min_SE_list))
print()

print("CHAUK_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.CHAUK_10_MINUTE_WIND_SPEED_ASCENDING, chauk_10_min_alpha, chauk_10_min_beta))
print()

# =======================  AUNGLAN 10 MINUTE  ==================================================
print()
print("======================  AUNGLAN 10 MINUTE WIND SPEED  ==================")
aunglan_10_min_beta = calculate_beta(data.AUNGLAN_10_MINUTE_S, data.BETA_N)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Beta = ", aunglan_10_min_beta)

aunglan_10_min_alpha = calculate_alpha(data.AUNGLAN_10_MINUTE_S, data.ALPHA_N)
print("AUNGLAN_10_MINUTE_WIND_SPEED :: Alpha = ", aunglan_10_min_alpha)

aunglan_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=aunglan_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    aunglan_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, aunglan_10_min_alpha, aunglan_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("AUNGLAN_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING, aunglan_10_min_alpha, aunglan_10_min_beta))
print()

print("AUNGLAN_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING, aunglan_10_min_alpha, aunglan_10_min_beta))
print()

print("AUNGLAN_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(aunglan_10_min_SE_list))
print()

print("AUNGLAN_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.AUNGLAN_10_MINUTE_WIND_SPEED_ASCENDING, aunglan_10_min_alpha, aunglan_10_min_beta))
print()

# =======================  PAKOKKU 10 MINUTE  ==================================================
print()
print("======================  PAKOKKU 10 MINUTE WIND SPEED  ==================")
pakokku_10_min_beta = calculate_beta(data.PAKOKKU_10_MINUTE_S, data.BETA_N)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Beta = ", pakokku_10_min_beta)

pakokku_10_min_alpha = calculate_alpha(data.PAKOKKU_10_MINUTE_S, data.ALPHA_N)
print("PAKOKKU_10_MINUTE_WIND_SPEED :: Alpha = ", pakokku_10_min_alpha)

pakokku_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=pakokku_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    pakokku_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, pakokku_10_min_alpha, pakokku_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("PAKOKKU_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING, pakokku_10_min_alpha, pakokku_10_min_beta))
print()

print("PAKOKKU_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING, pakokku_10_min_alpha, pakokku_10_min_beta))
print()

print("PAKOKKU_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(pakokku_10_min_SE_list))
print()

print("PAKOKKU_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAKOKKU_10_MINUTE_WIND_SPEED_ASCENDING, pakokku_10_min_alpha, pakokku_10_min_beta))
print()

# =======================  SINPHYUKYUN 10 MINUTE  ==================================================
print()
print("======================  SINPHYUKYUN 10 MINUTE WIND SPEED  ==================")
sinphyukyun_10_min_beta = calculate_beta(data.SINPHYUKYUN_10_MINUTE_S, data.BETA_N)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Beta = ", sinphyukyun_10_min_beta)

sinphyukyun_10_min_alpha = calculate_alpha(data.SINPHYUKYUN_10_MINUTE_S, data.ALPHA_N)
print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: Alpha = ", sinphyukyun_10_min_alpha)

sinphyukyun_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=sinphyukyun_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    sinphyukyun_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta))
print()

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta))
print()

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(sinphyukyun_10_min_SE_list))
print()

print("SINPHYUKYUN_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.SINPHYUKYUN_10_MINUTE_WIND_SPEED_ASCENDING, sinphyukyun_10_min_alpha, sinphyukyun_10_min_beta))
print()


# =======================  TAUNGDWINGYI 10 MINUTE  ==================================================
print()
print("======================  TAUNGDWINGYI 10 MINUTE WIND SPEED  ==================")
taungdwingyi_10_min_beta = calculate_beta(data.TAUNGDWINGYI_10_MINUTE_S, data.BETA_N)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Beta = ", taungdwingyi_10_min_beta)

taungdwingyi_10_min_alpha = calculate_alpha(data.TAUNGDWINGYI_10_MINUTE_S, data.ALPHA_N)
print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: Alpha = ", taungdwingyi_10_min_alpha)

taungdwingyi_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=taungdwingyi_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    taungdwingyi_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta))
print()

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta))
print()

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(taungdwingyi_10_min_SE_list))
print()

print("TAUNGDWINGYI_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.TAUNGDWINGYI_10_MINUTE_WIND_SPEED_ASCENDING, taungdwingyi_10_min_alpha, taungdwingyi_10_min_beta))
print()


# =======================  GANGAW 10 MINUTE  ==================================================
print()
print("======================  GANGAW 10 MINUTE WIND SPEED  ==================")
gangaw_10_min_beta = calculate_beta(data.GANGAW_10_MINUTE_S, data.BETA_N)
print("GANGAW_10_MINUTE_WIND_SPEED :: Beta = ", gangaw_10_min_beta)

gangaw_10_min_alpha = calculate_alpha(data.GANGAW_10_MINUTE_S, data.ALPHA_N)
print("GANGAW_10_MINUTE_WIND_SPEED :: Alpha = ", gangaw_10_min_alpha)

gangaw_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=gangaw_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    gangaw_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, gangaw_10_min_alpha, gangaw_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("GANGAW_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING, gangaw_10_min_alpha, gangaw_10_min_beta))
print()

print("GANGAW_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING, gangaw_10_min_alpha, gangaw_10_min_beta))
print()

print("GANGAW_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(gangaw_10_min_SE_list))
print()

print("GANGAW_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.GANGAW_10_MINUTE_WIND_SPEED_ASCENDING, gangaw_10_min_alpha, gangaw_10_min_beta))
print()

# =======================  PAUK 10 MINUTE  ==================================================
print()
print("======================  PAUK 10 MINUTE WIND SPEED  ==================")
pauk_10_min_beta = calculate_beta(data.PAUK_10_MINUTE_S, data.BETA_N)
print("PAUK_10_MINUTE_WIND_SPEED :: Beta = ", pauk_10_min_beta)

pauk_10_min_alpha = calculate_alpha(data.PAUK_10_MINUTE_S, data.ALPHA_N)
print("PAUK_10_MINUTE_WIND_SPEED :: Alpha = ", pauk_10_min_alpha)

pauk_10_min_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=pauk_10_min_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    pauk_10_min_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, pauk_10_min_alpha, pauk_10_min_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("PAUK_10_MINUTE_WIND_SPEED :: AD = ",
      AD_test.calculate_AD(data.PAUK_10_MINUTE_WIND_SPEED_ASCENDING, pauk_10_min_alpha, pauk_10_min_beta))
print()

print("PAUK_10_MINUTE_WIND_SPEED :: KS = ",
      KS_test.calculate_KS(data.PAUK_10_MINUTE_WIND_SPEED_ASCENDING, pauk_10_min_alpha, pauk_10_min_beta))
print()

print("PAUK_10_MINUTE_WIND_SPEED :: chi_square = ", chi_square.calculate_chi_square(pauk_10_min_SE_list))
print()

print("PAUK_10_MINUTE_WIND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAUK_10_MINUTE_WIND_SPEED_ASCENDING, pauk_10_min_alpha, pauk_10_min_beta))
print()


# ============================= 3 SECOND ==================================================

# =======================  MAGWAY 3 SECOND  ==================================================
print()
print("======================  MAGWAY 3 SECOND WIND SPEED  ==================")
magway_3_sec_beta = calculate_beta(data.MAGWAY_3_SECOND_S, data.BETA_N)
print("MAGWAY_3_SECOND_WIND_SPEED :: Beta = ", magway_3_sec_beta)

magway_3_sec_alpha = calculate_alpha(data.MAGWAY_3_SECOND_S, data.ALPHA_N)
print("MAGWAY_3_SECOND_WIND_SPEED :: Alpha = ", magway_3_sec_alpha)

magway_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=magway_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    magway_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, magway_3_sec_alpha, magway_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("MAGWAY_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.MAGWAY_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()

print("MAGWAY_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.MAGWAY_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()

print("MAGWAY_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(magway_3_sec_SE_list))
print()

print("MAGWAY_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MAGWAY_3_SECOND_WIND_SPEED_ASCENDING, magway_3_sec_alpha, magway_3_sec_beta))
print()

# =======================  MINBU 3 SECOND ==================================================
print()
print("======================  MINBU 3 SECOND WIND SPEED  ==================")
minbu_3_sec_beta = calculate_beta(data.MINBU_3_SECOND_S, data.BETA_N)
print("MINBU_3_SECOND_WIND_SPEED :: Beta = ", minbu_3_sec_beta)

minbu_3_sec_alpha = calculate_alpha(data.MINBU_3_SECOND_S, data.ALPHA_N)
print("MINBU_3_SECOND_WIND_SPEED :: Alpha = ", minbu_3_sec_alpha)

minbu_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=minbu_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    minbu_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, minbu_3_sec_alpha, minbu_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("MINBU_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.MINBU_3_SECOND_WIND_SPEED_ASCENDING, minbu_3_sec_alpha, minbu_3_sec_beta))
print()

print("MINBU_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.MINBU_3_SECOND_WIND_SPEED_ASCENDING, minbu_3_sec_alpha, minbu_3_sec_beta))
print()

print("MINBU_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(minbu_3_sec_SE_list))
print()

print("MINBU_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.MINBU_3_SECOND_WIND_SPEED_ASCENDING, minbu_3_sec_alpha, minbu_3_sec_beta))
print()

# =======================  CHAUK 3 SECOND  ==================================================
print()
print("======================  CHAUK 3 SECOND WIND SPEED  ==================")
chauk_3_sec_beta = calculate_beta(data.CHAUK_3_SECOND_S, data.BETA_N)
print("CHAUK_3_SECOND_WIND_SPEED :: Beta = ", chauk_3_sec_beta)

chauk_3_sec_alpha = calculate_alpha(data.CHAUK_3_SECOND_S, data.ALPHA_N)
print("CHAUK_3_SECOND_WIND_SPEED :: Alpha = ", chauk_3_sec_alpha)

chauk_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=chauk_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    chauk_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, chauk_3_sec_alpha, chauk_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("CHAUK_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.CHAUK_3_SECOND_WIND_SPEED_ASCENDING, chauk_3_sec_alpha, chauk_3_sec_beta))
print()

print("CHAUK_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.CHAUK_3_SECOND_WIND_SPEED_ASCENDING, chauk_3_sec_alpha, chauk_3_sec_beta))
print()

print("CHAUK_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(chauk_3_sec_SE_list))
print()

print("CHAUK_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.CHAUK_3_SECOND_WIND_SPEED_ASCENDING, chauk_3_sec_alpha, chauk_3_sec_beta))
print()

# =======================  AUNGLAN 3 SECOND  ==================================================
print()
print("======================  AUNGLAN 3 SECOND WIND SPEED  ==================")
aunglan_3_sec_beta = calculate_beta(data.AUNGLAN_3_SECOND_S, data.BETA_N)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Beta = ", aunglan_3_sec_beta)

aunglan_3_sec_alpha = calculate_alpha(data.AUNGLAN_3_SECOND_S, data.ALPHA_N)
print("AUNGLAN_3_SECOND_WIND_SPEED :: Alpha = ", aunglan_3_sec_alpha)

aunglan_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=aunglan_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    aunglan_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, aunglan_3_sec_alpha, aunglan_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("AUNGLAN_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.AUNGLAN_3_SECOND_WIND_SPEED_ASCENDING, aunglan_3_sec_alpha, aunglan_3_sec_beta))
print()

print("AUNGLAN_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.AUNGLAN_3_SECOND_WIND_SPEED_ASCENDING, aunglan_3_sec_alpha, aunglan_3_sec_beta))
print()

print("AUNGLAN_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(aunglan_3_sec_SE_list))
print()

print("AUNGLAN_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.AUNGLAN_3_SECOND_WIND_SPEED_ASCENDING, aunglan_3_sec_alpha, aunglan_3_sec_beta))
print()

# =======================  PAKOKKU 3 SECOND ==================================================
print()
print("======================  PAKOKKU 3 SECOND WIND SPEED  ==================")
pakokku_3_sec_beta = calculate_beta(data.PAKOKKU_3_SECOND_S, data.BETA_N)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Beta = ", pakokku_3_sec_beta)

pakokku_3_sec_alpha = calculate_alpha(data.PAKOKKU_3_SECOND_S, data.ALPHA_N)
print("PAKOKKU_3_SECOND_WIND_SPEED :: Alpha = ", pakokku_3_sec_alpha)

pakokku_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=pakokku_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    pakokku_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, pakokku_3_sec_alpha, pakokku_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("PAKOKKU_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.PAKOKKU_3_SECOND_WIND_SPEED_ASCENDING, pakokku_3_sec_alpha, pakokku_3_sec_beta))
print()

print("PAKOKKU_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.PAKOKKU_3_SECOND_WIND_SPEED_ASCENDING, pakokku_3_sec_alpha, pakokku_3_sec_beta))
print()

print("PAKOKKU_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(pakokku_3_sec_SE_list))
print()

print("PAKOKKU_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAKOKKU_3_SECOND_WIND_SPEED_ASCENDING, pakokku_3_sec_alpha, pakokku_3_sec_beta))
print()

# =======================  SINPHYUKYUN 3 SECOND  ==================================================
print()
print("======================  SINPHYUKYUN 3 SECOND WIND SPEED  ==================")
sinphyukyun_3_sec_beta = calculate_beta(data.SINPHYUKYUN_3_SECOND_S, data.BETA_N)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Beta = ", sinphyukyun_3_sec_beta)

sinphyukyun_3_sec_alpha = calculate_alpha(data.SINPHYUKYUN_3_SECOND_S, data.ALPHA_N)
print("SINPHYUKYUN_3_SECOND_WIND_SPEED :: Alpha = ", sinphyukyun_3_sec_alpha)

sinphyukyun_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=sinphyukyun_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    sinphyukyun_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("SINPHYUKYUN_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.SINPHYUKYUN_3_SECOND_WIND_SPEED_ASCENDING, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta))
print()

print("SINPHYUKYUN_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.SINPHYUKYUN_3_SECOND_WIND_SPEED_ASCENDING, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta))
print()

print("SINPHYUKYUN_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(sinphyukyun_3_sec_SE_list))
print()

print("SINPHYUKYUN_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.SINPHYUKYUN_3_SECOND_WIND_SPEED_ASCENDING, sinphyukyun_3_sec_alpha, sinphyukyun_3_sec_beta))
print()

# =======================  TAUNGDWINGYI 3 SECOND  ==================================================
print()
print("======================  TAUNGDWINGYI 3 SECOND WIND SPEED  ==================")
taungdwingyi_3_sec_beta = calculate_beta(data.TAUNGDWINGYI_3_SECOND_S, data.BETA_N)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Beta = ", taungdwingyi_3_sec_beta)

taungdwingyi_3_sec_alpha = calculate_alpha(data.TAUNGDWINGYI_3_SECOND_S, data.ALPHA_N)
print("TAUNGDWINGYI_3_SECOND_WIND_SPEED :: Alpha = ", taungdwingyi_3_sec_alpha)

taungdwingyi_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=taungdwingyi_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    taungdwingyi_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("TAUNGDWINGYI_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED_ASCENDING, taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta))
print()

print("TAUNGDWINGYI_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED_ASCENDING, taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta))
print()

print("TAUNGDWINGYI_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(taungdwingyi_3_sec_SE_list))
print()

print("TAUNGDWINGYI_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.TAUNGDWINGYI_3_SECOND_WIND_SPEED_ASCENDING, taungdwingyi_3_sec_alpha, taungdwingyi_3_sec_beta))
print()


# =======================  GANGAW 3 SECOND  ==================================================
print()
print("======================  GANGAW 3 SECOND WIND SPEED  ==================")
gangaw_3_sec_beta = calculate_beta(data.GANGAW_3_SECOND_S, data.BETA_N)
print("GANGAW_3_SECOND_WIND_SPEED :: Beta = ", gangaw_3_sec_beta)

gangaw_3_sec_alpha = calculate_alpha(data.GANGAW_3_SECOND_S, data.ALPHA_N)
print("GANGAW_3_SECOND_WIND_SPEED :: Alpha = ", gangaw_3_sec_alpha)

gangaw_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=gangaw_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    gangaw_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, gangaw_3_sec_alpha, gangaw_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("GANGAW_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.GANGAW_3_SECOND_WIND_SPEED_ASCENDING, gangaw_3_sec_alpha, gangaw_3_sec_beta))
print()

print("GANGAW_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.GANGAW_3_SECOND_WIND_SPEED_ASCENDING, gangaw_3_sec_alpha, gangaw_3_sec_beta))
print()

print("GANGAW_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(gangaw_3_sec_SE_list))
print()

print("GANGAW_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.GANGAW_3_SECOND_WIND_SPEED_ASCENDING, gangaw_3_sec_alpha, gangaw_3_sec_beta))
print()


# =======================  PAUK 3 SECOND  ==================================================
print()
print("======================  PAUK 3 SECOND WIND SPEED  ==================")
pauk_3_sec_beta = calculate_beta(data.PAUK_3_SECOND_S, data.BETA_N)
print("PAUK_3_SECOND_WIND_SPEED :: Beta = ", pauk_3_sec_beta)

pauk_3_sec_alpha = calculate_alpha(data.PAUK_3_SECOND_S, data.ALPHA_N)
print("PAUK_3_SECOND_WIND_SPEED :: Alpha = ", pauk_3_sec_alpha)

pauk_3_sec_SE_list = []
for T in data.T:
    SE = calculaate_SE(beta=pauk_3_sec_beta, T=T)
    print("SE for " + str(T) + " =  " + str(SE))
    pauk_3_sec_SE_list.append(SE)
print()

for T in data.T:
    Wt = calculate_Wt(T, pauk_3_sec_alpha, pauk_3_sec_beta)
    print("Wt for " + str(T) + " =  " + str(Wt))

print("PAUK_3_SECOND_SPEED :: AD = ",
      AD_test.calculate_AD(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, pauk_3_sec_alpha, pauk_3_sec_beta))
print()

print("PAUK_3_SECOND_SPEED :: KS = ",
      KS_test.calculate_KS(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, pauk_3_sec_alpha, pauk_3_sec_beta))
print()

print("PAUK_3_SECOND_SPEED :: chi_square = ", chi_square.calculate_chi_square(pauk_3_sec_SE_list))
print()

print("PAUK_3_SECOND_SPEED :: RMSE = ", RMSE.calculate_RMSE(data.PAUK_3_SECOND_WIND_SPEED_ASCENDING, pauk_3_sec_alpha, pauk_3_sec_beta))
print()

