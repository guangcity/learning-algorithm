#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        dict_1 = {}

        while 1:
            sum = 0

            while n != 0:  #计算平方之和
                sum += (n % 10) ** 2
                n /= 10

            n = sum

            if n == 1:   #如果平方之和为1，证明n是快乐数，返回True
                return True
            elif dict_1.has_key(n):  #若平方之和已出现过（循环计算），证明加法之和不可能为1，n不是快乐数，返回False
                return False

            dict_1[n] = 0

