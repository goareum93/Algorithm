N = int(input())

if N % 5 == 0 or N % 3 == 0:
    if (N % 5) % 3 == 0:
        bag_5 = N//5
        print('bag_5 :', bag_5)

        bag_3 = bag_5//3
        print('bag_3 :', bag_3)

        bag_num = bag_5 + bag_3
        print('bag_num :', bag_num)
    else:
        bag_3 = N // 3
else:
    print(-1)
