class Solution(object):
    def containsDuplicate(self, nums):
        new_nums = set(nums)
        if len(nums) == len(new_nums):
            return False
        else:
            return True

        