"""
 6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
"""

class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows==1 or numRows>len(s):
			return s
		zig=True
		k=0
		list_num=['']*numRows
		j=0
		while j <len(s):
			if zig:
				list_num[k] +=s[j]

				k+=1
				j+=1
				if k==numRows:
					zig=False
					k =numRows-1
			else:
				if numRows>2:
					k -=1
					list_num[k]+=s[j]
					if k==1:
						zig=True
						k=0
					j+=1	
				else:
					zig=True
					k=0

		return ''.join(list_num)

	def convert2(self, s, numRows): # faster solution from leetcode solutions
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows == 1 or numRows >= len(s):
			return s

		L = [''] * numRows
		index, step = 0, 1

		for x in s:
			L[index] += x
			if index == 0:
				step = 1
			elif index == numRows -1:
				step = -1
			index += step

		return ''.join(L)



s="ABC"
print Solution().convert(s,2)        	
print Solution().convert2('PAYPALISHIRING',3)        	




