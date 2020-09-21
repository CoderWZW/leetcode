# -*- coding: utf-8 -*-
'''
题目：
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
'''

'''
思路：
状态为 f[i] 为 表示第 i 天结束之后的「累计最大收益」
我们目前持有一支股票，对应的「累计最大收益」记为 f[i][0]；
我们目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为 f[i][1]；
我们目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为 f[i][2]。

状态转移方程为：
f[i][0]=max(f[i−1][0],f[i−1][2]−prices[i])
f[i][1]=f[i−1][0]+prices[i]
f[i][2]=max(f[i−1][1],f[i−1][2])

注意到如果在最后一天（第 n-1 天）结束之后，手上仍然持有股票，那么显然是没有任何意义的。因此更加精确地，最终的答案实际上是 f[n-1][1] 和 f[n-1][2] 中的较大值
'''

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        dp = [[0,0,0] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[n - 1][1], dp[n - 1][2])
        
        
test = [1,2,3,0,2]
solution = Solution()
print(solution.maxProfit(test))