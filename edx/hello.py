# Ask user for their name
name = input('What is your name? ')

# Say hello to user
'''
This is a comment
'''
# ',' will automatically makes space and '+' does not!
# end='\n' means go to the next line which is default
# end='' means do not break the line, instead concatenate the line with the next line

print('hello, ', end='')
print(name)

print ('hello, ', name, sep='')

# \(escape char) actually in front of ' makes the 'friend' while we use all the time same quotation mark
print('hello', '\'friend\'')

# Final way(f str): f'...,{variable}'

print(f'hello, {name}')



name = input('What is your name? ')
# Remove whitespace from str
name = name.strip()
 
# Capitalize user's name
name = name.capitalize()
print(f'hello, {name}')


name = input('What is your name? ')
# Remove whitespace from str
name = name.strip()
 
# Capitalize user's name and the all words
name = name.title()
print(f'hello, {name}')

name = input('What is your name? ')
# Remove whitespace from str and capitalize the str in the same time
name = name.strip().title()
 

print(f'hello, {name}')

# this is the best all ,methods together and chain it into variable
name = input('What is your name? ').strip().title()

 

print(f'hello, {name}')