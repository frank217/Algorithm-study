#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use
        
        a = sorted([(f,v) for v,f in Counter(nums).items()],reverse=True)
        
        return [ v for f,v in a[:k]]
