""" 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer. """

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email = dict()

for lines in handle :
    if lines.startswith('From ') :
        words = lines.split()
        data = words[1]
        email[data] = email.get(data,0) + 1
    
bigCount = None
bigEmail = None

for email_data, count in email.items() :
    if bigCount is None or count > bigCount :
        bigCount = count
        bigEmail = email_data

print(bigEmail,bigCount)