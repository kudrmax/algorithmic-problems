def foo():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    A, B, C, D = tuple(map(int, lines[0].split()))
    # print(A, B, C, D)

    if D <= B:
        return A

    return A + C * (D - B)


print(foo())
