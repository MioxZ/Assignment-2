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

with open(fileName, 'rt') as readFile:
    data = readFile.read();
    if (existingString not in data):
        print("string is not found");
    else:
        data = data.replace(existingString, newString);

with open(fileName, 'wt') as writefile:
    writefile.write(data);
    print("Replaced successfully.");
