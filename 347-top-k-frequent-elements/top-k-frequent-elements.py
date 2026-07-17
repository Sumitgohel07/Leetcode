class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for key in nums:
            if key not in my_dict:
                my_dict[key] = 1
            else:
                my_dict[key] += 1
        my_dict = dict(sorted(my_dict.items(),key = lambda x : x[1],reverse=True))
        List = []
        for key,value in my_dict.items():
            List.append([key,value])
        result = []
        for i in range(k):
            result.append(List[i][0])
        return result

