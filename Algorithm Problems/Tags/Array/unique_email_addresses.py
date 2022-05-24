from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()

        for email in emails:
            domain_name = email.split('@')[-1]
            local_name = email.split('@')[0]
            split_email = local_name.split('+')[0].replace('.', '')
            clean_email = split_email + '@' + domain_name
            email_set.add(clean_email)

        return len(email_set)

    # def numUniqueEmails(self, emails: List[str]) -> int:
    #     seen = set()
    #     for email in emails:
    #         name, domain = email.split('@')
    #         local = name.split('+')[0].replace('.', '')
    #         seen.add(local + '@' + domain)
    #     return len(seen)
