import random

name = input("What is your name? ")

if name == "":
  print("I need your name to know your future.")
elif name.isnumeric():
  print("Names can't be numbers, right?")
else:
  print("\nBonjour, " + name + "! You are going to know your future.")
  question = input("\nWhat is your question?\n")

  fortune = ["Absolutely", "No doubt about it", "Yeah, nah", "You don't wanna know the answer", "You're out of luck"]

  who_fortune = ["Me", "Your friend", "No one", "Your mother", "Your father"]
  where_fortune = ["Mount Roskill", "Mt Eden", "Overseas", "Nowhere"]
  why_fortune = ["Because I said so", "Because you didn't do it right", "Because you didn't pay me"]

  if question.startswith("Who"):
    print(random.choice(who_fortune))
  elif question.startswith("Where"):
    print(random.choice(where_fortune))
  elif question.startswith("Why"):
    print(random.choice(why_fortune))
  else:
    print(random.choice(fortune))
  

