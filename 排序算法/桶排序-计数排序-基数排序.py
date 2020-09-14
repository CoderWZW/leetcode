# -*- coding: utf-8 -*-

l = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
l_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

def count_sort(l):
    dic = {}
    max_value = 0
    min_value = 0
    for i in l:
        if i > max_value:
            max_value = i
        elif i < min_value:
            min_value = i
        else:
            continue
    for i in range(min_value, max_value+1):
        dic[i] = 0
    for i in l:
        dic[i] += 1
    l_new = []
    for i in dic.keys():
        for j in range(dic[i]):
            l_new.append(i)
    return l_new

#桶排序
#先将不同的数放入不同的桶
def bucket_sort(l):
    tmp = [[] for i in range(10)]
    #制定分桶规则
    for i in l:
        a = i // 10
        tmp[a].append(i)
    l_new = []
    for i in tmp:
        l_new += sorted(i)
    return l_new

#基数排序
#先个位，再十位，再百位
def radix_sort(l):
    i = 0 # 记录当前正在排拿一位，最低位为1
    max_num = max(l)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in l:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        l.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                l.append(y)
        i += 1
    return l

print(radix_sort(l))
                
            