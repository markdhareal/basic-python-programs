# TO DISPLAY INTRO MESSAGE
def introMesssage():
    intro = ["1. Add", "2. Subtract", "3. Multiply", "4. Divide"]

    for item in intro:
        print(item)

# FUNCTIONS FOR SIMPLE MATH FUNDAMENTAL OPERATIONS
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# FLAG AS 1 OR TRUE
flag = 1

# IF THE FLAG'S VALUE IS 1 THE LOOP WILL RUN CONTINUOUSLY
# IF NOT, THE LOOP WILL STOP
while flag:

    # INITIALIZE ANSWER AS 0
    answer = 0
    # CALL THE introMessage() TO DISPLAY INTRO
    introMesssage()
    # GET THE USER'S INPUT
    choice = int(input("Enter: [1, 2, 3, 4]: "))

    # IT WILL CHECK IF THE USER'S INPUT IS 1 TO 4 ONLY
    # IF NOT, THE PROGRAM WILL TELL THE USER TO CHECK THEIR INPUT
    # BECAUSE THE ONLY OPTION IS 1 TO 4 ONLY
    if choice >=1 and choice <=4:

        # IT WILL GET THE VALUE OF X AND Y VARIABLES
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))

        # IT WILL CHECK THE OPERATION CHOSEN BY THE USER
        if choice == 1:
            answer = add(x,y)
        elif choice == 2:
            answer = subtract(x,y)
        elif choice == 3:
            answer = multiply(x,y)
        else:
            answer = divide(x,y)

        # IT WILL PRINT THE ANSWER
        print("Answer: ", answer , "\n")
    else:
        print("Please Check your Input\n")
    
    # ASKING THE USER IF HE/SHE WANTS TO CONTINUE
    again = input("Try again? [y/n]: ")

    # IF THE USER CHOOSE 0, THE FLAG'S VALUE BECOMES 0
    # THE PROGRAM WILL STOP
    if not (again == "y"):
        flag = 0