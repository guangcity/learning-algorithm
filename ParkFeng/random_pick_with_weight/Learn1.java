
class Solution {

    int[] arr;
    int maxOfArr;
    Random random = new Random();
    public Solution(int[] w) {
        arr = new int[w.length];
        arr[0] = w[0];
        for (int i = 1; i <arr.length; i++) {
            arr[i] = arr[i-1]+w[i];
        }
        maxOfArr = arr[arr.length-1];
    }

    public int pickIndex() {
        int rand = random.nextInt(maxOfArr)+1;
        int index = findIndex(arr, rand);
        return index;
    }

    private int findIndex(int[] nums, int m) {
        int start = 0;
        int end = nums.length-1;
        while (start+1 < end) {
            int mid = (start+end)/2;
            if (nums[mid] == m) {
                return mid;
            } else if (nums[mid] < m) {
                start = mid+1;
            } else {
                end = mid-1;
            }
        }
        if (m > nums[end]) {
            return end+1;
        } else if (m > nums[start]) {
            return start+1;
        } else {
            return start;
        }
    }
}