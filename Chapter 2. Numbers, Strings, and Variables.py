# 2.1
# booleans
print(True, False)

# integers
print(42, 100000000000)

# floats
print(3.14159, 1/6, 1.0e8)

# strings
print('foo', 'bar')

# 2.2
# variables

a = 7
print(a)

b = a
print(b)

# type to tell you the type of variable

print(type(a))
print(type(b))
print(type(58))
print(type(99.0))
print(type('abc'))

# 2.3
# Math operators

print(5 + 8, 90 - 10, 4 * 7, 7 / 2, 7 // 2, 7 % 3, 3 ** 4)

a = 95
a -= 3
print(a)

a += 8
print(a)

a /= 3
print(a)

a //= 4

print(9 // 5, 9 % 5, divmod(9, 5))

# 2.4
# Bases
# Decimal
print(10)

# Binary
print(0b10)

# Octal
print(0o10)

# Hexadecimal
print(0x10)

# 2.5
# Type Conversions

# Bool to int
print(int(True), int(False))

# Float to int
print(int(98.6), int(1.0e4))

# String to int
print(int('99'), int('-23'), int('+12'))

# Automatic conversion by Python
print(4 + 7.0, True + 2, False + 5.0)

# Bool to Float
print(float(True), float(False))

# Int and string to Float
print(float(98), float('99'), float('98.6'), float('-1.5'), float('1.0e4'))

# test if this works
