d = [[0 for j in range(19)] for i in range(19)]

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)-1][int(y)-1] = 1

for i in range(19) :
  for j in range(19) : 
    print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
  print()                          #줄 바꿈


