int findMin(int* nums, int numsSize) {
    int L=0;
    int R=numsSize-1;
    int mid;
    while(L<R)
    {
        mid = (L+R)/2;
        if(nums[mid]>nums[R])
            L=mid+1;
        else if(nums[mid]<nums[R])
            R=mid;
    }
    return nums[L];
}