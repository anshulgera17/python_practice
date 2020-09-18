#!/usr/bin/python
exec(open("./test.py").read())
print('my name is '+ name)
subprocess.call('ls',shell=True)
output = subprocess.check_output('ls',shell=True)
print(output)
