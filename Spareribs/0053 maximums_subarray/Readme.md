**目录**
- <a href="#tm">`题目: 最大子序和`</a>
- <a href="#ckda">`参考答案`</a>
    - <a href="#fa1">`方案1 遍历法`</a>
    - <a href="#fa2">`方案2 动态规划`</a>
- <a href="#grzj">`问题`</a>

	
<a id="tm"/>

# 题目: 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

<a id="ckda"/>

# 参考答案
首先，注意审题
1. 最大和的 **连续** 子数组
2. 子数组 **至少** 包含一个元素

<a id="fa1"/>

## 方案1 遍历法
### 【思路】
遍历 nums 数据，求和标记最大值。当和小于0的时候，重置和为0。
### 【实现】
```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 异常校验, 如果为空 列表 直接返回
        if nums == []:
            return 
        
        # 初始化变量 
        # _sum: 统计当前连续子数据之和, 默认值为【0】
        # _max: 标记子数据的最大值, 默认值为【列表第1个值】
        _sum = 0
        _max = nums[0]
        
        for num in nums: # 迭代获取 nums 的数据
            _sum += num
            _max = max(_max, _sum)
            
            # 直到出现 _sum 小于 0的时候，重置 _sum 的值为0
            if _sum < 0:
                _sum = 0
        return _max
```
### 【分析】
假设 nums 长度为n
时间复杂度：O(n)
空间复杂度：O(n)

<a id="fa2"/>

## 方案2 动态规划
### 【思路】
假设sum[i]是第i个元素结尾的最大连续子数组和，那么sum[i-1]是第i-1个元素结尾的最大连续子数组和，对于整个计算结果而言，要么就是sum[i-1]是最优的结果，要么sum[i]是最优结果。实际上这个操作相当于方案1中的“当和小于0的时候，重置和为0”。
这里不再开辟新的空间，直接使用 nums 列表的空间，存储sum[i]
### 【实现】
```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 异常校验, 如果为空 列表 直接返回
        if nums == []:
            return 
        
        for i in range(1, len(nums)):  
            # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和  
            _max = max(nums[i] + nums[i-1], nums[i])  
            nums[i]= _max # 将当前和最大的赋给nums[i]，新的nums存储的为和值  
        return max(nums)
```
### 【分析】
假设 nums 长度为n
时间复杂度：O(n)
空间复杂度：O(n)

<a id="wt"/>

# 问题
1. 时间复杂度和空间复杂度的计算方法需要总结。

博客地址：[LeetCode刷题日记](https://blog.csdn.net/q370835062/column/info/30688) 欢迎关注，留言~~~
