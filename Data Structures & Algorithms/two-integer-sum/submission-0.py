class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                if i in indexes or j in indexes:
                    continue

                if nums[i] + nums[j] == target:
                    indexes.extend([i,j])
        
        return indexes