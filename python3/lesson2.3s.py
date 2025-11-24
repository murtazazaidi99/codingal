# ACTIVITY 4
with open("sample.txt",'w') as f:
    f.write("orange\nbanana\ngrapes\nmango")

with open("sample.txt","w") as f:
    f.write("cat\nelephent\ncow\nliger")

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