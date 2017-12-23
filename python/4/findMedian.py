"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		# Merge Sort

		l=len(nums1)+len(nums2)
		index =(l-1)/2

		i=0
		j=0
		num=[]
		while (i <len(nums1) or j<len(nums2)):
			if i==len(nums1) and j!=len(nums2):
				num.append(nums2[j])
				j+=1

			if j==len(nums2) and i!=len(nums1):
				num.append(nums1[i])
				i+=1
			if i <len(nums1) and j<len(nums2):
				if nums1[i]>nums2[j]:
					num.append(nums2[j])
					j+=1
				else:
					num.append(nums1[i])
					i+=1

			if len(num) == index+1	and l%2==1:
				return num[-1]
			elif len(num)==index+2	and l%2==0:
				return (num[-1]+num[-2])/2.

    def findMedianSortedArrays2(self, nums1, nums2):  # faster solution from leetcode solutions
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums3 = nums1 + nums2
        if not nums3:
            return -1
        
        nums3.sort()
        
        if len(nums3) % 2 == 0:
            idx1 = (len(nums3) / 2) - 1
            idx2 = (len(nums3) / 2)
            return ((nums3[idx1] + nums3[idx2]) / 2.0)
        
        mid_idx = len(nums3) / 2
        return nums3[mid_idx]

    def findMedianSortedArrays3(self, nums1, nums2):  # faster solution from leetcode solutions
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        all_nums = nums1 + nums2
        len_all = len(all_nums)
        all_nums.sort()
        
        if len_all == 0:
            return None
        elif len_all == 1:
            return all_nums[0]
        elif len_all == 2:
            return ((all_nums[0] + all_nums[1]) / 2.0)
        
        if len_all % 2 == 0:
            median = (all_nums[(len(all_nums) / 2)] + all_nums[(len(all_nums) / 2) - 1]) / 2.0
        else:
            median = all_nums[(len(all_nums) / 2)]
            
        return median    

print Solution().findMedianSortedArrays([1,3],[2])

