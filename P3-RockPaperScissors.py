import random

choiceList = ["Rock", "Scissors", "Paper"]
userScore = 0
computerScore = 0

humanToNumber = {"R": 1,
                 "S": 2,
                 "P": 3}
play = 1
while play > 0:
    userInput = input("------------------\nWrite your Choice\n1.Rock\n2.Paper\n3.Scissors\nEnter Here:-")
    userInput = userInput.capitalize()

    if userInput in choiceList:
        computerInput = str(random.choice(choiceList))
        print(f"Computer Chooses:-{computerInput}")
        computerInput = humanToNumber[computerInput[0]]
        userInput = humanToNumber[userInput[0]]

        if userInput == computerInput:
            print("------------------\nTie\n------------------")
        elif userInput == (computerInput % 3) + 1:
            print("------------------\nComputer Wins\n------------------")
            computerScore += 1
        else:
            print("------------------\nPlayer Wins\n------------------")
            userScore += 1
        print(f"Computer:-{computerScore}\nPlayer:-{userScore}")

    else:
        print("Your input is invalid....\nPlease enter again!")

    play = int(input("------------------\nTo Exit press 0\nTo Continue press 1\nEnter here:-"))

# Here we take input from the user and convert to a number using humanToNumber Dictionary
# For random selection of computer, we have created a choiceList List and we select from it using random.choice(choiceList) method
# For Win/Loss logic we are using arithmetic operator(%) modulo.
# To understand this logic visit https://therenegadecoder.com/code/rock-paper-scissors-using-modular-arithmetic/#the-modular-arithmetic-minimalist
