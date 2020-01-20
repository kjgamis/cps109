# VARIABLES

a = 42
b = a + 1

# print(f"a equals {a}, b equals {b}")
print(a)

# STRING AND STRING CONCATENATION

# name = input('What is your name? ')
# age = int(input('How old are you? '))

# answer = f"Your name is {name} and you are {age} years old."
# print(answer)

# BASIC ARITHMENTIC

# print(f'11 / 4 = {11/4}')
# print(f'11 / -4 = {11/-4}')
# print(f'11 // 4 = {11//4}')
# print(f'11 // -4 = {11//-4}')
# print(f'11 % 4 = {11%4}')
# print(f'-11 % 4 = {-11%4}')
# print(f'11 % -4 = {11%-4}')

# bob = 2 + 3 * 4 + 5
# print(f"Bob's value is {bob}")

# str(42) # '42'

# print(len(str(123**456)))

a = "9999"
b = str(9999)

print("Results for two strings '9999'")

print(f"a == b: {a==b}\na is b: {a is b}") 
print(f"id(a) equals {id(a)}, id(b) equals {id(b)}")

first = [1,1,1]
second = [first, first, first]

print(second)
first[0] = 99
print(second)

first.append(first)
print(first)

a = [1,2,3,4,5]

print(a[3:4])

d = { 1:"yeah", 2:"nope", "foo":42, 1.3:a }
dk = d.keys()
print(dk) # a dict_keys object
del d[1]
print(dk) # dict_keys with no more 1