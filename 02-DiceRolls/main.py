from random import randint

# make a different comment
# yet another

while True:
    response: str = input("How many dice would you like to roll? ")
    if response.lower() == "exit":
        print("Thanks for playing")
        break
    r = range(int(response))
    dice_rolls = [str(randint(1, 6)) for _ in r]
    print(*dice_rolls, sep=', ')