# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

'''
思想：
升序
找到一个对照数（比如第一个），遍历整个list，把小于对照数的放在左边，把大于对照数的放在右边，不断的递归
'''


# 不额外申请空间
def quick_sort1(l, start, end):
    i = start
    j = end
    if i >= j:
        return l
    flag = l[start]
    #小于基数的在左，大于基数的在右
    while i < j:
        while flag <= l[j] and i < j:
            j -= 1
        l[i] = l[j]
        while flag >= l[i] and i < j:
            i += 1
        l[j] = l[i]
    #基数放在该放的位置上
    l[i] = flag
    # 除去i之外两段递归
    quick_sort1(l, i+1, end)
    quick_sort1(l, start, i-1)
    return l




# 额外申请空间
def quick_sort(l):
    if len(l) <= 1:
        return l
    temp = l[0]
    left, right = [], []
    l.remove(temp)
    for i in l:
        if i <= temp:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [temp] + quick_sort(right)

#print(quick_sort(l))
print(quick_sort1(l, 0, len(l)-1))
print(l_out)
                
            