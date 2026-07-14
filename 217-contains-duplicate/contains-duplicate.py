class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i,j in enumerate(nums):
            if j in my_dict:
                my_dict[j] += 1
                return True
            else:
                my_dict[j] = 1
        return False