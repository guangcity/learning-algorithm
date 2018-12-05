class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_match = {'{':'}','[':']','(':')'}
        stack=[]
        for str in s:
            if str == '{' or str == '[' or str== '(':
                stack.append(str)
            else:
                # 无左括号，只有右括号，直接返回False
                if len(stack)==0:
                    return False
                # 栈顶元素对应的字符串是否匹配当前字符
                if stack_match[stack.pop()]!=str:
                    return False
        flag = True if len(stack)==0 else False

        return flag

s = Solution()
t = "{[]}"
res = s.isValid(t)
print(res)
