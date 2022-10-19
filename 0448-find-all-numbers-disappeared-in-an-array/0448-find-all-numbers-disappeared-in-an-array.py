class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {i:i for i in nums}
        result = []
        for i in range(1, len(nums)+1):
            if not i in hashMap.keys():
                result.append(i)
        return result