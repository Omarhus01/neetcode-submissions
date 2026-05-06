class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        start = 0 
        end = n - 1 
        
        while start <= end:
            #check if the current thing we are at is not alpha numeric, if  not, we continu, if yes 
            # we increment left adn we check it for ther end as well , and decrement 

            if  not s[start].isalnum():
                start+=1
                continue 
            elif not s[end].isalnum():
                end -= 1
                continue 
            else:
                if s[start] != s[end]:
                    return False
            start +=1 
            end  -= 1
        return True



        