class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ele_set = set()
        for num in nums:
            if(num in ele_set):
                return True
            ele_set.add(num)
            
        return False
