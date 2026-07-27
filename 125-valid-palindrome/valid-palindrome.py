class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                    left+=1
            while left<right and not s[right].isalnum():
                    right-=1
            if s[left].lower()!=s[right].lower():
                    return False
            left+=1
            right-=1
        return True

       # my firts solution :
       
        # s1 = ""
        # for char in s:
        #     if char.isalnum():
        #         s1 += char.lower()
        # for i in range(len(s1)//2):
        #     if s1[i] != s1[len(s1)-1-i]:
        #         return False
        # return True

