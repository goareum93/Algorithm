def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

# 전역 변수 부
SIZE = 5
queue = [None for _ in  range(SIZE)]
front = rear = -1

# 메인 코드 부
print('큐가 비어있는지 여부 ==>',isQueueEmpty())