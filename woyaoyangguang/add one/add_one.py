'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例１：
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
'''

'''
思路：
将数组转化为数字,当输入数组时,通过对其循环，将每一个数字按照位数提出，
通过intNum=intNum*10+digits[i]　转化为对应顺位的数字,在此基础上
加上下一位,达到要求’在此基础上加一’.接下来的思路是想到怎么将数字，转换
为之前格式的数组，可以将数字转换为字符串，然后对其遍历，将对应位置上的
数字放到列表当中。
'''


class Solution:
    def plusOne(self,digits):
        '''

        :param digits: List[int]
        :return: List[int]
        '''
        #数组转化为数字
        intNum=0
        for i in range(len(digits)):
            intNum=intNum*10+digits[i]
        intNum+=1
        #数字转化为字符
        strNum=str(intNum)
        #字符转化为数组
        res=[]
        for i in range(len(strNum)):
            res.append((int(strNum[i])))
        return res



a=Solution()
b=a.plusOne([1,2,3,4])
print(b)