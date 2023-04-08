n = int(input('Кол-во вершин: '))

matrix = [input('Input: ').split(' ') for j in range(n)]

spis_par = []

count1 = 0
for i in matrix:
    count2 = 0
    for j in i:
        if j == '1':
            if (count1, count2) not in spis_par and (count2, count1) not in spis_par:
                spis_par.append((count1, count2))

        count2 += 1

    count1 += 1

new_matrix = [[0 for i in range(n)] for i in range(n)]

for count, i in enumerate(spis_par):
    new_matrix[count][i[0]] = 1
    new_matrix[count][i[1]] = 1

print(new_matrix)