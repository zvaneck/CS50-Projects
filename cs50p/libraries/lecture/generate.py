import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(0, 10)
print(number)

cards = ["a", "b", "c"]
random.shuffle(cards)
for card in cards:
    print(card)