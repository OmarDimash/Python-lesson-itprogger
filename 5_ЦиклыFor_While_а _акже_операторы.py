lit = [6,8,"Stroka",False,46.7,234,1]

i = 0 
while i  < len(lit):
    #print("Значеник элемента под индексом: ", i  ,"равен", lit[i])
    i+=1

'''
Значеник элемента под индексом:  0 равен 6
Значеник элемента под индексом:  1 равен 8
Значеник элемента под индексом:  2 равен Stroka
Значеник элемента под индексом:  3 равен False
Значеник элемента под индексом:  4 равен 46.7
Значеник элемента под индексом:  5 равен 234
Значеник элемента под индексом:  6 равен 1
'''
lit = [6,8,"Stroka",False,46.7,234,1]

i = 0 
while i  < len(lit):
    #print("Значеник элемента под индексом: ", (i +1) ,"равен", lit[i])
    i+=1
'''
Значеник элемента под индексом:  1 равен 6
Значеник элемента под индексом:  2 равен 8
Значеник элемента под индексом:  3 равен Stroka
Значеник элемента под индексом:  4 равен False
Значеник элемента под индексом:  5 равен 46.7
Значеник элемента под индексом:  6 равен 234
Значеник элемента под индексом:  7 равен 1
'''
'''
for item in lit :

    print("значение эдементов равно ", item)
    '''
''''
for word in "Hello world":
    if word == "l":
       print ("буква l была найдена ")

'''
lit = [6,8,"Stroka",False,46.7,234,1]

i = 0 
while i  < len(lit):
    if i % 2 ==0 :
        i+=1
        continue
    print("Значеник элемента под индексом: ", i  ,"равен", lit[i])
    i+=1


for word in "Hello world":
    if word == "l":
       print ("буква l была найдена ")
       break