class Solution:
    def reverse(self, x: int) -> int:
        result = 0 
        flag = 0
        if x<0:
            flag = 1
            x = -x  
        while(x>0):
            ld = x % 10
            result = ld + result*10 
            x = x // 10
        if (-(2**31) <= result <= (2**31)-1):
            if flag == 1:
                return -result
            else:
                return result
        else:
            return 0



