# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

# 冒泡排序

'''
思想：
升序
不断的按顺序遍历，如果左边的数字比右边的数字大，就交换顺序
'''


def bubble_sort(l):
    while 1:
        # flag 用来记录此次遍历是否交换顺序
        flag = 0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                flag = 1
        if flag == 0:
            break
    return l

print(bubble_sort(l))
                
            