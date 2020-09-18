import sys

file_name = 'recipes.txt'
try:
    my_file = open(file_name, 'x')
    my_file.write('Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print("file name already exists")
#    sys.exit(1)
except:
    print("unable to write to the file")
#    sys.exit(1)
else:
    print("wrote to file")
finally:
    print("Execution completed")


