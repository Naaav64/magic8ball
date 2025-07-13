import random
import time
name = "Ken"
question = input("What is your question? : ")
answer = ""
random_number = random.randint(1,9)
# print(random_number)

match random_number:
  case 1: 
    answer = "Very doubtful"
  case 2:
    answer = "Outlook not so good"
  case 3:
    answer = "My sources say no"
  case 4:
    answer = "Better not tell you now"
  case 5:
    answer = "Ask again later"
  case 6:
    answer = "Reply hazy, try again"
  case 7:
    answer = "Without a doubt"
  case 8:
    answer = "It is decidedly so"
  case 9:
    answer = "Yes - definitely"
  case default:
    raise Exception("Please refill Magic 8 Ball")


print(f"You've asked: {question}\n")

random_reply = random.randint(1,3)

if random_reply < 2: 
    print("Magic 8 Ball is peering through the fog...")
    time.sleep(3)
elif random_reply > 2:
    print("Magic 8 Ball is scrying the Heavens for mandate...")
    time.sleep(3)
elif random_reply == 2:
    print("Magic 8 ball is rending the veil...")
    time.sleep(3)

print(f"Magic 8 Ball says: {answer}")
print(f"Magic 8 Ball has spoken!")