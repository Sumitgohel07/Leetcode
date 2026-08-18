class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for i in range(len(t)):
            t_dict[t[i]] = t_dict.get(t[i],0) + 1
        left = 0
        window_dict = {}
        need = len(t_dict)
        have = 0
        best_left = left
        best_len = len(s) + 1
        for right in range(len(s)):
            if s[right] in t:
                window_dict[s[right]] = window_dict.get(s[right],0) + 1
                if t_dict[s[right]] == window_dict[s[right]]:
                    have+=1
            while have == need:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                if s[left] in window_dict:
                    if window_dict[s[left]] == t_dict[s[left]]:
                        have -= 1

                    window_dict[s[left]] -= 1

                    if window_dict[s[left]] == 0:
                        del window_dict[s[left]]

                left += 1
        return "" if best_len == len(s) + 1 else s[best_left:best_left + best_len]  