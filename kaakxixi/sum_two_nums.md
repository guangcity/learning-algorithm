算法分析：

方法1. 整体时间复杂度为O(n^2). 由于python中的list对象实际上是链表，其查询效率为 O(n), 即这里的if 语句if num in nums复杂度为O(n),
再结合列表循环次数n, 整体时间复杂度为O(n^2).

方法2. 整体时间复杂度为常数级别O(1). 使用散列hash表(python中的dict和set), 将差值target - nums[i]作为dict的键, 索引 i 作为dict的值, 判断列表中的值是否在dict中, 这里对hash表中的元素的访问是常数时间级别.

