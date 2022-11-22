#https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Group by counter
        # When is it impossible to execute?
        # 1 -> impossible
        # 2,3 -> P
        # Every even is possible
        # every odd larger then 1 is possible since even(including 0) + 3(2+1) is possible
        # 1 is only implossible count

        cnt = Counter(tasks)
        ans = 0
        for v,q in cnt.items():
            if q == 1:
                return -1
            task3 = q // 3
            remnant = q % 3
            if remnant == 1: # remnant is 1 need to be handled by replacing one tasks of 3 by 2 tasks of 2  
                task3 -= 1
                task2 = 2
            else:
                task2 = remnant // 2
            ans += task3 +task2 

        return ans