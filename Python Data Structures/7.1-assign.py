""" 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt """

filename = input("Enter file name: ")

try :
    fh = open(filename)
except :
    print("File "+filename+" does not exist!")
    quit()

for content in fh :
        upperCaseContent = content.upper().rstrip()
        print(upperCaseContent)


""" 
Because that is standard behavior. Not just for Python, but for all applications (at least all that I know of). 
A relative path (like 'myfile') is assumed to be in the current directory. 
That path will change depending on what directory you are sitting in when you launch the script from a shell. 
If you don't give an absolute path, how would Python know which file to use in a directory structure like this?

root
|-- dir1
|   `-- myFile
`-- dir2
    `-- myFile
 """