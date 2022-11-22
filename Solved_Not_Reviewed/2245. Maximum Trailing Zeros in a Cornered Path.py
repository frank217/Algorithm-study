# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/description/


# TLE
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        # Conered path requires at most one turn  meaning straight line is also fine.
        # can solve with prefix value.
        rowLen, colLen = len(grid), len(grid[0])

        # Function to caculate 2 and 5 fits into value
        def get25(val:int):
            newVal = val
            val2, val5 = 0,0
            while newVal%2 == 0 or newVal%5 == 0 :
                if newVal%2 == 0 :
                    newVal //= 2
                    val2 +=1
                if newVal%5 == 0 : 
                    newVal //= 5
                    val5 += 1
            return (val2,val5)


            return (floor(log(c,2)),floor(log(c,5)))
        # Get prefixsum of base 2,5 for row and column
        grid25 =[]
        for r in grid:
            g = []
            for c in r:
                g.append(get25(c))
            grid25.append(g)
        #print("grid25",grid25)

        rowGrid25 = []
        for ri in range(rowLen):
            row = []
            row.append(grid25[ri][0])
            for ci in range(1,colLen):
                val2,val5 = grid25[ri][ci]
                prev2,prev5 = row[-1]
                row.append((val2+prev2,val5+prev5))
            rowGrid25.append(row)
        #print("row25",rowGrid25)

        colGrid25 = []
        colGrid25.append(grid25[0])
        for ri in range(1,rowLen):
            row = []
            for ci in range(colLen):
                val2,val5 = grid25[ri][ci]
                prev2,prev5 = colGrid25[-1][ci]
                row.append((val2+prev2,val5+prev5))
            colGrid25.append(row)
            
        #print("col25",colGrid25)
        #print(grid25,rowGrid25,colGrid25)
        ans = 0
        # Get each row and col max for straight ones
        for r in range(rowLen):
            ans = max(ans,min(rowGrid25[r][colLen-1]))
        for c in range(colLen):
            max(ans, min(colGrid25[rowLen-1][c]))
        
        #tuple caculate
        def calTuple(lists:List[tuple],f):
            ans = reduce(lambda x,y: (f(x[0],y[0]),f(x[1],y[1])),lists)
            #print(ans)
            return ans

      
        # Caculate each cells potential cornered path
        for r in range(rowLen):
            for c in range(colLen):
                # get max val when this cell is corner
                val = grid25[r][c]
               
                l = rowGrid25[r][c]
                right = calTuple([rowGrid25[r][-1],l],operator.sub)
                u = colGrid25[r][c]
                d = calTuple([colGrid25[-1][c],u],operator.sub)

                 #get l and u
                v1 = min(calTuple([calTuple([l,u],operator.add),val],operator.sub))
                #get l and d
                v2 = min(calTuple([l,d],operator.add))
                # get u and right
                v3 = min(calTuple([u,right],operator.add))
                # get d and right
                v4 = min(calTuple([d,right,val],operator.add))
                #print(r,c,val)
                #print(l,right,u,d)
                #print(v1,v2,v3,v4)
                
                ans = max([ans,v1,v2,v3,v4])
                #print(ans)
        #print(ans)
        return ans


