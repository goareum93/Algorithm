n = int(input())
a = input().split()

for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])    

print(min(a))