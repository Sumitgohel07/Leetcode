class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for char in s:
            if char.isalnum():
                s1 += char.lower()
        for i in range(len(s1)//2):
            if s1[i] != s1[len(s1)-1-i]:
                return False
        return True