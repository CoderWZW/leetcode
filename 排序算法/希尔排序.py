# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

'''
思想：
插入排序可以在有序的list上表现更好
按固定间隔生成新的list，用插入排序，不断的缩小间隔，最后实则还是用插入排序进行排序
'''

# 插入排序
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

# 希尔排序
def shell_sort(l):
    distance = int(len(l)/2)    #distance 记录分组数据之间的间隔， 如，1， 1+distance, 1+2*distance
    num = int(len(l)/ distance)   #num 记录每一组分组数据的个数
    while 1:
        for i in range(distance):
            tmp = []
            for j in range(num):
                tmp.append(l[distance*j+i])
            tmp = insert_sort(tmp)
            for j in range(num):
                l[distance*j+i] = tmp[j]
        distance = int(distance/2)
        if distance == 0:
            return l
        num = int((len(l) / distance))
        
print(shell_sort(l))
