'''
file = open('data/text.txt', 'w')
file.write("Hello\nDima")
file.close()
'''
'''
str = input("Enter:")
file = open('data/text.txt', 'w')
file.write(str)
file.close()
'''
'''
str = input("Enter:")
str += "\n"
file = open('data/text.txt', 'a')
file.write(str)
file.close()


file = open('data/text.txt', 'rt')
print(file.read(5))
for line in file:
    print(line)
file.close()
'''
a = int(input('Enter:'))
try:
    b = int(input('Enter:'))
except ValueError:
    b = 0
print("результат:",a+b)