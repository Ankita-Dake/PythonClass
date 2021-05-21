# create class
class sample:
    print("this is class")


print(sample)


# create object
class sample1:
    i = 20
    j = 40


d = sample1()
print(d.i)
print(d.j)


# __init__() function
class demo:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


d1 = demo('om', 203044)
print(d1.name)
print(d1.contact)


# method in class
class demo1:
    def method1(self):
        a = 10
        b = 20
        print('sum = ', a + b)

    def method2(self):
        a = 10
        b = 20
        print('sum = ', a - b)


d2 = demo1()
d2.method1()
d2.method2()


# example
class sampledemo:
    def __init__(self, name, email, contact):
        self.name = name
        self.email = email
        self.contact = contact

    def method1(name):
        print("my name is", name.name)


sampledemo = sampledemo('om', 'om@gmail.com', 8546574698)
sampledemo.method1()

#  modify object
class sampledemo2:
    def __init__(self, name, email, contact):
        self.name = name
        self.email = email
        self.contact = contact

    def method1(name):
        print("my name is", name.name)

sampledemo2 = sampledemo2('om', 'om@gmail.com', 8546574698)
sampledemo2.name = 'nikita'
sampledemo2.method1()

