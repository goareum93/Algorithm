def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print("스택 꽉!")
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    # 비었는지 체크
    #데이터를 추출해서 리턴
    if (isStackEmpty()):
        print("스택 빔!")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

SIZE = 5
stack = ['커피',None,None,None,None]
top = 0

print(stack)
retData = pop()
print('추출한 데이터 -->', retData)
print(stack)
retData = pop()

