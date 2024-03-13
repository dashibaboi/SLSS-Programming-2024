# alexander qiu
# march 5 2024
# Math test

# Define score
total = 0
int(total)

#Function to give user score
def score(num):
    if num == 0:
        print("Too bad!")
    elif num == 3:
        print("Amazing!")
    elif num > 0 and num < 3:
        print("Not bad!")

#first question
answer_1 = input("What is 1+1? ")

#add score
if answer_1 == "2":
    total = total + 1
    print("Correct!")
else:
    print("Incorrect!")    

print()

#second question
answer_2 = input("What is 7*10? ")

#add score
if answer_2 == "70":
    print("Correct!")
    total = total + 1
else: 
    print("Incorrect!")

print()

#third answer
answer_3 = input("What is x if 2x = 10? ")

#add score
if answer_3 == "5":
    print("Correct!")
    total = total + 1
else:
    print("Incorrect!")

print()

#print the users score
score(total)