import math

N = 20

Wi_star_list  = []
def calculate_WE(average_W,Wi, alpha, beta):
    WE = round(average_W + (beta * math.log(1/(1-calculate_FWi(Wi,alpha,beta)),math.e)), 3)
    print("Wi* = ", WE)
    Wi_star_list.append(WE)
    return WE

def calculate_FWi(Wi, alpha, beta):
    # print("Wi = ", Wi)
    # print("alpha = ", alpha)
    # print("beta = ", beta)
    FWi = round(math.e ** (-((math.e) ** (-(Wi-alpha)/beta))), 3)
    return FWi


def calculate_RMSE(W, alpha, beta):
    summation = 0
    avreage_W = round(sum(W) / N, 3)
    for a in range(1, N+1):
        summation = summation + round((W[a-1] - calculate_WE(avreage_W, W[a-1], alpha, beta)) **2, 3)
    print(Wi_star_list)
    return round(((summation / N) ** 0.5), 3)



# We = Wi*

# We = average_W + beta ln