class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        s1_len = len(num1)
        s2_len = len(num2)
        if s1_len == 0 or s2_len == 0 or num1 == '0' or num2 == '0':
            return '0'
        res_list = [0 for i in range(s1_len+s2_len)]
        for i in range(s1_len):
            for j in range(s2_len):
                muti_num = int(num1[s1_len-i-1])*int(num2[s2_len-j-1])
                low = s1_len+s2_len-i-j-1
                print("----")
                print(low)
                high = s1_len+s2_len-i-j-2
                print(high)
                muti_num += res_list[low]
                res_list[low]=muti_num%10
                res_list[high]+=muti_num//10
        print(res_list)
        str_res = ''
        for i in range(len(res_list)):
            if res_list[i] != 0:
                for j in res_list[i:]:
                    str_res += str(j)
                return str_res







s = Solution()
num1 = "48"
num2 = "17"
t = s.multiply(num1,num2)
print(t)
