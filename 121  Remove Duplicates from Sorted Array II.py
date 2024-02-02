def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    prev = nums[0]
    count = 1
    index = 1
    
    for i in range(1, len(nums)):
        if nums[i] == prev:
            count += 1
            if count <= 2:
                nums[index] = nums[i]
                index += 1
        else:
            prev = nums[i]
            count = 1
            nums[index] = nums[i]
            index += 1
    
    return index

A = [1, 1, 1, 2]
new_length = removeDuplicates(A)
print("New length:", new_length)  
print("Modified array:", A[:new_length])  
