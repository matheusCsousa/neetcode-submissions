class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l+r) // 2
            print("m", m)
            ll, rr = 0, len(matrix[m])-1
            if matrix[m][ll] <= target and matrix[m][rr] >= target:
                while ll <= rr:
                    mm = (ll+rr) // 2
                    print("mm",mm)
                    if matrix[m][mm] < target:
                        ll = mm+1
                    elif matrix[m][mm] > target:
                        rr = mm-1
                    else:
                        return True
                return False
            elif matrix[m][ll] > target:
                r = m-1
            else:
                l = m+1
        return False

