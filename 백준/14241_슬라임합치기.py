N = int(input())
num = list(map(int,input().split()))
num.sort(reverse=True) #큰 수부터 정렬
print('num : ',num)
result = 0
total = 0

for i in range(0,N-1):
    result = num[i] * num[i+1]
    print('result : ', result)
    num[i+1] = num[i] + num[i+1]
    print('num2 : ',num)
    total=total + result
print(total)