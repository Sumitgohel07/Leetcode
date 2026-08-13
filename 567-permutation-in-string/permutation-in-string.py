class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = dict()

        for i in s1:
            s1_count[i] = s1_count.get(i, 0) + 1

        left = 0
        right = len(s1)
        temp_count = dict()
        flag = 1
        while right <= len(s2):
            if flag == 1:
                for i in range(left,right):
                    temp_count[s2[i]] = temp_count.get(s2[i], 0) + 1
                    flag = 0

            if s1_count == temp_count:
                return True
            else:
                temp_count[s2[left]] -= 1
                if temp_count[s2[left]] == 0:
                    del temp_count[s2[left]]
                if right < len(s2):
                    temp_count[s2[right]] = temp_count.get(s2[right],0) + 1
            left += 1
            right += 1

        return False