class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinctSet = set(nums)
        return len(distinctSet) != len(nums)
    
        