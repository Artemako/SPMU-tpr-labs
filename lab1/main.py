import math


def read_data():
    k1, k2, k3 = map(int, input("Введите k1 k2 k3 'Шифр кода': ").split())
    return k1, k2, k3


def first():
    N = 3000000
    P1 = 0.5 + (k2 + 1) / (2 * (k3 + 11))
    P2 = 0.5 + 0.02 * (k1 + k2 + 1)
    print("P1 =", P1)
    print("P2 =", P2)
    print("-" * 20)
    nodes = {'A': {'B': {}, 'C': {}}}

    frst_p = [[P1 * N, 0.5 * N],[0.5 * N, P2 * N]]
    print('Матрица выигрышей первого')
    print(*frst_p[0])
    print(*frst_p[1])
    print("-" * 20)
    scnd_p = [[(1 - P1) * N, 0.5 * N],[0.5 * N, (1 - P2) * N]]
    print('Матрица выигрышей второго')
    print(*scnd_p[0])
    print(*scnd_p[1])
    print("-" * 20)
    x0 = (frst_p[1][1] - frst_p[0][1]) / (frst_p[0][0] - frst_p[0][1] - frst_p[1][0] + frst_p[1][1])
    V = x0 * frst_p[0][0] + (1 - x0) * frst_p[0][1]
    q1 = x0 * V
    q2 = (1 - x0) * V
    print('x0 =', '%.2f' % x0, '\nV =', '%.2f' % V, '\nq1 =', '%.2f' % q1, '\nq2 =', '%.2f' % q2)


if __name__ == '__main__':
    print("1) ЧТЕНИЕ ДАННЫХ")
    k1, k2, k3 = read_data()
    print("\n2) РАБОТА С ДАННЫМИ")
    first()
    input("\nНажмите Enter, чтобы выйти...")
