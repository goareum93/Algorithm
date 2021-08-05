k = int(input()) # 교통비
N = int(input()) # 도시의 숫자
R = int(input()) # 도로의 숫자
    
road = [[0 for i in range(4)] for j in range(R)]
print(road)

for i in range(R):
    s, d, l, t = map(int, input().split())

#     if d == 0:
#         for i in range(l):
#             g[(x-1)][(y-1)+i] = 1
#     else:
#         for i in range(l):
#             g[(x-1)+i][(y-1)] = 1

# for i in range(h):
#     for j in range(w):
#         print(g[i][j],end=' ')
#     print()
