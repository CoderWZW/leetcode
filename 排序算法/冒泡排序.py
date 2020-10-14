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

# -*- coding: utf-8 -*-
# """
# 题目：冒泡排序

# 思路：
# ·比较相邻的元素。如果第一个比第二个大，就交换他们两个
# ·对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对
# ·针对所有的元素重复以上的步骤，除了最后一个
# ·持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字比较
# """

# class Solution:
#     def bubbleSort(arr):
#         for i in range(1, len(arr)):
#             for j in range(0, len(arr)-i):
#                 if arr[j]>arr[j+1]:
#                     arr[j], arr[j+1] = arr[j+1], arr[j]
#         return arr
            
