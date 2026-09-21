class Solution(object):
    def twoSum(self, nums, target):
        start = 0
        end = len(nums)-1
        index=[]
        sorted_nums=nums[:]
        sorted_nums.sort()

        while start < end :
            if (sorted_nums[start]+sorted_nums[end])>target:
                end -= 1
            elif (sorted_nums[start]+sorted_nums[end])<target:
                start += 1
            else :
                break
        
        for i in range (len(nums)):
            if sorted_nums[start]==nums[i]:
                index.append(i)
            elif sorted_nums[end]==nums[i]:
                index.append(i)
        return index


        