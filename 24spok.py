
The text is converted to uppercase using the `upper()` method to ensure consistency in counting characters.
A dictionary `abeceda` is created to store the frequency of each uppercase letter in the text.

data = open("file_1.txt", 'r', encoding="UTF-8").readlines()# Open the file "" for reading and read all lines into a list

# Extract the times from each line and store them in a listcasy = [i.split()[0] for i in data]

A dictionary comprehension is used to iterate over each uppercase letter (`i`) in the `ascii_up# Convert the text to uppercase text = text.upper()# Count the frequency of each uppercase letter in the text
abeceda = {i: text.count(i) for i in ascii_uppercase}
percase` string and count its frequency in the text using the `count()` method.This list is then joined with newline characters and printed.
# Initialize variables to track previous time, days, reactions, and hours prev_time = 0 dni = [] reakcie = 0 hodiny = {}

# Iterate over the times extracted from the data for i in range(len(casy)):     # Convert the time string to minutes time = int(casy[i][:2])*60 + int(casy[i][3:5])
    # Check if the current time is less than the previous time (indicating a new day)     if prev_time > time: # Append the number of reactions from the previous day to the list of days
        dni.append(reakcie)         # Reset the reaction count for the new day  reakcie = 0
    # Increment the reaction count for the current day  reakcie += 1  # Update the previous time  prev_time = time # Update the dictionary of hours with the count of reactions for each hour hodiny[int(casy[i][:2])] = hodiny.get(int(casy[i][:2]), 0) + 1
The text is converted to uppercase using the `upper()` method to ensure consistency in counting characters.A dictionary `abeceda` is created to store the frequency of each uppercase letter in the text.The text is converted to uppercase using the `upper()` method to ensure consistency in counting characters.
A dictionary `abeceda` is created to store the frequency of each uppercase letter in the text.

# Print the count of reactions for each hour for i in sorted(hodiny):print(f"Hodina:{i} Reakcii zakaznikov:{hodiny[i]}")# Print the total number of days and the count of reactions for each day print("pocet dni:", len(dni)) for i in range(1, len(dni)+1):     print(f"{i}. den - pocet reakcii: {dni[i-1]}")

