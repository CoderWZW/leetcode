# -*- coding: utf-8 -*-
'''
思路：
dp[i][j]: 在背包大小为i的情况下，针对第j个物品后的总价值
dp[i][j][0]: 第j个物品后不放入背包后的总价值
dp[i][j][1]: 第j个物品后放入背包后的总价值

'''

# 0-1 背包问题
# weight , value , C
def bag(w, v, C):
    dp = [[0 for i in range(C+1)] for i in range(len(w))]
    # 先给第一个物品赋值
    for i in range(C+1):
        if w[0] <= i:
            dp[0][i] = v[0]
    for i in range(1, len(w)):
        for j in range(C+1):
            # 一种情况是当前的物品不放进背包，一种情况是当前物品放进背包
            one = dp[i-1][j]
            if j-w[i] >= 0:
                two = dp[i-1][j-w[i]]+v[i]
            else:
                two = 0
            dp[i][j] = max(one, two)
    print(dp)
    return max(dp[-1])