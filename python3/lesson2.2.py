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