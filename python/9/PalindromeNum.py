"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x%10==0 and x!=0) or x<0:
        	return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x/10

        return x == rev or x == rev/10    

    def isPalindrome2(self, x):  #  with converting to string
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        reverse = x[::-1]
        if x == reverse:
            return True
        return False        

print Solution().isPalindrome2(10)
