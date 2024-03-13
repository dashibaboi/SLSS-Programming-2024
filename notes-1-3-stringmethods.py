# stribg motehds
# alex feb 21

#ask name and strip it
name = input("What's your name?")


#ask user weather
user_reply = input("What's the weather like today? ")

#strip the string
user_reply.lower()
user_reply.strip()


#if they say rainy say bring umbrella

if user_reply == "rainy":
    print("Bring and unbrella!")
else:
    ("Pardon?")