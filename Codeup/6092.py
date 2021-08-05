n = int(input())
a = input().split()

for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1,24):
    print(d[i], end=' ')
