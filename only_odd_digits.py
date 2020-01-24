# Check that the given positive integer n contains only odd digits (1, 3, 5, 7 and 9) when it is written
# out. Return True if this is the case, and False otherwise. Note that this question is not asking
# whether the number n itself is odd or even. You therefore will have to look at every digit of the
# given number before you can claim that the number contains no odd digits.

# Hint: to extract the lowest digit of a positive integer n, use the expression n % 10. To extract all
# other digits except the lowest one, use the expression n // 10. Or, if you don't want to be this
# fancy, first convert the number into a string and work there.

def only_odd_digits(n):
    str_n = str(n)
    for i in range(len(str_n)):
         if i == '1' or i == '2' or i == '3' or i == '4' or i == '5':
            return True
    return True

print(only_odd_digits(8))
print(only_odd_digits(1357975313579))
print(only_odd_digits(42))
print(only_odd_digits(71358))
print(only_odd_digits(0))