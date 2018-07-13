class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n ==1:
            return True
        if n==0:
            return False
        while True:
            if n%2==0:
                n /=2
                if n ==1:
                    return True
                if n==0:
                    return False
            else:
                return False