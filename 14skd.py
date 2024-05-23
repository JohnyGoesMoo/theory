Each line of data is split into separate elements, representing the participant's name, country, and jump scores.
The dictionary `krajiny` is updated to keep track of the number of participants from each country.
# Open the file containing the data about long jump performances data = open("file.txt", 'r', encoding="UTF-8").readlines()
# Dictionary to store the number of participants from each country krajiny = {} # Variables to track the highest score and the winner(s)
winner_score = 0
winner = []

# Iterate through each line of datafor i in data:     # Split each line into separate elements temp = i.strip().split()
    # Update the dictionary with the number of participants from each country krajiny[temp[1]] = krajiny.get(temp[1], 0) + 1
    # Extract the jump scores as integers     skoky = [int(j) for j in temp[2:]]

The best performance for each participant is identified, and the highest score and the corresponding participant(s) are tracked.

The list of countries is printed, followed by the number of participants from each country.
The winner(s) with the highest score are printed. If there is a tie, all winners are listed.
    # Find the best performance in the current line     najlepsi_vykon = max(skoky)

    # Compare the best performance with the current winner's score     if najlepsi_vykon == winner_score:  winner.append(temp[0])  # Add the participant to the list of winners if they match the highest score elif najlepsi_vykon > winner_score:
        winner_score = najlepsi_vykon  # Update the highest score  winner = [temp[0]]  # Replace the list of winners with the current participant

The best performance for each participant is identified, and the highest score and the corresponding participant(s) are tracked.The list of countries is printed, followed by the number of participants from each country.
The winner(s) with the highest score are printed. If there is a tie, all winners are listed.# Print the list of countries print("zoznam krajin:", ', '.join(krajiny.keys()))
# Print the number of participants from each country print("pocty sutaziacich z krajin:", '\n'.join([': '.join([i, str(krajiny[i])]) for i in krajiny]))
# Print the winner(s) print("vitaz/i je/su:", ', '.join(winner))





