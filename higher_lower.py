import random
import art
import game_data
import os
import time

def clear():
    os.system('cls') #on Windows System

data_list = game_data.data

#the game_is_on variable is to keep the game running
game_is_on = True
score = 0

#the loop will be a count for the number of times the game loops itself
loop = 0

#the upper and lower bound are for the range in the data_list, because it'll be decreasing each time, becasuse we are removing
#the celebrities that we have already saw.
upperbound = 49
lowerbound = 0

while game_is_on:
    print(art.logo)

    #loop count
    loop += 1
    if loop > 0:
        upperbound -= 2

    def random_number():
        """This function will return a random number between 0 and 49"""
        return random.randint(lowerbound, upperbound)

    #this is for the second time the game starts, it will show us the score we have up until that moment
    if score > 0:
        print(f"*************** Current Score: {score} ***************")
        print('\n')

    #In here I'm calling the specific number in the list for the player A
    random_no1 = random_number()
    playerA = (data_list[random_no1])
    removeplayerA = data_list.remove(playerA)

    #In here I'm calling the specific number in the list for the player B
    random_no2 = random_number()
    playerB = (data_list[random_no2])
    removeplayerB = data_list.remove(playerB)

    #Player A function
    def A():
        """This function will call the player A"""
        global playerA
        print("Compare A: {}, a {}, from {}".format(playerA['name'], playerA['description'], playerA['country']))
        #data_list.remove(playerA)

    #Calling the function of player A
    A()

    print(art.vs)

    #Player B function
    def B():
        """This function will call the player B"""
        global playerB
        print("Against B: {}, a {}, from {}".format(playerB['name'], playerB['description'], playerB['country']))

    #Calling the function of player B
    B()
    print('\n')

    def subtract_followersA():
        """This function will subtract the followers from A to B in case 'A' is bigger than 'B'"""
        global playerA
        global playerB
        return (playerA['follower_count'] - playerB['follower_count'])

    def subtract_followersB():
        """This function will subtract the followers from B to A in case 'B' is bigger than 'A'"""
        global playerA
        global playerB
        return (playerB['follower_count'] - playerA['follower_count'])

    #This is where the game begins and we start asking the user to guess
    decision = input(f"Who has more followers?: {playerA['name']} or {playerB['name']} (Type 'A' or 'B'): ")

    #the if statement for each possible scenario
    if decision == 'A':
        if playerA['follower_count'] > playerB['follower_count']:
            print(f"Correct! {playerA['name']} has {subtract_followersA()} million followers more than {playerB['name']}")
            score += 1
            print(f"Current Score: {score}")
        else:
            print(f"Wrong! {playerB['name']} has more followers than {playerA['name']}")
            game_is_on = False
    elif decision == 'B':
        if playerB['follower_count'] > playerA['follower_count']:
            print(f"Correct! {playerB['name']} has {subtract_followersB()} million followers more than {playerA['name']}")
            score += 1
            print(f"Current Score: {score}")
        else:
            print(f"Wrong! {playerA['name']} has more followers than {playerB['name']}")
            game_is_on = False
    else:
        print("I don't understand what you meant by {decision}")
        continue

    #remove the celebrities we have already seen
    #data_list.remove(playerA)
    #data_list.remove(playerB)
    #wait 3 seconds
    time.sleep(3)
    #clear the console
    clear()
