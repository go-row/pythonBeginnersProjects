#Coin Counter Game

import random

counter=1
playedTimes=0

while counter:
    playedTimes+=1
    head=0
    tail=0
    n=int(input("Enter the number of tosses "))
    for i in range(0,n):
        turn=random.randint(0,1)
        if turn==1:
            head+=1
        else:
            tail+=1

            
    print("Head Count is ",head)
    print("Tail Count is ",tail)

    
    x=input("Do you want to continue?(Y/N)").lower()
    if x=='n':
        counter=0
        print("You played the game ",playedTimes," number of times.")
        print()
        print("Game Exited!!")

    
input()
