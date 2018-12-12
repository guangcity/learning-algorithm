#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = "vdlkdk"
dict = {}
num = 0
out = 0
flag = 0
i = 0
#暴力法1：找到所有不重复的字符串
'''
for i in range(0,len(s)) :
    dict[s[i]] = i
    num += 1
    for j in range(i+1,len(s)) :
        if s[j] in dict :
            break
        dict[s[j]] = j
        num += 1
    out = [num, out][out > num]
    if out >= len(s) / 2 :
        break
    dict.clear()
    num = 0
'''

#暴力法2：从输出长度out入手
'''
for out in range(0,len(s)):
    for i in range(0,out+1):
        for j in range(i,i+len(s)-out):
            if s[j] in dict:
                dict.clear()
                break
            dict[s[j]] = j
        else:
            flag = 1
        if flag == 1:
            break
    if flag == 1:
        break

print len(s)-out
'''
#滑动法，当往右滑动到右重复字符时，从前面重复的那个字符后开始搜索，不断循环
'''
n = len(s)
while i < n:
    if s[i] in dict:
        i = dict[s[i]] + 1
        out = [num, out][out > num]
        num = 0
        dict.clear()
        dict[s[i]] = i
        num += 1
        i += 1
        continue
    dict[s[i]] = i
    num += 1
    i += 1
out = [num, out][out > num]
'''

