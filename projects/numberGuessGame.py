import random
print("YOU HAVE TO ENTER A RANGE.")
def userinp():
    global n
    global p
    n=input("Enter first number of range.")
    p=input("Enter last number of range.")
userinp()
if n.isnumeric() == True and p.isnumeric() == True:
    a,b = int(n),int(p)
    num = random.randint(a,b)
    print("The game begins!")
    ch = int(input("Enter your guess: "))
    nguess = 0
    while ch != num:
        print("Wrong guess bud, try again.")
        ch = int(input("Enter your guess: "))
        nguess += 1
    if ch == num:
        print("Congrats you guessed it right.")
        print("Number of guesses taken:",nguess)
    else:
        pass
else:
    userinp()