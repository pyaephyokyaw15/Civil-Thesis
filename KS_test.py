import math

N = 20
# i =1 to 20

def calculate_FWi(Wi, alpha, beta):
    # print("Wi = ", Wi)
    # print("alpha = ", alpha)
    # print("beta = ", beta)
    FWi = round(math.e ** (-((math.e) ** (-(Wi-alpha)/beta))), 3)
    # print("FWi = ",  FWi)
    return FWi

def calculate_FeWi(i):
   return round((i-0.44) / (N + 0.12), 3)

def calculate_Zi(Wi, alpha, beta):
    return calculate_FWi(Wi, alpha, beta)


def calculate_KS(W, alpha, beta):
    ans_list = []
    for a in range(1, N+1):
        ans_list.append(round(calculate_FeWi(a) - calculate_FWi(W[a-1], alpha, beta),3))
    return max(ans_list)




