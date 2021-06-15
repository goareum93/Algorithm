# https://www.acmicpc.net/problem/10815
# 10815번 숫자 카드

# <문제>
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# <입력>
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
#
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며,
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# <출력>
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

n = int(input())
n_num = list(map(int, input().split()))
n_num.sort()

def binary_search(m_num):
    pl = 0
    pr = n-1
    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스
        if n_num[pc] == m_num:
            return 1        # 검색 성공
        elif n_num[pc] < m_num:
            pl = pc + 1     # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc -1      # 검색 범위를 앞쪽 절반으로 좁힘

        if pl > pr:
            break
    return 0

m = input()
for m_num in list(map(int, input().split())):
    print(binary_search(m_num), end = ' ')

# 답 제출 링크 : https://www.acmicpc.net/source/30069373