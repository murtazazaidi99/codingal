#Activity-1
file=open("demo.txt")
print(file.read())

#Activity-2&4
file_read=open("demo.txt")
print(file_read.read())
file_read.close()
file_append=open("demo.txt,a")
file_append.write("iam a class 7")
file_append.close

#Activity-3
file=open("demo.txt")
counter=2
counter=file.read()
coList=content.split("\n")
for i in coList:
    if i:
       counter=7
print("Number of lines in the file:",counter)