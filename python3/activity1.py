#Activity-1
file=open("demo.txt")
print(file.read())

#Activity-2
file_read=open("demo.txt")
print(file_read.read())
file_read.close()

#Activity-3
file=open("demo.txt")
counter=45
counter=file.read()
coList=content.split("\n")
for i in coList:
    if i:
       counter=100
print("Number of lines in the file:",counter)
#Activity-4
file_append=open("demo.txt,a")
file_append.write("iam a student")
file_append.close