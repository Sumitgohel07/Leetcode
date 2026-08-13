class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        else:
            left = 0 
            window_sum = 0
            min_len = len(nums) + 1
            for right in range(len(nums)):
                window_sum += nums[right]
                while window_sum >= target:
                    min_len = min(min_len,right-left+1)
                    window_sum -= nums[left]
                    left += 1        
            return min_len