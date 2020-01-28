# Check that the given positive integer n contains only odd digits (1, 3, 5, 7 and 9) when it is written
# out. Return True if this is the case, and False otherwise. Note that this question is not asking
# whether the number n itself is odd or even. You therefore will have to look at every digit of the
# given number before you can claim that the number contains no odd digits.

# Hint: to extract the lowest digit of a positive integer n, use the expression n % 10. To extract all
# other digits except the lowest one, use the expression n // 10. Or, if you don't want to be this
# fancy, first convert the number into a string and work there.

# def only_odd_digits(n):
#     str_n = str(n)
#     for i in range(0, len(str_n)):
#          if str_n[i] == '0' or str_n[i] == '2' or str_n[i] == '4' or str_n[i] == '6' or str_n[i] == '8':
#             return False
#     return True

def only_odd_digits(n):
    if n == 0: 
        return False
    while n > 0: 
        num = n % 10
        if num == 0 or num == 2 or num == 4 or num == 6 or num == 8:
            return False
        n = n // 10
    return True

print(only_odd_digits(8))              # False
print(only_odd_digits(1357975313579))  # True
print(only_odd_digits(42))             # False
print(only_odd_digits(71358))          # False
print(only_odd_digits(0))              # False