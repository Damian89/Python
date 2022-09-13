
fileName = input('Enter the name of the file: ')

with open(fileName) as f:
    text = f.readlines()
    print('You entered the file named %s ' % (fileName))
    print(text)
