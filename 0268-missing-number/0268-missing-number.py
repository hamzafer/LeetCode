class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=0
        arraysum=0
        for i in range(1, len(nums)+1):
            total+=i
            if(i!=len(nums)+1):
                arraysum+=nums[i-1]
        return total-arraysum
            