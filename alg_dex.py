#алгоритм декстера
f1 = open("input.txt", "rt")
f2 = open("output.txt", "wt")
m = []
for i in f1:
    f2.write(i)
    m.append([])
    m[-1] = list(map(int, i.strip().split()))
print("\n", file=f2)
L = [[-1 for i in range(len(m))] for j in range(len(m))]
for i in range(len(m)):
    V = []
    C = [False for i in range(len(m))]
    Fl = 1
    L[i][i] = 0
    t = [100 ** 100 for i in range(len(m))]
    t[i] = 0
    while Fl:
        a = None
        Fl = 0
        for j in range(len(m)):
            if not C[j] and j not in V:
                if a is None:
                    a = j
                    Fl = 1
                elif t[j] < t[a]:
                    a = j
                    Fl = 1

        if Fl:
            for X in range(len(m)):
                if m[a][X] != 0:
                    if m[a][X] + t[a] < t[X]:
                        t[X] = m[a][X] + t[a]
                        L[i][X] = t[X]
            V.append(a)
for i in L:
    print(" ".join(list(map(str, i))), file=f2)
f1.close()
f2.close()