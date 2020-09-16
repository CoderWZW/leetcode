# -*- coding: utf-8 -*-
'''
题目：
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
'''

'''
思路：

状态为 f(i): 字符串s[:i+1] 所能解码的数量
注意：这里需要考虑两种情况，
一种是第i位不为0时，就一定能增加f(i-1)次数
一种是（第i-1位+第i位）, 需要考虑两位加起来在10-26之间，才能增加f(i-2)次数

状态转移方程为：
f(i) += f(i-1) if s[i] != 0 else 0
f(i) += f(i-2) if [i-1:i+1] >= '10' and [i-1:i+1] <= '26' else 0

这里用了一个trick：res相对于s的index考虑往后延了一位，否则会超出阈值
'''

class Solution:
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0
        res = [0 for i in range(n+1)]
        res[0] = 1
        res[1] = 1 if s[0] != '0' else 0
        for i in range(1, n):
            res[i+1] += res[i] if s[i] != '0' else 0
            res[i+1] += res[i-1] if s[i-1:i+1] >= '10' and s[i-1:i+1] <= '26' else 0
        return res[-1]
        
test = "10"
solution = Solution()
print(solution.numDecodings(test))