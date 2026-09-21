class Solution(object):
    def reverse(self, x):
        if x==0:
            return 0
        elif x>0:
            result=  int(str(x)[::-1])
        elif x<0:
            result= -int(str(abs(x))[::-1])
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result

     

        