int findMin(int* nums, int numsSize) {
    int L=0;
    int R=numsSize-1;
    int mid;
    if(numsSize==1)
        return nums[0];
    if(numsSize==2)
        if(nums[0]<nums[1])
            return nums[0];
        else
            return nums[1];
    if(nums[0]<nums[numsSize-1])
        return nums[0];

    while(1)
    {
        mid = (L+R)/2;
        if(nums[mid]>nums[L]&&nums[mid]>nums[R])
            L=mid;
        else if(nums[mid]<nums[L]&&nums[mid]<nums[R])
            R=mid;
        if(nums[mid]<nums[mid+1]&&nums[mid]<nums[mid-1])
            break;
        if(R-L<=1)
            if(nums[L]>nums[L+1]&&nums[L]>nums[L-1])
                return nums[L+1];
    }
    return nums[mid];
}