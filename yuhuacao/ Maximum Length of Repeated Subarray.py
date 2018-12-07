"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3

Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

Note:
    1 <= len(A), len(B) <= 1000
    0 <= A[i], B[i] < 100
"""
"""
解体思路：采用动态规划的方法，维护矩阵DP，DP[i][j]代表以A[i-1]与B[j-1]结尾的公共字串的长度，公共字串必须以A[i-1]，B[j-1]结束，即当A[i-1] == B[j-1]时，DP[i][j] = DP[i-1][j-1] + 1; 当A[i-1] != B[j-1]时，以A[i-1]和B[j-1]结尾的公共字串长度为0,DP[i][j] = 0。输出最大的公共字串的长度即为最长重复字串。 
"""

class Solution(object): 
	def findLength(self, A, B): 
		"""
    	:type A: List[int]
        :type B: List[int]
        :rtype: int
        """ 
		n1,n2 = len(A),len(B) 
		dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)] 
		for i in range(1,n1+1): 
			for j in range(1,n2+1): 
				if A[i-1] == B[j-1]: 
					dp[i][j] = dp[i-1][j-1] + 1 
		return max(max(row) for row in dp)

