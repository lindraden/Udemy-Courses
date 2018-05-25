# Global variable
a = 250

def f1():               # local varible
    b = a + 10
    print(b)

def f2():               # local variable
    a = 50
    print(a)

def f3():               # changing Global Variable by using the keyword global
    global a
    a = 512
    print(a)

f1()
f2()
print(a)
f3()
