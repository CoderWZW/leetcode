# -*- coding: utf-8 -*-
'''
题目：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii\
'''

'''
思路：

状态为 f(i,j): 走到第(i,j)位时可以有的次数
注意：这里由于多了障碍物，所以需要额外考虑


状态转移方程为：
如果是障碍物，不管，如果不是障碍物，就等于f(i-1,j)+f(i, j-1)

'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        # 处理第一格
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        obstacleGrid[0][0] = 1
        # 处理第一行和第一列
        for j in range(1, col):
            if obstacleGrid[0][j] == -1:
                obstacleGrid[0][j:col] = [-1 for i in range(j,col)]
                break
            else:
                obstacleGrid[0][j] = obstacleGrid[0][j-1]
        for i in range(1, row):
            if obstacleGrid[i][0] == -1:
                for j in range(i, row):
                    obstacleGrid[j][0] = -1
                break
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == -1:
                    continue
                else:
                    obstacleGrid[i][j] +=  obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != -1 else 0
                    obstacleGrid[i][j] +=  obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != -1 else 0
        return obstacleGrid[-1][-1] if obstacleGrid[-1][-1]!=-1 else 0
                
test = [[0,0,0],[0,1,0],[0,0,0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(test))