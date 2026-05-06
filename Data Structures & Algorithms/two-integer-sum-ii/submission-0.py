class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) 
        l = 0 
        r = n -1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l +=1
        
        """
        I  was workign on this one in a very wrong approach at the beginning , I was workign on having both 
        pointers next to each other , but that woulr nbot work , this is why I tried to put 
        th epointers in different pleaces, the begining andnd the end 
        also two sum was using differenc of tarfget adn the actual number, we cna't do this here
        this is why it was better ti user both numebers we have and check if they meet the target 
        for the index of being starting at 1 , I made a mistake by increasing the list range
        and thats what I figured while I was working on it :D 
                        return [l+1, r+1]
            this is the righ approach for indexing at 1 

            I'm happy that I figured the way to place the pointers wigthout me checking the video or the answrr 
            from others 
            Alhamdullah :DDDDDDDDDDDDDDDDDDDDDDDDD
        """
