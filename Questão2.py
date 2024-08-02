def totalEntrevistados(n_A, n_B, n_C, n_A_B, n_A_C, n_B_C, n_A_B_C, n_nenhum):

    n_A_U_B_U_C = n_A + n_B + n_C - n_A_B - n_A_C - n_B_C + n_A_B_C

    n_T = n_A_U_B_U_C + n_nenhum
    return n_T

n_A = 210
n_B = 210
n_C = 250
n_A_B = 60
n_A_C = 70
n_B_C = 50
n_A_B_C = 20
n_nenhum = 100

total = totalEntrevistados(n_A, n_B, n_C, n_A_B, n_A_C, n_B_C, n_A_B_C, n_nenhum)
print(f"O número total de entrevistados é: {total}")