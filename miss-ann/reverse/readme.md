# 整数反转
今天是小安开始Leetcode刷题的第七题，正文开始ing😎

## 题目描述
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。[题目原址](https://leetcode-cn.com/problems/reverse-integer/)
**示例**
【示例1】
> 输入: 123
> 输出：321

【示例2】
> 输入:  -123
> 输出：-321

【示例3】
> 输入: 120
> 输出：21

## 方法：暴力法

### 思想
利用x%10/x/10得到当前值，注意考虑的是负值情况以及值范围大小。
### 代码实现   

【python3实现】
```
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            res = int(str(x)[::-1])
            if -2**31 <= res <=2**31-1 :
                return res
            else:
                return 0
        else:
            res = int(str(abs(x))[::-1])#非纯数字组成的字符串转换问题
            if res<=2**31-1:
                return -res
            else:
                return 0
```
【java实现】
```
class Solution {
    public int reverse(int x) {
        long res=0;
        while(x!=0){
            res = res*10+x%10;
            x/=10;
    }
        if(res>Integer.MAX_VALUE || res<Integer.MIN_VALUE){
            return 0;}
        return (int)res;
    }}
            
```
【c实现】

```
int reverse(int x) {
    long res=0;
    while(x!=0){
        res=res*10+x%10;
        x/=10;
    }
    int flog1=0x7fffffff;
    int flog2=0x80000000;
    if(res<flog2||res>flog1){
        return 0;
    }
   return (int)res; 
    
}
```

