# This program says 'Hello' and asks for my name.

print('Hello! I am Python.')
print('What is your name?')

MyName = input()

if MyName == 'Hector':
    print('It is good to meet you, ' + MyName)
elif MyName == 'David':
    print('Your name isn\'t Hector, but it is ' + MyName)
elif MyName != 'David' and 'Hector':
    print ('Your name isn\'t Hector or David, but it is ' + MyName)

print('The length of your name is:')

print(str(len(MyName)) + ' characters')


print('What is your age?')
MyAge = input()
print('You will be ' + str(int(MyAge) +1) + ' in a year.')
