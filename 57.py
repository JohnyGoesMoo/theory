The `shuffle` function from the `random` module is imported to shuffle characters within words.
 The file `poprehadzovany_text1_vstup.txt` is opened to read the original text.
Another file is opened in write mode to store the shuffled text (`poprehadzovany_text1.txt`).
from random import shuffle

# Open the file containing the original text text = open("file.txt", 'r', encoding="UTF-8").readlines()  # Open a new file to write the shuffled text  poprehadzovany_subor = open("file2.txt", 'w', encoding="UTF-8")
# Print the original text print(''.join(text)) # Process the original text text = [i.strip().split() for i in text]  # Split the text into words
The original text is split into words, and each word is stored in a nested list.
Each word in the original text is processed individually.
For each word, the characters (excluding the first and last characters) are shuffled using the `shuffle` function.
new_text = ""  # Initialize the variable to store the shuffled text

# Iterate through each word in the text
for i in text:The shuffled characters are then reconstructed into a shuffled word while preserving the first and last characters.
The shuffled word is appended to the `new_text` string, followed by a space.
After processing each line of text, a newline character is added to separate lines.

    for word in i:  # Shuffle the characters of the word (excluding the first and last characters) inner_word = [j for j in word[1:-1]]
        shuffle(inner_word) # Reconstruct the shuffled word while preserving the first and last characters  shuffled_word = word[0] + ''.join(inner_word) + word[-1] if len(word) > 1 else word new_text += shuffled_word + ' '  # Append the shuffled word to the new text
    new_text += '\n'  # Add a newline character after processing each line

# Print the shuffled text print('\n'+new_text) # Write the shuffled text to the output file poprehadzovany_subor.write(new_text)
The shuffled text stored in the `new_text` string is written to the output file using the `write` method.



