from string import ascii_uppercase
inp = input("xyz: ")
`ascii_uppercase` is imported from the `string` module, which contains all uppercase ASCII letters.
The user is asked to input a sentence.
Initialize an empty string `cipher` to hold the encrypted sentence.
Loop through each character in the input sentence: If the character is in the `tab` dictionary, append its numeric representation to `cipher`.
If the character is not in the dictionary, append it unchanged.
Print the encrypted sentence, removing the trailing space.

Each uppercase letter is mapped to a numeric representation based on its position in the alphabet. The formula `(i % 3 + 1) * f"{i // 3 + 1}"` creates a repeating pattern of 1, 2, 3 for each group of three letters.
Spaces are mapped to '0 '.
# dict to map uperc to numeric represent
tab = {
    ascii_uppercase[i]: (i % 3 + 1) * f"{i // 3 + 1}" + ' '
    for i in range(len(ascii_uppercase))
}
tab[' '] = '0 '  # map space to 0 # empty str to hold enc sentence cipher = ""  for i in inp:   if i in tab.keys():  # if char in dict
        cipher += tab[i]  # corresponding numeric value to enc senten   else:  cipher += i  # if not, add unchanged
Initialize a dictionary `num_count` to count the occurrences of numbers '0' through '10' in the encrypted sentence.
Count how many times each number appears in the encrypted sentence and store the counts in `num_count`.
# print enc sentence print(cipher[:-1])
# dict count the occurrences of each number (0-10) num_count = {str(i): 0 for i in range(11)}
# count occurences for i in num_count: num_count[i] = cipher.count(i)

# track the maximum count and the numbers with the maximum count max_count = 0 max_count_num = []
Initialize variables to track the maximum count (`max_pocet`) and the list of numbers with the maximum count (`max_policka`).
Loop through the counts in `num_count`:
If the count of a number equals the current maximum count, add the number to `max_count_num`.
# numbers with the highest occurrence
for i in num_count:     if max_count == num_count[i]: max_count_num.append(i)  # If the current number has the same count as the maximum, add it to the list
    elif max_count < num_count[i]: max_count_num = [i]  # If the current number has a higher count, reset the list and update the maximum count max_count = num_count[i]

# Print the numbers with the highest occurrence print("common nums:", ', '.join(max_count_num))
If the count of a number exceeds the current maximum count, update `max_pocet` and reset `max_count_num` to only include the current number.
Print the numbers with the highest occurrence, joining them with commas.








