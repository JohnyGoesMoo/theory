The `open()` function is used to open the file containing the list of games (`hada.txt`).
The `readlines()` method reads all lines from the file and returns them as a list of strings (`hry`).
Another file is opened in write mode to store the compressed data (`komprimovany_hada.txt`).


hry = open("file.txt", 'r', encoding="UTF-8").readlines() # Open a new file to write the compressed data komprimovany_subor = open("file.txt", 'w', encoding="UTF-8")
# Print the number of games print("pocet hier:", len(hry))
# Find and print the length of the longest game print("najdlhsia hra:", len(max(hry, key=lambda x: len(x))) - 1)
The compressed data for each game is written to the output file.
The loop iterates through each character in the game, updating the current letter and its count accordingly.
When a different character is encountered, the compressed data for the previous sequence is written to the file.
After processing each game, a newline character is added to separate the compressed data of different games.

# Compress each game and write the compressed data to the new file
for i in hry:  # Iterate through each game     current_letter = 'H'  # Initialize the current letter  counter = 0  # Initialize the counter for the current letter
    for j in i:  # Iterate through each character in the game   if j == current_letter:  # If the current character is the same as the current letter
            The total number of games (`len(hry)`) is printed.
The length of the longest game is determined using `max()` and the `key` argument, which specifies the criterion for finding the maximum length.

Each game is compressed by replacing consecutive occurrences of the same letter with the letter followed by its count.counter += 1  # Increment the counter  else:  # If the current character is different from the current letter # Write the compressed data (current letter and its count) to the file
            napis = current_letter + ' ' + str(counter) + ' ' komprimovany_subor.write(napis) current_letter = j  # Update the current letter
            counter = 1  # Reset the counter for the new letter komprimovany_subor.write('\n')  # Add a newline to separate compressed games in the file



