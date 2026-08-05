class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        lmax = 0
        rmax = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            if height[left]<=height[right]:
                lmax = max(lmax,height[left])
                result += lmax-height[left]
                left+=1
            else:
                rmax = max(rmax,height[right])
                result += rmax-height[right]
                right-=1
        return result
