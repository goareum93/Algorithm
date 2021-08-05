h, w = map(int, input().split())
n = int(input())

g = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for i in range(l):
            g[(x-1)][(y-1)+i] = 1
    else:
        for i in range(l):
            g[(x-1)+i][(y-1)] = 1

for i in range(h):
    for j in range(w):
        print(g[i][j],end=' ')
    print()
