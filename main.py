strategy_file = open("strategy.txt", "r")

scores = {
    "Win": 6,
    "Draw": 3,
    "Loss": 0,
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

strategies = strategy_file.readlines()

score = 0

# Part 1
for strategy in strategies:
    opponent_choice = strategy[0]
    your_choice = strategy[2]

    if opponent_choice == "A":
        if your_choice == "Y":
            score += (scores["Win"] + scores["Paper"])

        elif your_choice == "X":
            score += (scores["Draw"] + scores["Rock"])

        else:
            score += (scores["Loss"] + scores["Scissors"])

    elif opponent_choice == "B":
        if your_choice == "Z":
            score += (scores["Win"] + scores["Scissors"])

        elif your_choice == "Y":
            score += (scores["Draw"] + scores["Paper"])

        else:
            score += (scores["Loss"] + scores["Rock"])

    else:
        if your_choice == "X":
            score += (scores["Win"] + scores["Rock"])

        elif your_choice == "Z":
            score += (scores["Draw"] + scores["Scissors"])

        else:
            score += (scores["Loss"] + scores["Paper"])

print(score)

score = 0

# Part 2
for strategy in strategies:
    opponent_choice = strategy[0]
    your_choice = strategy[2]

    if opponent_choice == "A":
        if your_choice == "Y":
            score += (scores["Draw"] + scores["Rock"])

        elif your_choice == "X":
            score += (scores["Loss"] + scores["Scissors"])

        else:
            score += (scores["Win"] + scores["Paper"])

    elif opponent_choice == "B":
        if your_choice == "Z":
            score += (scores["Win"] + scores["Scissors"])

        elif your_choice == "Y":
            score += (scores["Draw"] + scores["Paper"])

        else:
            score += (scores["Loss"] + scores["Rock"])

    else:
        if your_choice == "X":
            score += (scores["Loss"] + scores["Paper"])

        elif your_choice == "Z":
            score += (scores["Win"] + scores["Rock"])

        else:
            score += (scores["Draw"] + scores["Scissors"])

print(score)
