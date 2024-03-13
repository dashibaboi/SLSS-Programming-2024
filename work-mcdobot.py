#mcdo bot
#alex feb 21

fries = input("Would you like fries with your meal? ").strip().lower()


if fries == "yes":
    print("Here's your meal with fries!")
elif fries == "no":
    print("Here's your meal without fries!")
else:
    print(f"Sorry, I don't understand", fries)