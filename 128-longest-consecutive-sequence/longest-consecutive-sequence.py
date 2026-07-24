class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = set(nums)
        count = 1
        result = []
        for num in sorted(sort):
            if num+1 in sort:
                count+=1
            else:
                result.append(count)
                count = 1
        return max(result,default=0)