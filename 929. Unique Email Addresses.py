class Solution:
    # �ѵ����Ѫk�A�Ĳv����
    def numUniqueEmails(self, emails):
        ans = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            ans.add(local.replace('.', '') + '@' + domain)
        return len(ans)
        
    # �ڪ��Ѫk�A�Ĳv�ܮt
    #         ans = set()
    #         for mail in emails:
    #             addr = ''
    #             stop = False
    #             at_sign = False
    #             for c in mail:
    #                 if c == '+':
    #                     stop = True
    #                 elif c == '@':
    #                     stop = False
    #                     at_sign = True
    #                     addr += '@'
    #                 elif not stop:
    #                     if c == '.' and not at_sign:
    #                         continue
    #                     else:
    #                         addr += c
    #             ans.add(addr)

    #         return len(ans)