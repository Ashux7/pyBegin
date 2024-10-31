print("--------------------------------------Library Management System--------------------------------------")
print('''
      1: Books Available
      2: Book Issue
      3: Book Return
      4: Exit
      ''')
booksAvailList=[]
ch = int(input("Enter your choice: "))
if(ch != 1,2,3):
    print("Invalid input. Program Exited.")
elif(ch == 1):
    print(booksAvailList)