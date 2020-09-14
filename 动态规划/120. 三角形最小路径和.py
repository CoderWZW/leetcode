# -*- coding: utf-8 -*-
'''
题目：
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
'''

'''
思路：
状态为 f(i,j): 到第i行第j列的最短路径

这里有两种方式，从上往下，
状态转移方程为： 
if j == 0:
    f(i, j) += f(i-1, j)
elif j == len(triangle[i]):
    f(i, j) += f(i-1, j-1)
else:
    f(i, j) += min(f(i-1, j-1), f(i-1, j))

从下往上
f(i, j) += min(f(i+1, j+1), f(i, j+1))

明显从下往上是更好的，同时为了省下空间，我们直接用triangle直接来存数据
'''

class Solution:
    def minimumTotal(self, triangle):
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
        
test = [[2],[3,4],[6,5,7],[4,1,8,3]]
solution = Solution()
print(solution.minimumTotal(test))