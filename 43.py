A random line (word) is selected and stripped of any leading or trailing whitespace.

A list `hada_slovo` is created to represent the word being guessed. Each character in the list is initially a dot ('.'), indicating unguessed letters.
A boolean flag `vyhra` is initialized to `False` to track whether the player wins the game.
import random

# Select a random word slovo = random.choice(open("file.txt", 'r', encoding="UTF-8").readlines()).strip()# init list to represent the word being guessed, with dots indicating unguessed letters hada_slovo = ['.' for i in range(len(slovo))]

The player has 10 attempts to guess the word. The loop iterates 10 times, each representing an attempt.
During each iteration, the current state of the guessed word and the attempt number are displayed.
The player is prompted to input a letter to guess.
# Initialize a flag to track if the player has won vyhra = False

# Loop for 10 attempts to guess the word
for i in range(10):   # Display the current state of the word and the attempt numberprint(''.join(hada_slovo), "pokus cislo", i + 1)    # Prompt the player to guess a letter
    pismeno = input("hadaj pismenko: ")    # If the guessed letter is in the word    if pismeno in slovo:        id_pismeno = []  # Initialize a list to store the indices of the guessed letter in the word
# Loop through the word to find all indices of the guessed letter        for i in range(len(slovo)):  if slovo[i] == pismeno:                 id_pismeno.append(i)

        # Update the guessed word with the correct letter at the found indices
        for i in id_pismeno:            hada_slovo[i] = pismeno
 If the guessed letter is found in the word, the program finds all indices of that letter in the word and updates `hada_slovo` to reveal the guessed letter at those positions.
After updating the guessed word, the program checks if the entire word has been guessed correctly. If so, the `vyhra` flag is set to `True` and the loop exits early.

After the loop completes (either after 10 attempts or an early exit due to a correct guess), the program prints "VYHRAL" if the player has won, or "PREHRAL" if the player has lost.
   # Check if the player has guessed the entire word    if ''.join(hada_slovo) == slovo:        vyhra = True  # Set the win flag to True
        break  # Exit the loop if the word is fully guessed# Display the final result, either "VYHRAL" for a win or "PREHRAL" for a loss
print("VYHRAL" if vyhra else "PREHRAL")




