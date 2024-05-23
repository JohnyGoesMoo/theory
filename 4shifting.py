
Adds the encrypted character to `new_text`.
If the character is not a lowercase letter, it is added unchanged to `new_text`.
Returns the encrypted text.
from string import ascii_lowercase

def en(text):
    new_text = ""  # empty str to hold en  for i in range(len(text)):  
    # loop through ever ch  if text[i] in ascii_lowercase:  # check if lowecase
            num = ord(text[i]) - 97  # convert to a number (0-25) current_k = ord(kluc[i % len(kluc)]) - 96  # calculate the current key character's value
            num = (num + current_kluc) % 26 + 97  # shift by key val and wrap around if needed #- d   new_text += chr(num)  # back to a ch and add it to the new text
        else:Similar to the encryption function but shifts characters backward by the key value.
Prints some newlines for spacing.
Prompts the user to enter an encryption key.
Opens and reads the input text file.
            new_text += text[i]  # not a lowercase add unchanged to the new text
    return new_text
Converts the character to a number (0-25) using `ord`.
Calculates the key value for the current character.
Shifts the character by the key value, wrapping around if needed, and converts it back to a character using `chr`.

Initializes an empty string `new_text` to store the encrypted text.
Loops through each character in the input `text`.
Checks if the character is a lowercase letter.
k = input("key: ")  #  enter enc key tex = open("file.txt", 'r', encoding="UTF-8")  # read mode text = tex.read()
# Open the encrypted text file in read mode cipher = open("file2", 'r', encoding="UTF-8").read()

# e/d
dec = input("S/D: ")

# If the user chooses "S" (for encrypt), encrypt the text and print it if dec == "S":    print(en(text)) # Otherwise, decrypt the text and print it
else:     print(de(cipher))

ascii_lowercase` is imported from the `string` module, which is a string containing all lowercase ASCII letters.
Opens and reads the encrypted text file.
Prompts the user to choose whether to encrypt (`S`) or decrypt (`D`).
Depending on the user's choice, it either encrypts or decrypts the text and prints the result.

This explanation breaks down the code into easy-to-understand steps.





