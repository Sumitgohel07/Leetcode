class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        left = [1]
        n = len(nums)
        for i in range(1,n+1):
            prod = prod * nums[i-1]
            left.append(prod)
        right = [1]
        prod = 1
        for i in range(n-2,-1,-1):
            prod = prod * nums[i+1]
            right.append(prod)
        final_list = []
        for i in range(n):
            temp = left[i]*right[n-i-1]
            final_list.append(temp)
        return final_list


