import os
# getting current working directory
CWD = os.getcwd()

# adding Tools folder to path
CWD = os.path.join(CWD, "Tools")
# adding filewriter folder to path
CWD = os.path.join(CWD, "filewriter")

# print(CWD)

# setting modified path as cwd
os.chdir(CWD)

# print(os.listdir())

filename = input(" Enter the desired file name with extension ")
noOfLine = input(" Enter number of lines you wants to write ")

print(" Enter Text to write ")
contents = []
for i in range(int(noOfLine)):
    con = input()
    contents.append(con)


with open(filename, 'w') as f:
    for con in contents:
        f.write(con + "\n")