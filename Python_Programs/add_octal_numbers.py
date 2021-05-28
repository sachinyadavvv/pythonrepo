# add octal numbers
a = "123"
b = "456"

sum = oct(int(a, 8) + int(b, 8))

print(sum[2:])
