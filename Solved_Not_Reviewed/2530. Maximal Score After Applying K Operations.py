# Medium
# https://leetcode.com/contest/weekly-contest-327/problems/maximal-score-after-applying-k-operations/
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        for i in range(k):
            val = -heapq.heappop(nums)
            score += val
            val = math.ceil(val/3)
            heapq.heappush(nums,-val)
        
        return score