class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while True:
            if len(nums) == 1:
                return nums[0]
            newNums = []
            for i in range(len(nums)-1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums

        # length of nums is >= 1 so this should always exit 
        # can Mathematically solved by caculating Pascal's  where n is length of list or row number and is column number
        # https://en.wikipedia.org/wiki/Pascal%27s_triangle
        #  Great explanation here : https://leetcode.com/problems/find-triangular-sum-of-an-array/solutions/1907380/o-n-time-o-1-space-python-189-ms-c-12-ms-java-4-ms/
        
        #(n r) = n! / r!(n-r)!
        # r = 0  ->    n! / (n)! = 1
        # r = 1  ->     n! / 1 * (n-1)! -> n 
        # r = 2  ->     n! / 2 * (n-2)! -> n*n-1 // 2
    
    def triangularSum(self, nums: List[int]) -> int:
        dic = dict()
        r = len(nums) -1
        mCn = 1
        result = 0
        for i in range(len(nums)):
            result = (result + mCn*nums) % 10
            mCn *= r-i
            mCn // i+1
        return result 
