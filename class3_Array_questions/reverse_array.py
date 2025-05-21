# Ques: https://www.geeksforgeeks.org/problems/reverse-an-array/1


class Solution:
    def reverseArray(self, nums):
        # code here
        
        i = 0
        j = len(nums) - 1
        
        while(i < j):
            
            nums[i], nums[j] = nums[j], nums[i]
            
            i+=1
            j-=1
        
        
        