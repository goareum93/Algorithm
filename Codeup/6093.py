n = int(input())
a = input().split()

for i in range(n-1, -1, -1) :  #0부터 n-1까지...
  print(a[i], end=' ')       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장
