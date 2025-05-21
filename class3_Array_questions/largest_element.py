# Ques: https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1

class Solution:
    def largest(self, arr):
        
        largest_num = arr[0]
        
        for num in arr:
            
            if num > largest_num:
                largest_num = num
            
        
        return largest_num