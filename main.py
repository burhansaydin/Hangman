

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)

guess=input("Guess a letter\n").lower()

for i in chosen_word:
  if guess==i:
    print("right")
  else:
    print("wrong")