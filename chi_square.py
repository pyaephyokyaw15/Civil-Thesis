def calculate_chi_square(SE_list):
    # Oi = SE for each T
    # Ei =  total_SE / count_SE(9)
    summation = 0
    Ei = round(sum(SE_list) / len(SE_list), 3)
    for SE in SE_list:
        summation += round((SE - Ei)**2 / Ei, 3)
    return round(summation, 3)
