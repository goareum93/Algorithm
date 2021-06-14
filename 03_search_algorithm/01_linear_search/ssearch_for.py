# for 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence # typing : Support for type hints
# Python 3.5부터 Type Hints라는 기능이 도입되었다. 이것은 (데이터)형에 관한 주석(데이터형 어노테이션)을 붙일 수 있는 것
# 예
# def greeting(name: str) -> str:
#     return 'Hello ' + name

# name: str : 인수 name이, str형이라는 것을 어노테이션한다.
# -> str : 함수 greeting의 반환값의 형이 str이라는 것을 어노테이션한다.

# Sequence 자료형에 속하는 객체는 문자열, 리스트, 튜플이 있다.
# 시퀀스(sequence)는 데이터에 순서(번호)를 붙여 나열한 것이다.

def seq_search(a: Sequence, key: Any) -> int: # -> int : 이거의 뜻은 이 함수가 반환해주는 값의 형식이 int라는 것을 말한다!
    # 모든 type은 Any의 서브타입이 된다. Any는 클래스의 object와는 다르기 때문에, 주의가 필요하다.

    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(for문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i # 검색 성공(인덱스를 반환)

    return -1        # 검색 실패(-1을 반환)

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: ')) # num값을 입력받음
    x = [None] * num                        # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: ')) # 검색할 키 ky를 입력받음

    idx = seq_search(x, ky)                  # ky와 값이 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')