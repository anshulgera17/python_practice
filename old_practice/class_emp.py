class Emp:
    def __init__(self, id, name, email):
        self.Id=int(input())
        self.name=input()
        self.email=input()

    def print_name(self):
        print("My name is "+self.name)
    
x=1
y="anshul"
z="email"
e = Emp(x, y, z)
print(e.Id)
print(e.name)
print(e.email)
e.print_name()
e.Id=40
print(e.Id)
