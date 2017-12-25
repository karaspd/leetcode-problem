"""
5. Longest Palindromic Substring


Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s=s[::-1]
        lon_pal=1
        s_l=s[0]
        m=len(s)
        for i in xrange(m-1):
            for j in xrange(m-1, i, -1):
                if lon_pal <j-i+1:
                    if s[i:j+1]==rev_s[m-1-j:m-i]:
	                    len_p =j-i+1
	                    if len_p >lon_pal:
	                        lon_pal=len_p
	                        s_l=s[i:j+1]

        return s_l     

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s=s[::-1]
        lon_pal=1
        u,v=-1,-1
        
        m=len(s)
        if m==1:
            return s[0]
        else:
            
            for i in xrange(m-1):
                for j in xrange(i+1, m):
                    if lon_pal <j-i+1:
                        if s[i:j+1]==rev_s[m-1-j:m-i]:
                            if j-i+1 >lon_pal:
                                lon_pal=j-i+1
                                u,v=i,j
        if u>-1:                            
            return s[u:v+1]
        else:
            return s[0]


    def longestPalindrome2(self, s):  # faster solution from leetcode solutions
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]

print Solution().longestPalindrome('babadada')
print Solution().longestPalindrome2('babadada')