import random
#alex
#roulteet
#apr 9

global money 

black = [2,4,6,8,11,10,13,15,17,20,22,24,26,28,29,31,33,35]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,30,32,34,36]
money = 20

#choose number
def roulette(user_bet):

    roll = random.randrange(0,36)
    user_roll = input("Pick a bet: ").lower().strip()
    if user_roll == roll:
        print("Your number hit!")
        num = user_bet*35
    elif user_roll == "1st 12" and roll <= 12:
        print("Hit! 1st 12!")
        num = user_bet*2
    elif user_roll == "2nd 12" and roll > 12 and roll < 25:
        print("Hit! 2nd 12!")
        num = user_bet*2
    elif user_roll == "1st 12" and roll > 24:
        print("Hit! 1st 12!")
        num = user_bet*2
    elif user_roll == "column 1" and roll%3 == 1:
        print("Hit! Column 1!")
        num = user_bet*2
    elif user_roll == "column 2" and roll%3 == 2:
        print("Hit! Column 2!")
        num = user_bet*2
    elif user_roll == "column 3" and roll%3 == 0:
        print("Hit! Column 3!")
        num = user_bet*2
    elif user_roll == "1 to 18" and roll <= 18:
        print("Hit! 1 to 18!")
        num = user_bet
    elif user_roll == "19 to 36" and roll > 18:
        print("Hit! 19 to 36!")
        num = user_bet
    elif user_roll == "even" and roll%2 == 0:
        print("Hit! The roll is even!")
        num = user_bet
    elif user_roll == "odd" and roll%2 != 0:
        print("Hit! The roll is odd!")
        num = user_bet
    elif user_roll == "black" and roll in black:
        print("Your color hit!")
        num = user_bet
    elif user_roll == "red" and roll in red:
        print("Your color hit!")
        num = user_bet
    else:
        print("Too bad!")
        print(f"The number was {roll}!")
        num = -abs(user_bet)


    return num



def main():
    global money

    while True:
        print(f"You have {money} dollars left!")
        answer = input("Do you want to keep playing? ").lower().strip()
        if answer == "no":
            break
        elif answer == "yes":
            bet = int(input("How much do you want to bet? "))
            if money <= 0:
                print("You're out of money!")
                break
            elif money < bet:
                print("You don't have that much money!")
            else:
                result = roulette(bet)
                money = money + result
        else: 
            print("I didn't understand that")
    
main()
    


