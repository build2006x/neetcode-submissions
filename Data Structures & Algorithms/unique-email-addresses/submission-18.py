class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
                   
                        unique = set()
                        
                        for emails in emails:
                                local,domain = emails.split('@')
                                ## filter the + 
                                if '+' in local:
                                                local = local[:local.index('+')]
                                ### we need to replace second 
                                local = local.replace('.','')
                                ####    
                                last_email  = local  + '@' + domain
                                unique.add(last_email)
                        return len(unique)

       
                               
