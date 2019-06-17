class Solution
    def peakIndexInMountainArray(self, A)
        low, hig = 0, len(A) - 1
        while low  hig
            mid = (low + hig)  2
            if A[mid]  A[mid - 1] and A[mid]  A[mid + 1]
                return mid
            elif A[mid]  A[mid + 1]
                low = mid + 1
            elif A[mid]  A[mid + 1]
                hig = mid
        return low