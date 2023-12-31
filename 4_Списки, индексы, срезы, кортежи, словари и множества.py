# Списки 
list = [5,"Stroka",True,5.23,7]
list[1] = 12
#print(list[0])
#print(list[1])
# чтобы добавить элемент в  конец списка list.append("Word") 
list.append("Word")
#что бы обьяденить списки нужно использовать метод list.extend(b)
b = [1,4,3,7,5,]
list.extend(b)
#чтобы удвлить элемент сосписка list.remove("Word")
list.remove(5)
list.remove(5)
list.remove(5.23)
#так же удалить элемент по его инлексу list.pop(0)
list.pop(0)
#для сортировки списка list.sort
b.sort()
#print(b)
# .reverse переворачивает список с конца в начало 
#b.reverse()
#print(b)
# метод очиски .clear 
#b.clear()
#print(b)
list.pop(0)
################################################################
#срезы 
#print(list[::3])
#print(list)
#print(list[2::2])
#print(list[2:5:2])
#что бы с конца -1
#print(list[1:-1:2])
print(list[::])
################################################################
#кордеэджи менять нельзя

cor = (5, "Stroka",True,5.23,7)
#print(cor)
#print(cor[0])
################################################################
#множестао не повторяется 
list1 = (6,2,9,True,6,2,9,True)
print(list1) 

mult = set(list1)
print(mult)


fmult = frozenset(list1)
print(fmult)


################################################################
#словори 
words = {'short':'Dimash', 'long':'Dinmukhammed'}
print(words['short'])
print(words['long'])
