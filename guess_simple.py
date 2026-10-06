secret_number = 7

while True:
    x = int(input("Guess (1-10): "))
    
    if x < secret_number:
        print("Too low! Try again.")
    elif x > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You win! 🎉")
        break
        
