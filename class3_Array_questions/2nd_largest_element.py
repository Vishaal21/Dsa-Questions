# Ques: https://www.geeksforgeeks.org/problems/second-largest3735/1

class Solution:
    
    def getSecondLargest(self, arr):
    
        # find the 2nd largest element
        first_larg = arr[0]
        sec_larg = 0
        n = len(arr)
        
        for i in range(1, n):
            
            if arr[i] > first_larg:
                sec_larg = first_larg
                first_larg = arr[i]
                continue
            
            
            if arr[i] > sec_larg and arr[i] != first_larg:
                sec_larg = arr[i]
                
                
                
        
        if sec_larg == 0:
            return -1
            
        return sec_larg
                