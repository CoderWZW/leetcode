# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

'''
思想：
升序
递归，将list分成n组，先2个一组，再4个，6个.....
每个组从左往右依次比较，因为先是2个排过了，所以一定是有序的
'''

def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = int(len(l) / 2)
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    l_new = []
    # left和right都是有序的，依次比较最小的
    while left and right:
        if left[0] >= right[0]: 
            l_new.append(right.pop(0))
        else:
            l_new.append(left.pop(0))
    if left:
        l_new += left
    if right:
        l_new += right
    return l_new
        
print(merge_sort(l))
                
            