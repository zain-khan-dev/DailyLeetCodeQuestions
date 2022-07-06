class Solution:
    # Sorted version
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    #  hashing version

    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for char in s:
            if(char not in freq):
                freq[char] = 0
            freq[char] += 1
        for char in t:
            if(char not in freq):
                freq[char] = 0
            freq[char] -= 1
        for value in freq.values():
            if(value != 0):
                return False
        return True
            
            
        

