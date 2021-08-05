a, m , d, n = map(int, input().split())
total = a
for i in range(n-1):
    total = total*m+d
    
print(total)