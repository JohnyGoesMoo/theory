The file `tabulka_pocetnosti.txt` is opened to read the text data.

The text is converted to uppercase using the `upper()` method to ensure consistency in counting characters.
A dictionary `abeceda` is created to store the frequency of each uppercase letter in the text.

from string import ascii_uppercase  # Importing uppercase letters from the string module

# Open the file containing the text data and read its contents text = open("maturita/13/tabulka_pocetnosti.txt", 'r', encoding="UTF-8").read() # Print the original text print(text)
A dictionary comprehension is used to iterate over each uppercase letter (`i`) in the `ascii_up# Convert the text to uppercase text = text.upper()# Count the frequency of each uppercase letter in the text
abeceda = {i: text.count(i) for i in ascii_uppercase}
percase` string and count its frequency in the text using the `count()` method.This list is then joined with newline characters and printed.

The frequency of each letter is printed using a list comprehension to create a list of strings in the format `"letter - frequency"`.
# Print the frequency of each letter print("pocet znakov", "\n".join([" - ".join([i, str(abeceda[i])]) for i in abeceda]))

# Find letters that do not appear in the text bez_znakov = []
for i in abeceda: if abeceda[i] == 0:  # If the frequency of a letter is zero, it is not present in the text   bez_znakov.append(i)  # Add the letter to the list of letters not present in the text
A loop iterates over each letter in the `abeceda` dictionary.
If the frequency of a letter is zero, it means the letter does not appear in the text, so it is added to the list `bez_znakov`.

The letters that do not appear in the text are printed by joining the elements of the `bez_znakov` list with commas.
# Print letters that do not appear in the text print("bez vyskytu v texte su pismena:", ', '.join(bez_znakov))



