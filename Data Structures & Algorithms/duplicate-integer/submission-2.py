class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for i2 in range(len(nums)):
                if i == i2:
                    continue
                if nums[i] == nums[i2]:
                    return True
        return False