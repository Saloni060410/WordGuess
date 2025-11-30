import random

wordBank=[ "planet", "orange", "guitar", "castle", "bridge", "forest", "frozen","golden", "shadow", "mirror", "socket", "switch", "window", "rocket","python", "banana", "market", "random", "wizard", "legend", "mystic","galaxy", "island", "beauty", "silver", "danger", "hunter", "puzzle","thunder", "crystal", "diamond", "journey", "kingdom", "network","firefly", "butter", "cookie", "candle", "tunnel", "marker", "circle","impact", "instead", "perfect", "victory", "freedom", "passion","horizon", "awesome", "gravity", "valley", "engine", "device", "system","flower"]

word=random.choice(wordBank)

attempts=10

current_w=["_"]*len(word)

while attempts>0:

    print("Current Word : ","".join(current_w))
    guess=input("Guess a letter : ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                current_w[i]=guess
        print("Correct Guess")

    else:
        print("Wrong Guess")
        attempts=attempts-1
        print("Remaining attempts : ",attempts)
    
    if "_" not in current_w:
        print("\nCongratulations you guessed the word.")
        print("Word is : ","".join(current_w))
        break
    
    if "_" in current_w and attempts==0:
        print("You ran out of attempts...Better luck next time.")
        break

    print("\n")
    
