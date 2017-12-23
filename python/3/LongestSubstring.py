"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring={}
        max_l=0
        s_l=0
        for i, c in enumerate(s):
        	if c in substring:
        		s_l =i-substring[c]
        		for key in substring.keys():
	        		if substring[key]<substring[c]:
	        			substring.pop(key, None)
        		substring[c]=i
        		
        	else:
        		substring[c]=i
        		s_l +=1

        		if s_l > max_l:
        			max_l=s_l


        return max_l

    def lengthOfLongestSubstring2(self, s): # Solution with lowest outcome from leetcode solutions
        """
        :type s: str
        :rtype: int
        """
        indexes = {}
        longest = 0
        last_repeating = -1
        for i, c in enumerate(s):
            if c in indexes and last_repeating < indexes[c]:
                last_repeating = indexes[c]
            if i - last_repeating > longest:
                longest = i - last_repeating
            indexes[c] = i
            
        return longest

print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("pwwkew")
print Solution().lengthOfLongestSubstring("bbtablud")