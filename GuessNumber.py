import random as rd

def GuessNumber():
    Count = 0
    RandomNumber = rd.randint(1,100)
    
    while True :
        MyNumber = int(input("Pick a number: "))
        if MyNumber > RandomNumber :
            print("Too High!")
            Count += 1
            if Count == 3:
                print("Game Over!")
                print(f"The number to guess was {RandomNumber}")
                break
        elif MyNumber < RandomNumber :
            print("Too low!")
            Count += 1
            if Count == 3:
                print("Game Over!")
                print(f"The number to guess was {RandomNumber}")
                break
        else:
            print("Well done!")
            break

GuessNumber()



