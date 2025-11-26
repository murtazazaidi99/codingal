#Activity 1
with open("sample.txt","w") as f:
    f.write("hello\n i am zaidi\n welcome to a codingal")

#read the file
with open("sample.txt","r") as f:
    content=f.read()
    print("half content:\n",content)

# split content in to words and store in list
words=content.split()
print("\nsplit words",words)

#close the file (not needed when using 'with',it auto-close

import os
filename="sample.txt"

# check if file extsts
if os.path.exists(filename):
    print(f"{filename} already exists.")
else:
    print(f"{filename} does'nt exists.creating one...")
    with open(filename,'w') as f:
        f.write("this is second  created file.\n")

import os 
filename= 'sample.txt'

#deleated the file
if os.path.exists(filename):
    os.remove(filename)
    print("file deleted:",filename)
else:
    print("file not found to deleted.")
#checkagain
if os.path.exists(filename):
    print("file still exists.")
else:
    print("file doesnot exists after deletion.")





    # ACTIVITY 4
with open("sample.txt",'w') as f:
    f.write("liger\n monkey\n zabracrossing\n horce")

with open("sample.txt","w") as f:
    f.write("dolphin\n wale\n star fish\n shark")

#step 2; function to remove duplicates from a file
def remove_duplicates(input_file,output_file):
    with open (input_file,"r") as f:
        lines=f.readlines()

#remove duplites lines(order preserved)
unique_lines=list(dict.fromkeys(lines))

with open(output_file ,"w") as f:
    f.writelines(unique_lines)

#reove duplites from both files
remove_duplites("sample.txt","sample_clean.txt")
remove_duplites("sample.txt","sample_clean.txt")

#step3 merge both cleaned files into one

files_to_merge=("file_clean.txt","file_clean.txt")

with open("mergedd.txt","w") as outfile:
    for fname in files_to_merge:
        with open (fname,"r") as infile:
            outfile.write(infile.read())

#final
print("duplites lines remove from sample.txt and sample.txt")
print("clean files created:samole_clean.txt,sample_clean.txt")
print("files successfully merged in merged.txt")