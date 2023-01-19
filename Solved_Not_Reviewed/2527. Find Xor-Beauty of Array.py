#Medium
# https://leetcode.com/contest/biweekly-contest-95/problems/find-xor-beauty-of-array/
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
         return reduce(xor, nums) 