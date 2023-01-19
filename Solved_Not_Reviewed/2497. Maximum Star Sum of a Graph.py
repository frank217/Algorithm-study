# biweekly-contest-93
# https://leetcode.com/contest/biweekly-contest-93/problems/maximum-star-sum-of-a-graph/

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # graph dictionary of node and neighbor with heap
        # Should be able to add as we go. loop through sum of each 
        
        
        dic = defaultdict(list)
        for a,b in edges:
            if vals[b] > 0:
                heapq.heappush(dic[a],vals[b])
            if vals[a] > 0:
                heapq.heappush(dic[b],vals[a])
            if len(dic[a]) > k :
                heapq.heappop(dic[a])
            if len(dic[b]) > k :
                heapq.heappop(dic[b])
        
        ans = max(vals)
        for key,items in dic.items():
            ans = max(ans,sum(items)+vals[key])
        return ans
            
            