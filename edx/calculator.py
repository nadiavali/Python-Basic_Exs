# int
x = int(input('what is x? '))
y = int(input('what is y? '))

print(x + y)

# Float print round 999 + 1 = 1,000 (us unit) comma matters

x = float(input('what is x? '))
y = float(input('what is y? '))
z = round(x + y)
print(f'{z:,}')

x = float(input('what is x? '))
y = float(input('what is y? '))
z = round(x / y)
print(z)


# Round x/y till two decimals
x = float(input('what is x? '))
y = float(input('what is y? '))
z = round(x / y, 2)
print(z)

# F-string approach to the very same problem

# round x/y till two decimals
x = float(input('what is x? '))
y = float(input('what is y? '))
z = x / y
print(f'{z:.2f}')




