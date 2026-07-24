class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num_set = set(nums)
        # result = 0
        # for num in num_set:
        #     if num-1 not in num_set:
        #         count = 1
        #         current = num
        #         while current+1 in num_set:
        #             count+=1
        #             current+=1
        #         result = count if count>result else result
        # return result

        sort  = set(nums)
        count = 1
        result = []
        for num in sorted(sort):
            if num+1 in sort:
                count+=1
            else:
                result.append(count)
                count = 1
        return max(result,default=0)