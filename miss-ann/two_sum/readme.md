Leetcode 小安晋升分享（第一题哦）

# 两数之和

今天是小安开始Leetcode刷题的第一天，一定要加油o.废话不多，进入正文啦…@-@

## 题目描述
给定一个整数数组 *nums* 和一个目标值*target*，请你在该数组中找出和为目标值的两个**整数**。你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。[题目原址](https://leetcode-cn.com/problems/two-sum/solution/)
**示例**

> 给定 nums = [2, 7, 11, 15]，target = 9
> 因为 nums[0] +nums[1] =2+7 =9
> 所以返回 [0,1]

## 方法一：暴力解法

### 思想
暴力法很简单。遍历每个元素 xx，并查找是否存在一个值与 target - xtarget−x 相等的目标元素。

### 代码实现
【C实现】

```
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    static int a[2]={0,0};
    for (int i=0;i<numsSize;i++){
        for (int j=i+1;j<numsSize;j++){
           if(nums[j] == target - nums[i]){
               a[0]=i;
               a[1]=j;
               return a;}  
        }
    }
    return NULL;
}
```
【Java实现】

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] == target - nums[i]) {
                return new int[] { i, j };
            }
        }
    }
    throw new IllegalArgumentException("No two sum solution");
    }
}
```
【python实现】

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(len(nums) -i -1):
                if nums[i]+nums[i+j+1]==target:
                    return [i,i+j+1]
        return []
    
```
### 复杂度分析
 - 时间复杂度：$O(n^2)$， 对于每个元素，我们试图通过遍历数组的其余部分来寻找它所对应的目标元素，这将耗费$O(n)$的时间。因此时间复杂度为 $O(n^2)$。
 - 空间复杂度： $O(1)$
 
## 方法二：两遍哈希表
### 思想
为了对运行时间复杂度进行优化，我们需要一种更有效的方法来检查数组中是否存在目标元素。如果存在，我们需要找出它的索引。保持数组中的每个元素与其索引相互对应的最好方法是什么？哈希表。

通过以空间换取速度的方式，我们可以将查找时间从 O(n) 降低到 O(1)。哈希表正是为此目的而构建的，它支持以 **近似** 恒定的时间进行快速查找。我用“近似”来描述，是因为一旦出现冲突，查找用时可能会退化到 O(n)。但只要你仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为 O(1)。

一个简单的实现使用了两次迭代。在第一次迭代中，我们将每个元素的值和它的索引添加到表中。然后，在第二次迭代中，我们将检查每个元素所对应的目标元素 *target - nums[i]* 是否存在于表中。注意，该目标元素不能是 *nums[i]* 本身！
### 代码实现
【Java实现】

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);//将每个元素的值和他的索引添加到表中
        }
        for (int i = 0; i < nums.length; i++) {
            int tmp = target - nums[i];
            if (map.containsKey(tmp) && map.get(tmp) != i) {
            return new int[] { i, map.get(tmp) };
            }
        }
        throw new IllegalArgumentException("No two sum solution");//异常抛出
    }
}
```


### 复杂度分析

 - 时间复杂度：$O(n)$， 我们把包含有 $n$个元素的列表遍历两次。由于哈希表将查找时间缩短到 $O(1)$，所以时间复杂度为 $O(n)$。
 - 空间复杂度：$O(n)$， 所需的额外空间取决于哈希表中存储的元素数量，该表中存储了$n$ 个元素。 
## 方法三：一遍哈希表
### 思想
事实证明，我们可以一次完成。在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。如果它存在，那我们已经找到了对应解，并立即将其返回。
### 代码实现
【Java实现】

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int tmp = target - nums[i];
        if (map.containsKey(tmp)) {
            return new int[] { map.get(tmp), i };
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
    }
}
```
【python实现】

```
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None
        d ={}
        for i,item in enumerate(nums):
            tmp = target - item
            for key,value in d.items():
                if value == tmp:
                    return [i,key]
                
            d[i] = item 
        return None
    
```
### 复杂度分析

 - 时间复杂度：$O(n)$， 我们只遍历了包含有$n$个元素的列表一次。在表中进行的每次查找只花费 $O(1)$的时间。
 - 空间复杂度：$O(n)$， 所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存$n$个元素。
 

# Thanks
一起加油哦~~
