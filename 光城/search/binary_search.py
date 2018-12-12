class BS:
    def search(self,nums,target):
        return self.bsearch(nums,0,len(nums)-1,target)
    def bsearch(self,nums,low,high,target):
        while(low<=high):
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low=mid+1
            elif nums[mid] > target:
                high=mid-1
        return None
nums = [9,5,7,0,1,2,3,12]
target = 0
bs = BS()
print(bs.search(nums,target))