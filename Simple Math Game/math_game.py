print("MATH QUIZ GAME")
print("You have 3 lives")

# THE PLAYER HAS 3 LIVES
lives = 3

correctAnswer = 2

# LOOP
while True:
    
    # IF LIVES BECOMES 0, THE PROGRAM WILL STOP
    if lives == 0:
        print("Life: "+str(lives))
        print("SORRY, YOU LOSE")
        break
    else:
        # ASKING THE USER
        print("Lives: "+str(lives))
        print("1 + 1 = ?")
        
        # GETTING USER INPUT
        answer = int(input("Answer: "))

        # CHECKING IF THE USER'S ANSWER IS CORRECT
        if answer == correctAnswer:
            print("CORRECT!")
            break
        else:
            print("WRONG")
            lives -= 1
    print()

print("\nTHANK YOU FOR PLAYING")