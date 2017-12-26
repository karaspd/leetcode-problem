"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        last_num=2**31-1
        
        sign=1
        if x<0:
            sign=-1
       	s_rev=int(str(sign*x)[::-1])

       	if s_rev >last_num:
       		return 0
       	else:
            return sign*s_rev

print Solution().reverse(-120)       			