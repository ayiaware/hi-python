import random

def roll(num_sides):
   
    print("Rolling a pair of %d-sided dice."%num_sides)
    
    rollOne = random.randint(1, num_sides)
    rollTwo = random.randint(1, num_sides)

    totalRoll = rollOne + rollTwo
    
    print("First die rolled %d."%rollOne,"\nSecond die rolled %d."%rollTwo)

    if rollOne == rollTwo:
        print("You rolled a double !")

    return totalRoll

numOfSides = (int(input("Enter number of sides")))

print("The total is %d."%roll(numOfSides))

