
A canvas widget (`canvas`) is created to display buildings and streets.
An entry widget (`entry`) allows the user to input the maximum height difference.
A button widget (`button`) triggers the drawing function when clicked.
data = open("file", 'r', encoding="UTF-8").readlines()
print("celkovy pocet vyjadreni je:", len(data)) #exp num # Initialize an empty dictionary to store expressions per hour hodiny = {}

# Iterate over each line in the data for i in data:     # Remove leading and trailing whitespaces and split the line into parts     temp = i.strip().split()
    # Extract the hour from the first part and convert it to an integer    cas = int(temp[0][:2])    # Get the list of expressions for the current hour or an empty list if not present    temp_list = hodiny.get(cas, [])
    # Append the expression to the list for the current hour    temp_list.append(temp[1])    # Update the expressions list for the current hour in the dictionary    hodiny[cas] = temp_list

# Count the number of 'áno' and 'nie' expressions for each hour for i in hodiny:    hodiny[i] = {"áno": hodiny[i].count("áno"), "nie": hodiny[i].count("nie")}
The setup function is called to create the initial game UI elements and get the correct cable and timer display.
Starting the Countdown Timer:The timer function is called to start the countdown timer.inding Events:The tag_bind method is used to bind the click event on the cables (tagged as "cable") to the check_cable function.
Starting the Tkinter Main Loop:
# Find the hour with the maximum number of 'áno' expressions najspokojnejsia_hodina = max(hodiny, key=lambda x: hodiny[x]["áno"]) print("najspokojnejsia hodina je", najspokojnejsia_hodina, "s poctom ano", hodiny[najspokojnejsia_hodina]["áno"])

# Find the hour with the maximum number of 'nie' expressionsnespokojna_hodina = max(hodiny, key=lambda x: hodiny[x]["nie"])
print("nanejspokojnejsia hodina je", nespokojna_hodina, "s poctom nie", hodiny[nespokojna_hodina]["nie"])

The script imports the Tkinter library, allowing for the creation of a graphical user interface.

Functions**: Several functions are defined to handle different tasks:
   - `open_text()`: Reads data from a text file and processes it.
   - `start()`: Initializes the canvas by drawing buildings and streets based on the processed data.
import tkinter as tk
# Calculate the relative satisfaction percentages for each hourrelativna_spokojnost = {i: 0 for i in sorted(hodiny.keys())}
for i in hodiny:relativna_spokojnost[i] = int(hodiny[i]["áno"]/(hodiny[i]["áno"]+hodiny[i]["nie"])*100)
# Print the relative satisfaction percentages print("percenta spokojnosti:\n" + "\n".join([': '.join([str(i), str(relativna_spokojnost[i])+"%"]) for i in relativna_spokojnost]))


