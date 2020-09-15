# -*- coding: utf-8 -*-
'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
'''

'''
思路：
注意：此题n最小为2，同时拆分为至少两个正整数。
状态为 f(i): 组成数字i需要的平方数的个数

状态转移方程为：
f(i) = min(f(i-x)+1, f[i])
三种情况取最大：本身，分离出的数字x和（当前数-x），分离出的数字x和f(i-x)
'''

import math
class Solution:
    def numSquares(self, n):
        res = [n+1 for i in range(n+1)]
        res[0] = 0  # 这里要设0 为0个，考虑数字本身为平方数的情况
        res[1] = 1 
        for i in range(2, n+1):
            tmp = n+1
            sqrt = int(math.sqrt(i))
            for j in range(1, sqrt+1):
                tmp = min(tmp, res[i-j*j]+1)
            res[i] = tmp
        return res
        
test = 13
solution = Solution()
print(solution.numSquares(test))