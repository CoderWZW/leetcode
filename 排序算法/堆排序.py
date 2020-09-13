# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

'''
思想：
升序
建立最大堆，每三个数把最大的放在最上面，把最小的放在左子节点，
'''

#堆排序
#性质一：索引为i的左孩子的索引是 (2*i+1);
#性质二：索引为i的左孩子的索引是 (2*i+2);
#性质三：索引为i的父结点的索引是 floor((i-1)/2);

#针对一个父节点来比较，使父节点的值大于两个子节点

def max_heap(l, start, end):
    root = start
    while 1:
        child = root*2 + 1
        #可能child 超出边界
        if child > end:
            return
        #如果左子节点小于右子节点, 且右子节点存在（即不超出范围）
        if child+1 <= end:
            if l[child] < l[child+1]:
                child += 1
        #如果根节点小于子节点，则交换
        if l[child] > l[root]:
            l[child], l[root] = l[root], l[child]
            root = child
        #如果没有小于子节点的情况，则终止
        else:
            return

def heap_sort(l):
    #先遍历非叶子节点
    length = len(l) // 2 - 1
    for root in range(length, -1, -1):
        max_heap(l, root, len(l)-1)
    #遍历最后一个值与第一个值交换位置，然后对根节点进行比较，使根节点最大
    for end in range(len(l)-1, 0, -1):   #最后不用遍历根节点，已经排好了
        l[0], l[end] = l[end], l[0]
        max_heap(l, 0, end-1)
    return l

print(heap_sort(l))
                
            