class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for i in range(len(nums)):
            count += 1
            if nums[i] == 0:
                count = 0
                
            if count > max_count:
                max_count = count
        return max_count
        