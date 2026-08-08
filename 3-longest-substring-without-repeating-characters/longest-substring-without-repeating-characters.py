class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        i = 0
        j=0
        while i <= j:
            j = i
            while j <= len(s)-1:
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    max_len = max(len(seen),max_len)
                    seen = set()
                    break
                j+=1
            max_len = max(len(seen),max_len)
            i+=1
        return max_len

            
