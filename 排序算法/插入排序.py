# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]


'''
思想：
升序
不断的按顺序遍历，将当前值与前面的值依次比较，插入该值所在位置
'''

# 直接插入排序
# 思路：依次遍历，倒序遍历已经排好序的list，比较后如果目标值大于遍历值，则插入在该遍历值index+1的位置
def insert_sort(l):
    l_new = [l[0]]
    for i in range(1,len(l)):
        temp = l[i]
        flag = 0
        for j in range(len(l_new)-1, -1, -1):
            if temp >= l_new[j]:
                l_new.insert(j+1, temp)
                flag = 1
                break   # break 很关键，否则就会每次都遍历所有的排序好的数字
        if flag == 0:
            l_new.insert(0, temp)
    return l_new            

print(insert_sort(l))
                
            