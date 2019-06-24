class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for i in A:
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        ans = []
        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans