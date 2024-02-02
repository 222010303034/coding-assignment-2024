def sin(nums):
    c=0
    for i in nums:
        c=c^i
        
    return c
nums = [4, 1, 2, 1, 2]
print(sin(nums))