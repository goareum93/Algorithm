n = int(input())
sum = 0
for i in range(n+1):
    if sum < n:
        sum += i
    else:
        break

print(i-1)