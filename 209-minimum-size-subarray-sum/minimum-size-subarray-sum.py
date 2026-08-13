class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        window_sum = 0
        min_len = len(nums) + 1

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                length = right - left + 1
                if length < min_len:
                    min_len = length
                window_sum -= nums[left]
                left += 1

        return 0 if min_len == len(nums) + 1 else min_len