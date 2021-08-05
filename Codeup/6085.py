w, h, b = map(int, input().split())
capacity = w*h*b/8/1024/1024
print('{:.2f}'.format(capacity), 'MB')