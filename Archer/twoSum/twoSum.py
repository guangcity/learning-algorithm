#!/usr/bin/env python
# -*- coding:utf-8 -*-

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # 解法1，将数组中所有元素依次相加，计算量o((n^2)/2)
    ''' 
    k = len(nums)

    for i in range(0,k-1):
        for j in range(i+1,k):
            if nums[i] + nums[j] == target:
                return [i,j]
    '''
    # 解法2，用目标和target去减数组中的元素，然后再把另一个加法项找出来，计算量o((n^2)/2)，
    '''
    k = len(nums)

    for i in range(0,k-1):
        temp = target - nums[i]
        for j in range(i+1,k):
            if temp == nums[j]:
                return [i, j]
    '''

    # 解法3，用哈希表，空间换时间，第一次循环将数组的值放入哈希表中，第二次循环从哈希表中取出值(待完善)

    map_a = dict()

    k = len(nums)
    for i in range(0, k):
        map_a[nums[i]] = (i,nums[i])

    print map_a.items()

    for i in range(0, k):
        temp = target - nums[i]
        if temp in map_a and map_a[temp][0]!=i:
            return [map_a[temp][0], i]
    print "No two sum solution"

    # 解法4，用哈希表，一边把数组元素放到哈希表中，一边判断哈希表中是否有满足和的两个整数（待完善）
    '''
    map_a = dict()
    k = len(nums)

    for i in range(0, k):
        map_a[nums[i]] = (i, nums[i])
        print map_a.items()
        temp = target - nums[i]
        if temp in map_a and map_a[temp][0]!=i:
            return [map_a[temp][0], i]
    '''
