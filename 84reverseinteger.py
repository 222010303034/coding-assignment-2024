def reverse(n):
    reversed = 0
    
    while n > 0:
        last_digit = n % 10
        reversed = reversed * 10 + last_digit
        n = n // 10

    return reversed

number = int(input("Enter a number: "))
print("Reversed number: ", reverse(number))