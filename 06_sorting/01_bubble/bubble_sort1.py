# 버블 정렬 알고리즘 구현하기

from typing import MutableSequence
# 시퀀스의 특징
# 데이터를 순서대로 하나씩 나열하여 나타낸 데이터 구조다.
# 특정 위치(~번째)의 데이터를 가리킬 수 있다.

# MutableSequence : list의 제네릭 버전.

def bubble_sort(a: MutableSequence) -> None:
    # None은 값이 없음을 나타내는 값이다. 함수의 반환값을 지정하지 않으면 None이 반환된다.
    """버블 정렬"""

    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))


    bubble_sort(x)  # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
