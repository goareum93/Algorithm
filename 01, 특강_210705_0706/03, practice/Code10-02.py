def openBox() :
    global count
    print("박스 열기~~")
    count -= 1

    if count == 0 :
        print('#### 반지 넣기 ####')
        return
    openBox()
    print('박스 닫기!!!')

count = 10
openBox()	# 처음 함수를 다시 호출
