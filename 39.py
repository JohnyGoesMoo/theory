The code prompts the user to input a sentence.
It splits the input sentence into individual words and initializes an empty string to store the modified sentence.
Each word in the sentence is processed to capitalize the first letter and convert the rest to lowercase.
veta = input("daj oznam: ") # Split into individual words slova = veta.split(' ') #  string to store the modified sentence new_veta = ""

# Iterate over each word in the sentence
for i in slova:     # Capitalize the first letter and convert the rest to lowercase    temp = i[0].upper() + i[1:].lower()    # Append the modified word to the new sentence     new_veta += temp
The code prints the number of words in the original sentence and the modified sentence.
It initializes an empty list to store individual words in the modified sentence and an empty string to store each word.The code prints the number of words in the original sentence and the modified sentence.
It initializes an empty list to store individual words in the modified sentence and an empty string to store each word.The code prints the number of words in the original sentence and the modified sentence.
It initializes an empty list to store individual words in the modified sentence and an empty string to store each word.
# Print the number of words in the sentence and the modified sentence print(f"oznam sa sklada z {len(slova)} slov") print(new_veta)
# Initialize an empty list to store individual words in the modified sentence new_slova = [] # Initialize an empty string to store each word slovo = ""

Each character in the modified sentence is iterated over, and words are extracted based on uppercase characters.
The modified sentence with each word separated by a space is printed.
# Iterate over each character in the modified sentence for i in new_veta:     # Check if the character is uppercase     if i.isupper():
Each character in the modified sentence is iterated over, and words are extracted based on uppercase characters.
The modified sentence with each word separated by a space is printed. # If uppercase, add the current word to the list and reset the word new_slova.append(slovo)  slovo = ""     # Concatenate the character to the current word
    slovo += i

# Add the last word to the list new_slova.append(slovo)# Print the modified sentence with each word separated by a space print(' '.join(new_slova[1:]))
