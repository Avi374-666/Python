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

'''3'''
name = str(input("Enter Name"))
age = int(input("Enter Age "))
year = str((2021 - age) + 100)
print(name + " will be 100 years old in the year " + year)

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
