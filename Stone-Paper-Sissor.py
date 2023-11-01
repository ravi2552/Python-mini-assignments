import random
list = ['Stone', 'Paper', 'Sissor']
while True:
    uc = int(input('''
    Game Start...
    1. Yes
    2. No
    '''))
    usercount = 0
    comcount = 0

    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
            1. Stone
            2. Paper
            3. Scissor
            '''))

            if userinput == 1:
                userChoice = 'Stone'
            elif userinput == 2:
                userChoice = 'Paper'
            elif userinput == 3:
                userChoice = 'Scissor'
            com_choice = random.choice(list)
            if userChoice == com_choice:
                print("User value", userChoice)
                print("Computer value", com_choice)
                print("Game Draw")
                usercount = usercount + 1
                comcount = comcount + 1
            elif (userChoice == 'Stone' and com_choice == "Scissor") or (userChoice == "Paper" and com_choice == "Stone") or (userChoice == "Scissor" and com_choice == "Paper"):
                print("Computer value", com_choice)
                print("User value", userChoice)
                print("You Win")
                usercount = usercount +1
            else:
                print("User value", userChoice)
                print("Computer value", com_choice)
                print("Computer Win")
                comcount = comcount + 1

        if usercount == comcount:
            print("Final game draw...")
            print("User Score", usercount)
            print("Computer Score", comcount)

        elif usercount > comcount:
            print("You win the game...")
            print("User Score", usercount)
            print("Computer Score", comcount)

        else:
            print("You lose the game...")
            print("User Score", usercount)
            print("Computer Score", comcount)

    else:
        break


