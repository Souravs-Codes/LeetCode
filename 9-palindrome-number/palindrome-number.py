class Solution(object):
    def isPalindrome(self, x):
        if x>=0:
            rev=int(str(abs(x))[::-1])
            if rev == x:
                return True
            else :
                return False
        else :
            return False
        

        

        