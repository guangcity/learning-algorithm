LeetCode 1 两数之和 
2018-12-05
代码提交地址 https://leetcode-cn.com/problems/two-sum/submissions/

算法分析：

方法1. 暴力查询,整体时间复杂度为O(n^2),空间复杂度为0. 由于python中的list对象实际上是链表，其查询效率为 O(n), 即这里的if 语句if num in nums复杂度为O(n),再结合列表循环次数n, 整体时间复杂度为O(n^2).

方法2. hash查询,整体时间复杂度为常数级别O(n),空间复杂度为O(n). 使用hash建立 item->index 的映射关系，通过 target-item 反向查找hash是否存在这个index，因为hash的查找时间是O(1)的时间复杂度，所以复杂度如下:

步骤  时间复杂度   空间复杂度
hash映射  n   n
反向寻找  1   1
总计  n   n

