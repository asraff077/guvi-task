import random 
num = random.randint(1,100) 
guessNumber = int(input("Guess the number(1-100):")) 
while (num!="stop"): 
    if(guessNumber<num): 
        print("your guess is low") 
        guessNumber = int(input("enter the number(1-100):")) 
    elif(guessNumber>num): 
        print("your guess is high") 
        guessNumber=int(input("enter the number(1-100):")) 
    else:
        print("You won")
        break
