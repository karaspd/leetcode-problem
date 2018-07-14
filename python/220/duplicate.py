class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        nums_dict=dict()
        for i, n in enumerate(nums):
            if n in nums_dict:
                nums_dict[n].append(i)
            else:
                nums_dict[n]=[i]
        if t==0:        
            for _, v in nums_dict.items():
                diff_v=[]
                if len(v)>1:
                    for i in range(1,len(v)):
                        diff_v.append(abs(v[i]-v[i-1]))

                    if min(diff_v)<k+1:                    
                        return True
        else:
            for k1, v1 in nums_dict.items():
                for k2, v2 in nums_dict.items():
                    # print(k1, k2)
                    if k1==k2 and t>-1:
                        diff_v=[]
                        if len(v1)>1:
                            for i in range(1,len(v1)):
                                diff_v.append(abs(v1[i]-v1[i-1]))

                            if min(diff_v)<k+1:                    
                                return True

                    elif abs(k2-k1) <t+1:
                        diff_v=[]
                        # print('here')                      
                        for i in v1:
                            for j in v2:
                                diff_v.append(abs(i-j))
                        if min(diff_v)<k+1:                    
                            return True
        return False
                       