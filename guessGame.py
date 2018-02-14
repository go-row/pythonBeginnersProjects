import random
import time

noOfGuesses=0

print("Hello!What is your name?")
myName=input()

print("So "+ myName +"!! I am thinking of a number between 1 to 1000. MAKE A GUESS..")
answer=random.randint(1,1000)
time1=time.time()
while True:
    guess=int(input())
    noOfGuesses+=1
    if guess<answer:
        print('Your guess is too low.')
    elif guess>answer:
        print('Your guess is too high.')
    else:
        print('Correctly guess in '+str(noOfGuesses)+' moves.')
        break

time2=time.time()


totalTime=time2-time1

print('Correctly guess in '+str(totalTime)+' seconds.')
