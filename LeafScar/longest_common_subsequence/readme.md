<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Longest Common Subsequence
	问题：A_1
	1)子序列：对于任一序列A=a1a2a3...an,删除其中若干项，剩余的序列叫作A的子序列
		对于一个长度为n的子序列，共有2^n个子序列
	2)公共子序列：如果一个序列C即是序列A的子序列，又是序列B的子序列，则称C为序列A和序列B的公共子序列
	3)序列A与序列B的公共子序列中，长度最长的公共子序列叫作序列A和序列B的最长公共子序列

	现给定长度为n的序列A与长度为m的序列B，求它们的最长公共子序列
#### 方法1.以递归的方式求解
	先设定函数的参数
	
###### 0）