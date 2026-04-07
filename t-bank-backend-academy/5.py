# with open('input.txt') as file:
#     lines = file.readlines()
# N, _ = map(int, lines[0].split())

N, M = map(int, input().split())


def create_graph(arr):
    graph = {}
    for A, B in arr:
        if A not in graph:
            graph[A] = set()
        graph[A].add(B)
    return graph

arr = []
for _ in range(M):
    arr.append(tuple(map(int, input().split())))
graph = create_graph(arr)


def is_loop(graph):
    color = {}
    ans = False
    for vertex in graph:
        color[vertex] = 'white'

    def is_loop_rec(vertex, graph, flag=False):
        color[vertex] = 'grey'
        if vertex in graph:
            for neighbour in graph[vertex]:
                if neighbour not in color or color[neighbour] == 'white':
                    flag = is_loop_rec(neighbour, graph, flag)
                elif color[neighbour] == 'grey':
                    flag = True
        color[vertex] = 'black'
        return flag

    for vertex in graph:
        if color[vertex] == 'white':
            is_loop = is_loop_rec(vertex, graph)
            ans = ans or is_loop
    return ans


def top_sort(graph):
    color = {}
    ans = []
    for vertex in graph:
        color[vertex] = 'white'

    def top_sort_rec(vertex, graph):
        color[vertex] = 'grey'
        if vertex in graph:
            for neighbour in graph[vertex]:
                if neighbour not in color or color[neighbour] == 'white':
                    top_sort_rec(neighbour, graph)
        color[vertex] = 'black'
        ans.append(vertex)

    for vertex in graph:
        if color[vertex] == 'white':
            top_sort_rec(vertex, graph)
    ans.reverse()
    return ans


for vertex in graph:
    if is_loop(graph):
        print('NO')
    else:
        print('YES')
        sorted_arr = top_sort(graph)
        arr_set = set(sorted_arr)
        for n in range(1, N + 1):
            if n not in arr_set:
                sorted_arr.append(n)
        print(*sorted_arr)
    break
