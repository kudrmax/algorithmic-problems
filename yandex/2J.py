with open('input.txt', 'r') as file:
    lines = file.readlines()

n, m = list(map(int, lines[0].split()))

matrix = []
for line in lines[1:]:
    line = line.rstrip('\n')
    row = list(map(str, line))
    matrix.append(row)

print(matrix)

white = '.'
black = '#'

# 1. Найти три точки
# 2. Найти все возможные прямоугольники по этим трем точкам
# 3. Понять является ли оставшаяся фигура прямоугольником

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

first_black = [0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == black:
            first_black = [i, j]
            break
dir1 = [1, 0]
dir2 = [0, 1]

print(first_black)


