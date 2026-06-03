
import random
lower=int(input("Enter the lower number= "))
higher=int(input("Enter the higherst number="))

print(f"You have 7 chnances on your hand. The number must be between {lower}and {higher} Number")

number=random.randint(lower,higher)
chance=7
guess_count=0


while guess_count<chance:
    
    guess =int(input("Enter the guess number="))
    guess_count +=1
    if guess==number:
        print(f"Congrates!!. You have guesses the write number {number}")
        break
    elif guess_count>chance and number!=guess:
        print("Sorry!. The number was{number}, But your guess was{guess}.")
        print("Butter luck next time :-)")
    elif guess >number:
        print("Lower the guess please")
    elif guess<number:
        print("Higher number please")

    if guess==chance and guess != number:
        print("The game is over.\n Butter luck neime :)")
    elif guess==chance and guess == number:

        print("Congrates you have guesses the number.")
