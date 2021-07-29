## 함수 선언부
def selctionSort(ary):
    n = len(ary) # 4개
    for i in range(0, n-1): # 사이클 (큰 반복 3회)
        minIdx = i
        for k in range(i+1, n): # 작은 반복
            if (ary[minIdx] > ary[k]):
                