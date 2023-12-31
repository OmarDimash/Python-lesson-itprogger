# обычные функчии
def func():
    print("Hello world")

func()
################################################################
def func(wrods):
    print("Переменная:", wrods)


func("Hello world")

def summ(a=2,b=4,x=0):
    res = a+b+x
    return res
result= summ(5,2,7)
print(result)


################################################################
def printAll(*params):
    for i in params:
        print(i * 2)
    print("\n")

printAll(6,"word",7,9.23)
printAll(8,1)
################################################################
def printDictinary(**args):
    print(args)

printDictinary(name= "Dimash",surname = "Omar",age = 21, stat = "Student",city = "Istanbul")

################################################################
def printDictinary(**args):
    for key ,valus in args.items():
        print("Ключ:",key,",","Значение:",valus)
    print(args)

printDictinary(name= "Dimash",surname = "Omar",age = 21, stat = "Student",city = "Istanbul")
#анонимные функции 
mult = lambda x, a: x * a 

print(mult(6,3))
print(mult(5,2))
################################################################
mult = lambda *args: print(args)

mult(6, " Stroka", True )
mult(5,2)