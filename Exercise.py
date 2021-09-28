'''1'''
x= float(input("Enter number 1"))
y=float(input("Enter number 2"))
z=float(input("Enter number 3"))
if(x>y and x>z):
    print("x is the biggest number")
elif(y>x and y>z):
    print("y is the biggest number")
else:
    print("z is the biggest number")

'''3'''
name= str(input("Enter Name"))
age=int(input("Enter Age "))
year = str((2021 - age)+100)
print(name + " will be 100 years old in the year " + year)

