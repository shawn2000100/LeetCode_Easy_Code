from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        m, n = len(s), len(p)
        if m < n:
            return []
        
        ans = []
        pCounter = Counter(p) # �ؼФ��r��
        sCounter = Counter(s[:n-1]) # �ưʵ��f�r��A�en-1�Ӧr���[�i���f�A����A�C�C���k�[�@
        
        for i in range(n-1, m):
            sCounter[s[i]] += 1 # �V�k�W�[�@�Ӧr��
            if sCounter == pCounter:
                ans.append(i - n + 1) # i�V��n�Ӧr�����צA+1�^�ӴN�O���ת��_�lindex�F
            
            sCounter[s[i - n + 1]] -= 1 # �̥���R���@�Ӧr���A�έp��-1
            if sCounter[s[i - n + 1]] == 0: #�W�v��0�A�����R���C�_�h{��a��: 0, ��b��: 1}) != {��b��: 1}
                 del sCounter[s[i - n + 1]]
        
        return ans