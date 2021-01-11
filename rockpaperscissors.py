import random
global playerChoice
won = 0

while won < 1:
    
    rps = input("Rock(r), Paper(p), or Scissors?(s)")

    def AI():
        global aiChoice
        randomRPS = random.choice([r, p, s])
        if randomRPS == r:
            aiChoice = "rock"
        elif randomRPS == p:
            aiChoice = "paper"
        elif randomRPS == s:
            aiChoice = "scissors"
        print("Computer chose:", randomRPS)

    def who_won():
        global won
        if playerChoice == aiChoice:
            print("Draw!")
        elif 'rock' in playerChoice and 'scissors' in aiChoice:
            print("You Win! :)")
            won += 1
        elif 'paper' in playerChoice and 'rock' in aiChoice:
            print("You Win! :)")
            won += 1
        elif 'scissors' in playerChoice and 'paper' in aiChoice:
            print("You Win! :)")
            won += 1
        else:
            print("A.I Wins! :(")

    if rps == "r" or rps == "R":
        playerChoice = "rock"
        AI()
        who_won()
    elif rps == "p" or rps == "P":
        playerChoice = "paper"
        AI()
        who_won()
    elif rps == "s" or rps == "S":
        playerChoice = "scissors"
        AI()
        who_won()
    else:
        print("Invalid Input! :(")
