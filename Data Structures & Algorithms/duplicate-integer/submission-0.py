class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        if len(nums) > 2:
            split = len(nums) // 2
            return self.hasDuplicate(nums[:split]) or self.hasDuplicate(nums[split:])

        if len(nums) == 2:
            return nums[0] == nums[1]
        
        return False