import math


def read_data():
    k1, k2, k3 = map(int, input("Введите k1 k2 k3 'Шифр кода': ").split())
    q1 = float(input("Введите q1 'Количество плановых сборок станционарных компьютеров фирмой «X» на следующий год': "))
    return k1, k2, k3, q1


def second():
    P1 = 0.5 + (k2 + 1) / (2 * (k3 + 11))
    nodes = {'A': {'B': {}, 'C': {}}}
    S = 10 * (5 + k2 + k3)
    W = (2 + k1) / 10
    nu = 40000
    n = math.ceil(q1 / (nu * 4))
    m = 10
    pMs = [0.04, 0.21, 0.25, 0.25, 0.1, 0.05, 0.04, 0.03, 0.02, 0.01]
    p_sum = 0.331
    Np = q1 * p_sum / 1000000

    print("n =", n)
    print("m =", m)
    print("S =", S)
    print("W =", W)
    print("-" * 20)
    print('Вершина B')

    d = 1
    old_vi = -10**6
    flag = True
    while flag:
        vi = S * (0.16 * d - d / 2 * abs(0.16 * d - Np))
        nodes['A']['B'][d] = vi
        print("При d =", d, ": Vd(B) =", '%.2f' % vi)
        if old_vi < vi:
            old_vi = vi
            d += 1
        else:
            flag = False

    VB = max(list(nodes['A']['B'].values()))
    Nv = (list(nodes['A']['B'].keys())[list(nodes['A']['B'].values()).index(VB)]) * 0.16
    print("-" * 20)
    print('Вершина C')
    VC = 0
    for j in range(0, 10):
        print("При i =", j + 1, ":")
        p = j * 0.1 + 0.05
        Npi = p * q1 / 1000000
        print("pi =", '%.2f' % p)
        print("Npi =", '%.2f' % Npi)
        nodes['A']['C'][p] = []
        d = 1
        old_vi = -10 ** 6
        flag = True
        while flag:
            vi = (S * (0.16 * d - d / 2 * abs(0.16 * d - Npi)))
            nodes['A']['C'][p].append(vi)
            print("При d =", d, ": V(p) =", '%.2f' % vi)
            if old_vi < vi:
                old_vi = vi
                d += 1
            else:
                flag = False

        VC += max(nodes['A']['C'][p]) * pMs[j]
        print("-" * 20)

    F = VC - VB
    print("V(C) =", '%.2f' % VC)
    print("V(B) =", '%.2f' % VB)
    print("-" * 20)

    if F <= W:
        print('Обследование не нужно.')
        print("-" * 20)
        print('Vb =', '%.2f' % VB, "* 10^6")
        print('Nв =', '%.2f' % Nv, "* 10^6")
    else:
        print('Обследование нужно.')
        mem = (0, 0)
        Np = q1 * P1 * 0.7 / 1000000
        print("Np =", '%.2f' % Np)
        d = 1
        old_vi = -10 ** 6
        flag = True
        while flag:
            vi = S * (0.16 * d - d / 2 * abs(0.16 * d - Np))
            nodes['A']['B'][d] = vi
            print("При d =", d, ": Vd(B) =", '%.2f' % vi)

            if vi > mem[0]:
                mem = (vi, 0.16 * d)

            if old_vi < vi:
                old_vi = vi
                d += 1
            else:
                flag = False
        print("-" * 20)
        print('Vb =', '%.2f' % mem[0], "* 10^6")
        print('Nв =', '%.2f' % mem[1], "* 10^6")

if __name__ == '__main__':
    print("1) ЧТЕНИЕ ДАННЫХ")
    k1, k2, k3, q1 = read_data()
    print("\n2) РАБОТА С ДАННЫМИ")
    second()
    input("\nНажмите Enter, чтобы выйти...")
