import random

n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Enter the number:"))
    if(a>n):
        print("Lower Number please")
        guesses += 1
    elif(a<n):
        print("Higher Number please")
        guesses += 1
print(f"You have correctly guessed the number {n} in {guesses} attempts")