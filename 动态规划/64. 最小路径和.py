# -*- coding: utf-8 -*-
'''
题目：
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
'''

'''
思路：
状态为 f(i,j): 到第i行第j列的最短路径和

状态转移方程为:
f(i, j) += min(f(i-1, j), f(i, j-1))

第一排和第一列只能由左边或者上面的数得到
'''

class Solution:
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])
        #先处理第一排和第一列
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for j in range(1, col):
            grid[0][j] += grid[0][j-1]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
        
test =[[1,3,1],[1,5,1],[4,2,1]]
solution = Solution()
print(solution.minPathSum(test))