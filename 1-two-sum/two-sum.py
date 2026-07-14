class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for i,j in enumerate(nums):
            current = j
            need = target - current
            if need in Dict:
                return [Dict[need],i]
            else:
                Dict[j]=i
