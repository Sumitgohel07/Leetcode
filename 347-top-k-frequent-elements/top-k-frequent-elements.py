class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for key in nums:
            if key not in my_dict:
                my_dict[key] = 1
            else:
                my_dict[key] += 1
        result = []
        for i in range(k):
            temp = max(my_dict,key = my_dict.get )
            result.append(temp)
            del my_dict[temp]
        return result
            


        # sorted_item = sorted(my_dict.items(),key = lambda x : x[1],reverse=True)
        # freq_list = []
        # for key,value in sorted_item:
        #     freq_list.append([key,value])
        # result = []
        # for i in range(k):
        #     result.append(freq_list[i][0])
        # return result

