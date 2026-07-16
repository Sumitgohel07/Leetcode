class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            x = "".join(sorted(word))
            if x in my_dict:
                my_dict[x].append(word)
            else:
                my_dict[x] = [word]
        return list(my_dict.values())
