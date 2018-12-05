class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 定义边界
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        # 去空格
        str_new = str.strip()

        # 定义最终结果字符
        saved_s = ''
        # 字符为空或开头直接为非字符
        if len(str_new)==0 or str_new[0].isdigit()==False and str_new[0]!='-' and str_new[0]!='+':
            return 0
        # 遍历
        for i in range(len(str_new)):
            # 首位有+-号时,让+-号存储到最终结果字符里面
            if str_new[i] == '+' or str_new[i] == '-' or str_new[i].isdigit():
                saved_s+=str_new[i]
                # 判断下一个是否为数字
                if i + 1 < len(str_new) and str_new[i + 1].isdigit() == False:
                    break
        # 最终结果字符只有+-,直接返回0
        if saved_s=='+'or saved_s=='-':
            return 0
        # 获取数字结果
        number = int(saved_s)
        # 判断是否越界
        if number>INT_MAX:
            return INT_MAX
        elif number<INT_MIN:
            return INT_MIN
        else:
            return number


s = Solution()
a = s.myAtoi('-15')
print(a)

