### ========== CYCLOPS NUMBERS ========== ###

# def is_cyclops(n):
# A nonnegative integer is said to be a cyclops number if it consists of an odd number of digits so
# that the middle (or more poetically, the "eye") digit is a zero, and all other digits of that number are
# nonzero. This function should determine whether its parameter integer n is a cyclops number, and
# accordingly return either True or False.


def is_cyclops(n):
    str_n = str(n)
    length = len(str_n)

    if length % 2 != 0:
        middle = int((len(str_n) - 1) / 2)
        list_n = list(str_n)
        list_n[middle] = ''
        new_n = "".join(list_n)
        if str_n[middle] == '0' and '0' not in new_n:
            return True
    return False

print(is_cyclops(101))
print(is_cyclops(101))
print(is_cyclops(98053))
print(is_cyclops(777888999))
print(is_cyclops(1056))
print(is_cyclops(675409820))
