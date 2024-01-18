class Solution:
    def isPalindrome(self, x: int):
        
        total = 0
        k = x
        while(x > 0):
            b = x%10
            total = total*10+b
            x = x//10
    
        if total == k:
            return 1
        else:
            return 0
print(Solution((121))