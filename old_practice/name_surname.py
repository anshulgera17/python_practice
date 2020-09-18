def name_surname(name):
    print(name)
    arry=name.split(" ")
    naam=arry[0]
    jaat=arry[1]
    print(naam)
    print(jaat)
    return naam, jaat

full_name=input()

name_surname(full_name)
