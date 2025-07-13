import random
import time
name = input("What is your name? : ")
question = input("What is your question? : \n")
random_number = random.randint(1,9)
# print(random_number)

if question == "":
  print("You must ask a question!")
  exit()
if name == "":
  name = "Nameless Wretch"

print(f"{name} asked, '{question}'\n")

fortunes = [
  "Very doubtful",
  "Outlook not so good",
  "My sources say no",
  "Better not tell you now",
  "Ask again later",
  "Reply hazy, try again",
  "Without a doubt",
  "It is decidedly so",
  "Yes - definitely"
]

replies = [
  "Magic 8 Ball is peering through the fog...",
  "Magic 8 Ball is scrying the Heavens for mandate...",
  "Magic 8 ball is rending the veil..."
]


print(random.choice(replies))
time.sleep(3)




print(f"Magic 8 Ball says: {random.choice(fortunes)}")
print(f"Your (un)lucky number is {random_number}")
print(f"Magic 8 Ball has spoken!")
print(f"Begone, {name}!")