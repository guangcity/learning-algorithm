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


