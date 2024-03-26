import math

N = 20
# i =1 to 20

def calculate_FWi(Wi, alpha, beta):
    # print("Wi = ", Wi)
    # print("alpha = ", alpha)
    # print("beta = ", beta)
    FWi = round(math.e ** (-((math.e) ** (-(Wi-alpha)/beta))), 3)
    return FWi

def calculate_Zi(Wi, alpha, beta):
    return calculate_FWi(Wi, alpha, beta)


def calculate_AD(W, alpha, beta):
    summation = 0
    for a in range(1, N+1):
        # summation = summation + round(((2*a-1) * math.log(calculate_Zi( W[a-1], alpha, beta), math.e) + (2*N + 1 - 2*a) * math.log((1-calculate_Zi(W[a-1], alpha, beta)),math.e)), 3)
        summation = summation + round(((2*a-1) * math.log(calculate_Zi( W[a-1], alpha, beta), math.e) + (2*N + 1 - 2*a) * math.log((1-calculate_Zi(W[a-1], alpha, beta)),math.e)), 3)
    return round((-N) - summation / N, 3)



