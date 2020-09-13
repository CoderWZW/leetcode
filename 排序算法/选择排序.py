# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

'''
思想：
升序
不断的按顺序遍历，记录最小的数字的index和value，然后放在新的list最前面
'''


def selection_sort(l):
    l_new = []
    while l:
        temp = [0, l[0]]
        for i in range(1, len(l)):
            if temp[1] > l[i]:
                temp = [i, l[i]]
        l_new.append(temp[1])
        del l[temp[0]]
    return l_new

print(selection_sort(l))
                
            