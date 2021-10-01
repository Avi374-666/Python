"""1"""

x = float(input("Enter number 1"))
y = float(input("Enter number 2"))
z = float(input("Enter number 3"))
if x > y and x > z:
    print("x is the biggest number")
elif y > x and y > z:
    print("y is the biggest number")
else:
    print("z is the biggest number")

'2'


def biggest(x, y, z):
    if (x > y) and (x > z):
        max = x

    elif (y > x) and (y > z):
        max = y
    else:
        max = z

    return max


x = float(input("Enter number 1"))
y = float(input("Enter number 2"))
z = float(input("Enter number 3"))
print((biggest(x, y, z)))

'3'  # a
name = str(input("Enter Name"))
age = int(input("Enter Age "))
year = str((2021 - age) + 100)
print(name + " will be 100 years old in the year " + year)

'3'  # b Age using function
name = input('Please enter your name ...')
age = input('Please enter your age ...')


def turns_100(age):
    return 2021 - int(age) + 100


print(name, 'will be 100 years old in ', turns_100(age))

'4'

first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

both = []

if len(second) < len(first):
    for i in second:
        if i in first and i not in both:
            both.append(i)

if len(second) > len(first):
    for i in first:
        if i in second and i not in both:
            both.append(i)

print(both)

'5'


def even(list):
    for i in list:
        if i % 2 == 0:
            print(i, end=" ")


even([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

'''6'''
U1 = input("First Name")
U2 = input("Second Name")
U1_reply = input("%s, do yo want to choose rock, paper or scissors?" % U1)
U2_reply = input("%s, do you want to choose rock, paper or scissors?" % U2)


def compare(u1, u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1 == 'rock':
        if u2 == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif u1 == 'scissors':
        if u2 == 'paper':
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif u1 == 'paper':
        if u2 == 'rock':
            return "Paper wins!"
        else:
            return "Scissors win!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."


print(compare(U1_reply, U2_reply))
print("Do you both want to play again??")

'7'


# a

def remove(duplicates):
    f_list = []
    for num in duplicates:
        if num not in f_list:
            f_list.append(num)
    return f_list


duplicates = [2, 6, 10, 15, 17, 2, 15, 17]
print(remove(duplicates))

'7'
# b

birthdays = {"Albert Einstein": "14/3/1879",
             "Benjamin Franklin": "17/01/1706",
             "Ada Lovelace": "10/12/1815"}
print('Welcome to the birthday dictionary.We know the birthdays of:\n'
      'Albert Einstein\n'
      'Benjamin Franklin\n'
      'Ada Lovelace\n')
ques = input("Who's birthday do you want to look up?")
if ques in birthdays:
    print(birthdays.get(ques))
else:
    print("sorry,there is no such name")
