with open(r"file.txt", 'r', encoding="UTF-8") as fp: #reads
    lines = len(fp.readlines())
    print('number of lines:', lines) #prints the number of lines♥ with open(r"file.txt", "r") as fp:measurements = fp.readlines() #stores lines in a list

The first with open block reads the file "meteo.txt" and counts the number of lines (measurements).
It then prints the total count of measurements.
The second with open block reads the file again and stores all lines in a list called merania.
Each line is processed to remove extra spaces and split into individual components (assumed to be space-separated).

The highest temperature is determined by sorting the temperature list and taking the last element (which is the highest).
The station corresponding to this highest temperature is found using its index and printed.

The average temperature is calculated and printed.

measurements = [i.strip().split(' ') for i in measurements] #strips whitespaces, splits according to spaces
print(measurements)data = [i[3] for i in measurements] #takes the 4th thing in line,  stores it as a string the temps list

print('measured data:') #prints temps for i in data:  print(I)

The code extracts the fourth element from each measurement (assumed to be the temperature) into a list called teploty.
It prints these temperatures as strings.
Converting temperatures to floats:

The temperatures, originally in string format with commas, are converted to floats by replacing commas with dots.
The processed list of measurements is printed again for verification.
Finding the highest temperature:

# makes strings into floats for i in range(len(data)): data[i] = float(data[i].replace(',', '.'))print(measurements)

# sorts the list and prints the last value, the greatest one
max = sorted(data)[-1]print('1measurement:', max)

# finds the ID where the max is print('measurement id:', measurements[data.index(max)][0]) # average priemer = sum(data) / len(data) print('average', priemer)

The highest temperature is determined by sorting the temperature list and taking the last element (which is the highest).
The station corresponding to this highest temperature is found using its index and printed.

