class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = dict()
        for i in s1:
            s1_count[i] = s1_count.get(i,0)+1
        left = 0
        right = len(s1)
        window_list = []
        while right <= len(s2):
            temp_count = dict()
            word = s2[left:right]
            window_list.append(word)
            for i in word:
                temp_count[i] = temp_count.get(i,0)+1
            if s1_count == temp_count:
                return True
            left+=1
            right+=1
        return False

            