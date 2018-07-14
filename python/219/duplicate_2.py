class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums))==len(nums):
            return False
        nums_dict=dict()
        for i, n in enumerate(nums):
            if n in nums_dict:
                nums_dict[n].append(i)
            else:
                nums_dict[n]=[i]
        
        for _, v in nums_dict.items():
            diff_v=[]
            if len(v)>1:
                for i in range(1,len(v)):
                    diff_v.append(abs(v[i]-v[i-1]))
                    
                if min(diff_v)<k+1:                    
                    return True
                
        return False
        