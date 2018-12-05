class Solution:
    def isValid(self,s):
        dict = {')': '(', '}': '{', ']': '['}
        l = [None]
        for i in s:
            if i in dict and dict[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l) == 1


s = Solution()
t = "{[]}"
res = s.isValid(t)
print(res)
