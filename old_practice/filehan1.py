my_file = open('xmen.txt', 'w+t')
my_file.write('Beast\n')
my_file.write('Pheonix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishops\n',
    'Nightcrwler\n'
])

my_file.close()

my_file = open('xmen.txt', 'r+t')
print(my_file.read())
print("I am reading again")
print(my_file.read())
my_file.close()
