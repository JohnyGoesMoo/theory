with open(r"file.txt", 'r', encoding="UTF-8") as fp: #reads
    lines = len(fp.readlines())
    print('number of lines:', lines) #prints the number of lines♥ with open(r"file.txt", "r") as fp:measurements = fp.readlines() #stores lines in a list

measurements = [i.strip().split(' ') for i in measurements] #strips whitespaces, splits according to spaces
print(measurements)data = [i[3] for i in measurements] #takes the 4th thing in line,  stores it as a string the temps list

print('measured data:') #prints temps for i in data:  print(i)

# makes strings into floats for i in range(len(data)): data[i] = float(data[i].replace(',', '.'))print(measurements)

# sorts the list and prints the last value, the greatest one
max = sorted(data)[-1]print('1measurement:', max)

# finds the ID where the max is print('measurement id:', measurements[data.index(max)][0]) # average priemer = sum(data) / len(data) print('average', priemer)


