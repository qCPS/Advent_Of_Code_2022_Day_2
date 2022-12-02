# Open the input file
strategy_file = open("strategy.txt", "r")

# Create a dictionary of the possible ways of scoring
scores = {
    "Win": 6,
    "Draw": 3,
    "Loss": 0,
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

# Create a list of the lines of the input file
strategies = strategy_file.readlines()

# Initialise the score variable to 0
score = 0

# Part 1

# Iterate through the lines of the file
for strategy in strategies:

    # Set the opponent's strategy to the first character in the line
    opponent_choice = strategy[0]

    # Set your choice to the third character
    your_choice = strategy[2]

    # Check what the opponent chose
    if opponent_choice == "A":

        # Calculate the score you get from the choice
        if your_choice == "Y":
            score += (scores["Win"] + scores["Paper"])

        elif your_choice == "X":
            score += (scores["Draw"] + scores["Rock"])

        else:
            score += (scores["Loss"] + scores["Scissors"])

    elif opponent_choice == "B":

        # Calculate the score you get from the choice
        if your_choice == "Z":
            score += (scores["Win"] + scores["Scissors"])

        elif your_choice == "Y":
            score += (scores["Draw"] + scores["Paper"])

        else:
            score += (scores["Loss"] + scores["Rock"])

    else:

        # Calculate the score you get from the choice
        if your_choice == "X":
            score += (scores["Win"] + scores["Rock"])

        elif your_choice == "Z":
            score += (scores["Draw"] + scores["Scissors"])

        else:
            score += (scores["Loss"] + scores["Paper"])

# Display the score
print(score)

# Reset the score
score = 0

# Part 2
for strategy in strategies:

    # Set the opponent's strategy to the first character in the line
    opponent_choice = strategy[0]

    # Set your choice to the third character
    your_choice = strategy[2]

    # Check what the opponent chose
    if opponent_choice == "A":

        # Calculate the score you get from the choice
        if your_choice == "Y":
            score += (scores["Draw"] + scores["Rock"])

        elif your_choice == "X":
            score += (scores["Loss"] + scores["Scissors"])

        else:
            score += (scores["Win"] + scores["Paper"])

    elif opponent_choice == "B":

        # Calculate the score you get from the choice
        if your_choice == "Z":
            score += (scores["Win"] + scores["Scissors"])

        elif your_choice == "Y":
            score += (scores["Draw"] + scores["Paper"])

        else:
            score += (scores["Loss"] + scores["Rock"])

    else:

        # Calculate the score you get from the choice
        if your_choice == "X":
            score += (scores["Loss"] + scores["Paper"])

        elif your_choice == "Z":
            score += (scores["Win"] + scores["Rock"])

        else:
            score += (scores["Draw"] + scores["Scissors"])

print(score)
