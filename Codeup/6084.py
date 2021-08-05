h, b, c, s = map(int, input().split())
capacity = h*b*c*s*1/8/1024/1024
print('{:.1f}'.format(capacity), 'MB')