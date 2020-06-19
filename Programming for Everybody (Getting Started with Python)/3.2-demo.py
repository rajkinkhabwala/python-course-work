rawstr = input("Enter a number: ")

try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print("Number you have enter: ",ival)
else:
    print("You have not enter a number! Please check")
