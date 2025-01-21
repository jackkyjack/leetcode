num = [0,1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,6,6,6,6,6,6,6,6,7]

class Solution:
    def removeDuplicates(self,nums):
        i=j=0
        while i<len(nums) and j<len(nums):
            nums[i]=nums[j]
            i+=1
            j+=1
            while j<len(nums) and nums[j-1]==nums[j]:
                j+=1
            
        return i
    
sol = Solution()
print(sol.removeDuplicates(num))