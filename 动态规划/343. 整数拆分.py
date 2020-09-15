# -*- coding: utf-8 -*-
'''
题目：
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
'''

'''
思路：
注意：此题n最小为2，同时拆分为至少两个正整数。
状态为 f(i): 数字i被拆分后的最大乘积

状态转移方程为：
f(i) = max(f(i-x)*x, f(i), i * (i-x))
三种情况取最大：本身，分离出的数字x和（当前数-x），分离出的数字x和f(i-x)
'''

class Solution:
    def integerBreak(self, n):
        result = [-1 for i in range(n+1)]
        result[1] = 1
        result[2] = 1
        for i in range(3, n+1):
            tmp = 0
            for j in range(1, i):
                tmp = max(tmp, (i-j)*j, result[i-j]*j)
            result[i] = tmp
        return result[-1]
        
test = 10
solution = Solution()
print(solution.integerBreak(test))