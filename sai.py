import os
file_type=".txt" # Make sure only .tt files are considered
word_count={}
directory=input("Enter Folder Path:")
os.chdir(directory)
for filename in os.listdir(directory):
    if filename.endswith(file_type):
        file_content = open(filename,"r")
        for line in file_content:
            words=line.split()
            for word in words:
                if word.lower() in word_count:
                    word_count[word.lower()]+=1
                else:
                    word_count[word.lower()]=1
        file_content.close()
print({k: v for k, v in sorted(word_count.items(), key=lambda item: item[1],reverse=True) if v>=3})