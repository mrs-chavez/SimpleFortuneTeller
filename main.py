import random

name = input("What is your name? ")

if name == "":
  print("Hmm.. I need to know your name to see your future.")
else:
  if name.isnumeric():
    print("Interesting.. Your name is a number.")
  
  print("\nWelcome, " + name + "! I'm glad you're here.")
  question = input("What is your question?\n")

  if question == "":
    print("\nHmm.. You've gone quiet.")
  elif question[-1] != "?":
    print("\nThat wasn't a question, was it? It didn't end with a question mark.")
  else:
    fortune = [
      "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Signs point to yes.",
    "Don't count on it.", "My sources says no.", "Outlook not so good.", "Very doubtful."]
    print("\n")
    print(random.choice(fortune))
    

