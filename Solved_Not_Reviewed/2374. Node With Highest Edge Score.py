#https://leetcode.com/problems/node-with-highest-edge-score/


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        dic = defaultdict(int)
        
        for i in range(len(edges)):
            dic[edges[i]] += i
        
        ans = (0,0)
        
        for i,v in dic.items():
            if v > ans[0]:
                ans = (v,i)
            if v== ans[0]:
                ans = (v,min(i,ans[1]))
        return ans[1]