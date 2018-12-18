#!/usr/bin/env python
# -*- coding:utf-8 -*-


s = ""
set0 = set()
dict = {}
num = 0
out = 0
flag = 0
i = 0
j = 0

n = len(s)


# 索引i和j分别表示子字符串的起始和结束，如何有相同的字符，则一直把前面的删掉，知道没有重复为止
'''
while i<n and j<n:
    if (s[j] in dict) == False :
        dict[s[j]] = j
        j += 1
        out = [j-i,out][out>(j-i)]
    else :
        del dict[s[i]]
        i += 1
'''
# 直接找字符串，用find，如果找到，先得到字符串大小，再把索引i往前移到找到的索引，优点是不用一直把前面的删掉，进一步优化效率

j = 1
i = 0


while j<n :
    cur = s.find(s[j],i,j)
    if cur != -1:
        out = max(j-i,out)
        i = cur+1
    j += 1

if n != 0:
    out = max(j-i,out)
else :
    out = 0

print out