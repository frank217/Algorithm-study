#https://leetcode.com/problems/sort-array-by-increasing-frequency/
# 451. Sort Characters By Frequency is same.    

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # 
        dic = defaultdict(int)
        
        for num in nums:
            dic[num] += 1
        
        freq = []
        for v,f in dic.items():
            freq.append((f,-v))
        
        freq.sort(reverse=False)
        
        res = []
        for f,v in freq:
            res += [-v] *f
        return res
        
        