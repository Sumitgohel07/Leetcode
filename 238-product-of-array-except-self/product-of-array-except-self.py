class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        left = []
        for i in range(len(nums)):
            if i == 0:
                left.append(prod)
            else:
                prod = prod * nums[i-1]
                left.append(prod)
        right = []
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                right.insert(0,prod)
            else : 
                prod = prod * nums[i+1]
                right.insert(0,prod)
        final_list = []
        for i in range(len(nums)):
            temp = left[i]*right[i]
            final_list.append(temp)
        return final_list


