class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        sq = []

        while left < right:
            if abs(nums[left]) > abs(nums[right]):
                sq.append(nums[left] ** 2)
                left += 1
            else:
                sq.append(nums[right] ** 2)
                right -= 1

        sq.append(nums[left] ** 2)
        return sq[::-1]