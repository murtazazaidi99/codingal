#Activity 1
#write to a file]
with open("sample.txt","w") as f:
    f.write("welcome \n how are you \n this is a file operation")

#read the file
with open("sample.txt","r") as f:
    content=f.read()
    print("full content:\n",content)

# split content in to words and store in list
words=content.split()
print("\nsplit words:",words)

#close the file (not needed when using 'with',it auto-closes)

