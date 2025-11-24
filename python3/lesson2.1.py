import os
filename="sample.txt"

#check if file exists
if os.path.exists(filename):
    print(f"{filename} already exists.")
else:
    print(f"{filename} doesnot exists.creating one...")
    with open(filename,'w') as f:
        f.write("this is a newly created file.\n")