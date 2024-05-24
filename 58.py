The first line of the file is read to get the maximum bus capacity (`max_kapacita`).
The remaining lines are read and split into lists containing information about each bus stop (`zastavky`).
Each bus stop's data includes the number of passengers getting on and off the bus.

data = open("file.txt", 'r', encoding="UTF-8")

# Read the maximum bus capacity from the first line of the file max_kapacita = int(data.readline()) Read the bus stops and their occupancy data zastavky = data.readlines()
# Process the bus stops data zastavky = [i.strip().split(' ') for i in zastavky] # Print the number of bus stops print("pocet zastavok:", len(zastavky))
# Print the names of the bus stops print("nazvy zastavok:", ', '.join([' '.join(i[2:]) for i in zastavky]))

# Initialize variables for tracking the most overcrowded bus stop najviac_nad_ramec = 0  # Tracks the highest overcrowding
pocet_v_buse = 0  # Tracks the total number of passengers on the bus preplneny = []  # Stores the names of the most overcrowded bus stops
The script calculates the total number of passengers on the bus (`pocet_v_buse`) by summing the difference between passengers getting on and off at each stop.
It identifies the most overcrowded bus stops by comparing the total number of passengers to the maximum bus capacity.
The names of the most overcrowded bus stops are stored in the list `preplneny`.

# Iterate through each bus stop for i in zastavky:     pocet_v_buse += int(i[0]) - int(i[1])  # Update the total number of passengers on the bus
    # Check if the current bus stop is overcrowded     if pocet_v_buse > max_kapacita and najviac_nad_ramec < pocet_v_buse - max_kapacita:
        najviac_nad_ramec = pocet_v_buse - max_kapacita  # Update the highest overcrowding value
        preplneny.append(' '.join(i[2:]))  # Add the name of the overcrowded bus stop to the list

The highest level of overcrowding (`najviac_nad_ramec`) is updated if a bus stop is found to be more overcrowded than the previous highest level.
The script prints the number of bus stops, their names, the names of the most overcrowded bus stops, and the highest level of overcrowding.
# Print the names of the most overcrowded bus stops print("preplneny bol na zastavke/kach:", ', '.join(preplneny))
# Print the highest overcrowding value print("najviac nad ramec:", najviac_nad_ramec)





