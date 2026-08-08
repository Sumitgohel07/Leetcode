class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left=0
        right=0
        seen = set()
        while left <= right and right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
            else:
                max_len = max(len(seen),max_len)
                seen.remove(s[left])
                left+=1
            max_len = max(len(seen),max_len)
        return max_len
            
            
