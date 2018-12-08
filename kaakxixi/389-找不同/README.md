LeetCode 389 两数之和 
2018-12-08
代码提交地址 https://leetcode-cn.com/problems/find-the-difference/submissions/

算法分析：

方法1.  hash比较, 整体时间复杂度为线性级别O(n),空间复杂度为O(n). 使用hash建立 item->count 的映射关系,这里的时间和空间复杂度都是线性的,
然后在遍历hash表中的元素,进行比较,时间复杂度也是O(n).

步骤  时间复杂度   空间复杂度
hash映射  2n   2n
键值比较  n   1
总计  n   n

方法2. 使用异或运算, 整体时间复杂度为O(n), 空间复杂度为0. 对字符串中的字符转换为数字后异或连乘2n次,整体时间复杂度为O(n).但不消耗空间建立hash表,
是更好的方法.