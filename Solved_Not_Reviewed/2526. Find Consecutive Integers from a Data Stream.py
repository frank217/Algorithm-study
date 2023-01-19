# Medium
# https://leetcode.com/contest/biweekly-contest-95/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.cnt = 0

    def consec(self, num: int) -> bool:
        if num == self.v:
            self.cnt += 1 
            return self.cnt >= self.k
            
        self.list = []
        self.cnt = 0
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)