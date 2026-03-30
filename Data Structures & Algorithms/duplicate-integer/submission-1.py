class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            for num2 in nums:
                if num == num2:
                    return True
        return False