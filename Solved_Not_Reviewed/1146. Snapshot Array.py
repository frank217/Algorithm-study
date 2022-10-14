#https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.snaparray = defaultdict(list)
        self.snap_id_cur = 0
        for i in range(length):
            self.snaparray[i].append([0,0])

    def set(self, index: int, val: int) -> None:
        if self.snaparray[index][-1][0] != self.snap_id_cur:
            self.snaparray[index].append([self.snap_id_cur,val])
            return
        self.snaparray[index][-1][1] = val

    def snap(self) -> int:
        self.snap_id_cur += 1
        return self.snap_id_cur-1

    def get(self, index: int, snap_id: int) -> int:
        #binary search
        indexsnap = self.snaparray[index]
        l,h = 0, len(indexsnap)-1
        while l < h:
            mid = (l+h)//2
            if indexsnap[mid][0] < snap_id : 
                l = mid + 1
            else:
                h = mid
        #print(l,indexsnap)
        if self.snaparray[index][l][0] > snap_id:
            l -= 1
        return self.snaparray[index][l][1]
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)