f = open('input.txt', 'r')

arr = []
for line in f:
    for el in list(map(int, line.split())):
        arr.append(el)

P, V = arr[0], arr[1]
Q, M = arr[2], arr[3]

int1 = [P - V, P + V]
int2 = [Q - M, Q + M]

if int1[0] > int2[0]:
    int1, int2 = int2, int1

if int1[1] < int2[0]:
    print(int1[1] - int1[0] + int2[1] - int2[0] + 2)
else:
    new_int = [int1[0], max(int1[1], int2[1])]
    print(new_int[1] - new_int[0] + 1)
