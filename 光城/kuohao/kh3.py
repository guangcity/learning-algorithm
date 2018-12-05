class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_len=0
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack_len+=1
                stack.append(i)
            else:
                if stack and i==')' and stack[-1]=='(':
                    stack.pop()
                    stack_len-=1
                elif stack and i=='}' and stack[-1]=='{':
                    stack.pop()
                    stack_len-=1
                elif stack and i==']' and stack[-1]=='[':
                    stack.pop()
                    stack_len-=1
                else:
                    return False
        return stack_len==0


s = Solution()
t = "(]"
res = s.isValid(t)
print(res)
