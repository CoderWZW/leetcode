# -*- coding: utf-8 -*-
'''
题目：
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
'''

'''
思路：
注意：此题为198 打架劫舍的加强版，其实就是加了限制条件，每次偷只能首尾两个房子偷一个。

'''

class Solution:
    def rob198(self, nums):
        n = len(nums)
        res = [0 for i in range(n+1)]
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        res[1] = nums[0]
        for i in range(1, n):
            res[i+1] = max(res[i], res[i-1]+nums[i])
        return res[-1]
    
    def rob(self, nums):
        n = len(nums)
        if n == 0 and n == 1 and n == 2:
            return 0
        return max(self.rob198(nums[1:]), self.rob198(nums[:-1]))
        
test = [1,2,3,1]
solution = Solution()
print(solution.rob(test))