import random
import time

count = 0

print("DICE ROLLING SIMULATOR.".center(50,'*'))
print()

time1 = time.time()


while True:
    numberOnRoll = random.randint(1,6)
    count += 1
    start = input("Hit enter to roll the dice. ")
    print()
    print("The number on the dice after roll ",count," is ",numberOnRoll)
    print()
    playAgain = input("Do you wish to continue?(Y/N)")
    print()
    if playAgain.lower().startswith('y'):
        continue
    else:
        break



time2 = time.time()



totalTime = time2-time1


print("You rolled the dice ",count," times.")
print()


print("You used the DICE ROLLING SIMULATOR for ",totalTime," seconds.")
