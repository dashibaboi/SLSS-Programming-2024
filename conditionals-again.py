#ask user what favorite fruit is
fave_fruit = input("What's your favorite fruit? ")
age = input("How old are you? ")

if fave_fruit == "apple" or fave_fruit == "orange":
    print("Delicious choice")
elif fave_fruit == "banana" and age == "10":
    print("Haha.")