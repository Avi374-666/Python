
print("Hello")
i = 10
print(i)
x = 20
y = 30
if x < y:
    print(x)
    print(y)
    print(x + y)
else:
    print("Yuck!!!")

height = 1.59
print(height)
weight = 50
bmi = (weight/height**2)
print(bmi)
print('Avi\'s "PC"')
print('Avi'+'Avi')
print(2*'Avi')


x =float(input("Please enter an integer: "))
if (x < 0):
    print('Negative Number')
elif (x == 0):
    print('Zero')
elif (x == 1):
    print('One')
else:
    print(x)

no1 = int(input("Enter no1"))
no2 = int(input("Enter no2"))
if ( no1 < no2):
    sum  = no1+no2
    print(sum)
elif (no1 > 5):
    sub = no1-no2
    print(sub)
else:
    print("Hello")

for v in range(1,10,2):
    print ("Avichal")
    print(v)

words =['cat', 'window', 'defenestrate']
for w in words:
    print(w,len(w))
i=0
while(i<10):
    print(i)
    i=i+1


# Check Prime Number Between 1 to 1000
for no in range(2, 1001):
    if no > 1:
        for i in range(2, no):
            if (no % i) == 0:
                break
        else:
            print(no)

# Python program to
# demonstrate break statement
s = 'pythonetraining'
for letter in s:
    print(letter)
    if letter == 'e' or letter == 's':
        break
print("Out of for loop")
print()


# Python program to  demonstrate continue statement
for i in range(1, 10):
    if i == 8:
        continue
    else:
        print(i, end=" ")


# Python program to  demonstrate pass statement
for letter in 'python':
   if letter == 'o':
      pass
      print (' pass block')
   print ( letter)
print ("That's it!")


