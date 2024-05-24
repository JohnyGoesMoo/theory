The user is prompted to enter a message.
The input text is split into individual words using whitespace as a delimiter.

The number of words in the message is calculated and printed.from string import ascii_lowercase, ascii_uppercase

# text = input("daj oznam: ") # Split the input text into individual words text = text.split(' ') # Print the number of words in the message
Each word in the input text undergoes a case modification (alternating between upper and lower case).
The case modification is achieved by iterating over each word and toggling between upper and lower case based on the `horedole` list.
print("pocet slov:", len(text)) # Define a list to toggle between upper and lower case for each word horedole = ["hore", "dole"]
# Initialize an empty string to store the modified text new_text = ""

# Iterate over each word in the input textfor i in text:    # Toggle between upper and lower case for each word based on the horedole list
    if horedole[0] == "hore": new_text += i.upper()  # Convert the word to uppercase    else: new_text += i.lower()  # Convert the word to lowercase     # Toggle between "hore" and "dole" for the next word
    horedole = [horedole[1], horedole[0]] # Print the modified text print(new_text)
The modified text is decompressed to restore the original case of the words.
The decompression involves identifying transitions between upper and lower case characters to determine word boundaries.
The decompressed text is constructed by iterating over the modified text and appending the lowercase version of each word to the `dekompresia` string.

# Decompression of the modified text dekompresia = ""  # Initialize an empty string for decompressed text zaciatok_slova = 0  # Initialize the start index of each word
# Iterate over the modified text to perform decompression for i in range(1, len(new_text)):     # Check if the current character's case is different from the previous character
    if new_text[i].isupper() != new_text[i-1].isupper():        # Append the decompressed word to the decompression string     dekompresia += new_text[zaciatok_slova:i].lower() + ' '# Update the start index for the next word         zaciatok_slova = i

The modified text and the decompressed text are printed to the console.
# Append the last word to the decompression string dekompresia += new_text[zaciatok_slova::] + new_text[-1]
# Print the decompressed textprint(dekompresia[:-1])



