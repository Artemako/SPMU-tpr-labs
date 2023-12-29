from decimal import *
from tkinter import *
from tkinter.filedialog import askopenfilename
import math

getcontext().prec = 14

def search_optimal_way(graph):
    current_node = 1
    way = []
    while current_node != last_v:
        way.append(graph[current_node])
        current_node = graph[current_node][0]
    return way

def optimal_f():
    # for_out = []
    print("Поиск f(i)")
    print("-" * 20)
    graph = dict()
    F = dict()
    for q, v in vs_IV.items():
        F[v] = Decimal(0)
    list_all = list(vs_III.items()) + list(vs_II.items()) + list(vs_I.items()) + list({Decimal(0): 1}.items())
    for q, v in list_all:
        F[v] = Decimal('Infinity')
        print("Вершина", v)
        for elem in list(filter(lambda x: x[0][0] == v, rebra.items())):
            D = 0
            dij = Decimal(elem[1])
            if dij != 0:
                D = (200 * (dij + 1) / dij + 10 * k1) * dij * η

            Q = 0
            for search_q, search_v in list_all:
                if search_v == elem[0][1]:
                    Q = Decimal((20 + k3) * search_q)
                    break
            print(elem[0], ": dij = ", elem[1], "; D(dij) = ", '%.2f' % D, "; Q(qj) = ", '%.2f' % Q, "; f(j) = ",
                  '%.2f' % F[elem[0][1]], "; C(dij, qj) + f(j) = ", '%.2f' % (D + Q + F[elem[0][1]]), sep='')

            if F[v] > D + Q + F[elem[0][1]]:
                F[v] = D + Q + F[elem[0][1]]
                graph[elem[0][0]] = (elem[0][1], elem[1])

        print("F(", v, ") = ", '%.2f' % F[v], sep='')
        print("-" * 20)
    print("Затраты на производство и хранение:", '%.3f' % (F[1] * Decimal(10**-6)), "млн руб")
    print("Оптимальный путь: 1", end='')
    for next_node, dij in search_optimal_way(graph):
        print(" --(dij = ", dij, ")-> ", next_node, end='', sep='')
    print()





def draw_net():
    # размеры
    padding_window = 50
    margin_x = 150
    margin_y = 100
    width = 4 * margin_x + padding_window * 2
    height = ((max(len(vs_I), len(vs_II), len(vs_III), len(vs_IV))) - 1) * margin_y + padding_window * 2
    delta_x = 25
    delta_y = 15

    # создание программы
    root = Tk()
    root.title("Сетевое представление задачи управления запасами")
    root.resizable(0, 0)
    canvas = Canvas(root, bg="yellow", height=height, width=width)

    # вершины
    coordinates = dict()

    x = padding_window
    y = height // 2
    coordinates[1] = (x, y)
    rect = canvas.create_rectangle((x - delta_x, y - delta_y), (x + delta_x, y + delta_y), outline='black',
                                   fill="white")
    text = str(0)
    label = canvas.create_text(x, y, text=text, fill="black", )
    label_2 = canvas.create_text(x, y - delta_y - 7, text=1, fill="black")

    x = padding_window + margin_x
    y = padding_window
    for q, v in vs_I.items():
        coordinates[v] = (x, y)
        rect = canvas.create_rectangle((x - delta_x, y - delta_y), (x + delta_x, y + delta_y), outline='black',
                                       fill="white")
        text = str(round(Decimal(q * Decimal(0.0001)), 2))
        label = canvas.create_text(x, y, text=text, fill="black")
        label_2 = canvas.create_text(x, y - delta_y - 7, text=v, fill="black")
        y += margin_y

    x = padding_window + margin_x * 2
    y = padding_window
    for q, v in vs_II.items():
        coordinates[v] = (x, y)
        rect = canvas.create_rectangle((x - delta_x, y - delta_y), (x + delta_x, y + delta_y), outline='black',
                                       fill="white")
        text = str(round(Decimal(q * Decimal(0.0001)), 2))
        label = canvas.create_text(x, y, text=text, fill="black")
        label_2 = canvas.create_text(x, y - delta_y - 7, text=v, fill="black")
        y += margin_y

    x = padding_window + margin_x * 3
    y = padding_window
    for q, v in vs_III.items():
        coordinates[v] = (x, y)
        rect = canvas.create_rectangle((x - delta_x, y - delta_y), (x + delta_x, y + delta_y), outline='black',
                                       fill="white")
        text = str(round(Decimal(q * Decimal(0.0001)), 2))
        label = canvas.create_text(x, y, text=text, fill="black")
        label_2 = canvas.create_text(x, y - delta_y - 7, text=v, fill="black")
        y += margin_y

    x = padding_window + margin_x * 4
    y = height // 2
    for q, v in vs_IV.items():
        coordinates[v] = (x, y)
        rect = canvas.create_rectangle((x - delta_x, y - delta_y), (x + delta_x, y + delta_y), outline='black',
                                       fill="white")
        text = str(0)
        label = canvas.create_text(x, y, text=text, fill="black")
        label_2 = canvas.create_text(x, y - delta_y - 7, text=v, fill="black")

    # print(coordinates)

    # ребра
    for pair, v in rebra.items():
        x_start = coordinates[pair[0]][0]
        y_start = coordinates[pair[0]][1]
        x_end = coordinates[pair[1]][0]
        y_end = coordinates[pair[1]][1]

        line = canvas.create_line((x_start, y_start), (x_end, y_end), fill='black', tags=["line"])
        line_label = canvas.create_text(x_start + (0.2 + 0.05 * int(v)) * (x_end - x_start),
                                        y_start + (0.2 + 0.05 * int(v)) * (y_end - y_start), text=v, fill="black")

    canvas.tag_lower("line")
    canvas.pack()
    root.mainloop()


def work_with_data():
    # обработка и получение новых данных
    n1 = Decimal(80 * k1 / (k1 + k2 + k3 + 2))
    n2 = Decimal(80 * k2 / (k1 + k2 + k3 + 2))
    n3 = Decimal(80 * k3 / (k1 + k2 + k3 + 2))
    n4 = Decimal(100 - (n1 + n2 + n3))
    N1 = Decimal(0.01) * n1 * Nv
    N2 = Decimal(0.01) * n2 * Nv
    N3 = Decimal(0.01) * n3 * Nv
    N4 = Decimal(0.01) * n4 * Nv

    print("n1, n2, n3, n4:", '%.2f' % n1, '%.2f' % n2, '%.2f' % n3, '%.2f' % n4)
    print("N1, N2, N3, N4:", '%.2f' % N1, '%.2f' % N2, '%.2f' % N3, '%.2f' % N4)

    η = 40000
    n_float = q1 / (η * 4)
    n = math.ceil(q1 / (η * 4))
    print("n 'Максимально возможное число отделений':", '%.2f' % n_float, "->", n)

    last_v = 1
    rebra = dict()
    # первый квартал
    vs_I = dict()
    for d in range(0, int(n) + 1):
        ql1 = 0 + d * η - N1
        if ql1 >= 0 and Decimal('%.0f' % ql1) <= Decimal('%.0f' % (N2 + N3 + N4)):
            if not vs_I.get(ql1):
                last_v += 1
                vs_I[ql1] = last_v
            rebra[(1, vs_I[ql1])] = d
    # print(vs_I)

    # второй квартал
    vs_II = dict()
    for ql, v in vs_I.items():
        for d in range(0, int(n) + 1):
            ql1 = ql + d * η - N2
            if ql1 >= 0 and Decimal('%.0f' % ql1) <= Decimal('%.0f' % (N3 + N4)):
                if not vs_II.get(ql1):
                    last_v += 1
                    vs_II[ql1] = last_v
                rebra[(v, vs_II[ql1])] = d
    # print(vs_II)

    # третий квартал
    vs_III = dict()
    for ql, v in vs_II.items():
        for d in range(0, int(n) + 1):
            ql1 = ql + d * η - N3
            if ql1 >= 0 and Decimal('%.0f' % ql1) <= Decimal('%.0f' % (N4)):
                if not vs_III.get(ql1):
                    last_v += 1
                    vs_III[ql1] = last_v
                rebra[(v, vs_III[ql1])] = d
    # print(vs_III)

    # четвертый квартал
    vs_IV = dict()
    for ql, v in vs_III.items():
        # print(ql, v)
        for d in range(0, int(n) + 1):
            ql1 = ql + d * η - N4
            # print(d, ql1)
            if abs(ql1) <= Decimal("0.1"):
                if not vs_IV.get(ql1):
                    last_v += 1
                    vs_IV[ql1] = last_v
                rebra[(v, vs_IV[ql1])] = d

    # print(vs_IV)
    # print(rebra)

    return rebra, vs_I, vs_II, vs_III, vs_IV, last_v, η


def read_data(filename):
    f = open(str(filename), 'r', encoding='utf-8')
    readlines = f.readlines()
    k1, k2, k3 = map(Decimal, readlines[1].split())
    Nv_man, Nv_por = map(str, readlines[3].split())
    Nv = Decimal(Nv_man) * Decimal(str(10 ** int(Nv_por)))
    q1 = Decimal(readlines[5].split()[0])

    print("k1 k2 k3 'Шифр кода':", *readlines[1].split())
    print("Nв (мантисса порядок_10) 'Число выпущенных двуядерных компьютеров':", *readlines[3].split())
    print("q1 'Количество плановых сборок станционарных компьютеров фирмой «X» на следующий год':", *readlines[5].split())
    return k1, k2, k3, Nv, q1


def openfile():
    Tk().withdraw()
    filename = askopenfilename(defaultextension="txt", filetypes=[('Text Files', '*.txt')])
    return filename


if __name__ == '__main__':
    print("1) ВЫБОР ФАЙЛА")
    filename = openfile()
    print("\n2) ЧТЕНИЕ ДАННЫХ")
    k1, k2, k3, Nv, q1 = read_data(filename)
    print("\n3) РАБОТА С ДАННЫМИ")
    rebra, vs_I, vs_II, vs_III, vs_IV, last_v, η = work_with_data()
    optimal_f()
    print("\n4) СЕТЕВОЕ ПРЕДСТАВЛЕНИЕ")
    draw_net()
