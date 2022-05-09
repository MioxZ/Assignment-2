# libraries
import sys

# Variables Initialization 
fileName = sys.argv[1];
existingString = sys.argv[2];
newString = sys.argv[3];
data = None;

# Main
print("Running script - {0}...".format(sys.argv[0]));
print("To read from - {0}".format(sys.argv[1]));
print("To replace - {0}".format(sys.argv[2]));
print("To replace with - {0}".format(sys.argv[3]));

with open("./files/{0}".format(fileName), 'rt') as readFile:
    if (existingString in readFile.read()):
        data = readFile.read();
        data = data.replace(existingString, newString);
    else:
        print("String is not found.");

if (len(data)):
    with open(fileName, 'wt') as writeFile:
        writeFile.write(data);
        print("Replaced successfully.");
