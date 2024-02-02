def count_set_bits(A):
    count = 0
    while A:
        count += A & 1
        A >>= 1
    return count

input_number = 11
print(count_set_bits(input_number))  
