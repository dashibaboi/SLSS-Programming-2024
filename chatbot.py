#charboy
#akex
#march8
import random

#greet''
print("Hello there!")



#ask them  something
print("How are you doing? ")
user_feeling = input().strip(",.?! ").lower()

positive_responses = ["Anazing!", "That's great!", "Awesome!", "THE FOG IS COMING"]
bad_repond = ["Sucks to suck", "L", "And?", "Womp womp"]
#respond
if user_feeling == "good" or user_feeling == "great":
    answer = random.choice(positive_responses)
    print(answer)
elif user_feeling == "bad" or user_feeling == "not too good":
    bad_answer = random.choice(bad_repond)
    print(bad_answer)
else:
    print("Speak English")

#BYE BYE
    
print("Nice to talk to you!")