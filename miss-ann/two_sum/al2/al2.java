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
