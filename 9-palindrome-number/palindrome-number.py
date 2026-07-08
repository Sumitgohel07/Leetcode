class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp  = x
        num = 0
        if temp>=0:   
            while(temp!=0):
                ld = temp % 10
                num = (num*10)+ld
                temp = temp//10
            if num == x:
                return True
            else:
                return False
        else:
            return False        