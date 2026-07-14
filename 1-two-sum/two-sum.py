class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i,j in enumerate(nums):
            need = target - j
            if need in my_dict:
                return [my_dict[need],i]
            else:
                my_dict[j]=i
