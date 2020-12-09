import random
import art
import game_data
import os
import time

def clear():
    os.system('cls') #on Windows System

data_list = game_data.data

game_is_on = True
score = 0
loop = 0
upperbound = 49
lowerbound = 0

while game_is_on:
    loop += 1
    if loop > 0:
        upperbound -= 1

    def random_number():
        """This function will return a random number between 0 and 49"""
        return random.randint(lowerbound, upperbound)

    if score > 0:
        print('\n')
        print(f"*************** Current Score: {score} ***************")

    print(art.logo)

    #In here I'm calling the specific number in the list for the player A
    random_no1 = random_number()
    playerA = (data_list[random_no1])

    #In here I'm calling the specific number in the list for the player B
    random_no2 = random_number()
    playerB = (data_list[random_no2])

    def A():
        """This function will call the player A"""
        global playerA
        print("Compare A: {}, a {}, from {}".format(playerA['name'], playerA['description'], playerA['country']))
        #data_list.remove(playerA)

    A()

    print(art.vs)

    def B():
        """This function will call the player B"""
        global playerB
        print("Against B: {}, a {}, from {}".format(playerB['name'], playerB['description'], playerB['country']))

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

    decision = input(f"Who has more followers?: {playerA['name']} or {playerB['name']} (Type 'A' or 'B'): ")

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

    data_list.remove(playerA)
    data_list.remove(playerB)
    time.sleep(3)
    clear()
