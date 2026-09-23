class Solution(object):
    def productExceptSelf(self, nums):
        left=[1]*len(nums)
        right=[1]*len(nums)
        for i in range (1,len(nums)):
            left[i]=nums[i-1]*left[i-1]
        
        for j in range ((len(nums)-2),-1,-1):
            right[j]=nums[j+1]*right[j+1]

        for k in range(len(left)):
            right[k]=right[k]*left[k]
        
        return right
