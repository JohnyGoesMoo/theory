fr = open("data_file.txt", 'r', encoding="UTF-8")

# dict begins to count every instance
counts = {"z": 0, "c": 0, "m": 0, "o": 0}
   - A dictionary `jedla` is initialized to keep track of the count of each type of food, where the keys are food type codes ("z", "c", "m", "o").
   - Each line in the file is read and processed:
     - Whitespace is stripped from the line, and the line is split into a list using spaces.
     - The second element of the list (assumed to be the food type) is extracted.
     - The count for this food type is incremented in the dictionary.

# loops through every line
for i in fr:     # strips whitespace, splits according to spaces into a list temp = i.strip().split(' ')[1] # increment the count of the respective food type in the dictionary
    counts[temp] += 1


The total number of food orders is calculated by summing the values in the dictionary and printed.# sum values total counts
print(sum(counts.values()))

The counts for each food type ("z", "c", "m", "o") are printed with their respective labels.
An empty list `nedostatok` is initialized to track food types with orders less than 20.
Each food type's count is checked:
If the count is less than 20, the food type is added to the `nedostatok` list.
#pocty print("Z:", counts['z']) print("C:", counts["c"]) print("M:", counts["m"]) print("O:", counts['o'])

# empty list, keeps track of counts w/ insufficiency
insuf = [] for i in counts:     # if count is <20  if counts[i] < 20:  # if yes than insuf insuf.append(i)
If the `nedostatok` list is empty, it means all food types have sufficient orders, and a corresponding message is printed.
If there are any food types with insufficient orders, they are printed as a comma-separated list.

This explanation provides a step-by-step breakdown of the code's functionality for easier understanding.
if len(insuf) == 0: #ci je insuf empty  print("enough")
else:
    print("insuficiency:", ', '.join(insuf))





