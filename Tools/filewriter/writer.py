
import sys


#Function definations 
def filewriter(filename="demo.txt",noOfLine=1):
    print(" Enter Text to write ")
    contents = []
    for i in range(int(noOfLine)):
        con = input()
        contents.append(con)


    with open(filename, 'w') as f:
        for con in contents:
            f.write(con + "\n")




if len(sys.argv)>2:
    filename =sys.argv[1]
    noOfLine=sys.argv[2]

    filewriter(filename,noOfLine)
else :
    filename =input(" Enter File name with extention You wants to write ")
    noOfLine =input(f" Enter Number of lines You wants to write in {filename} ")
    noOfLine =int(noOfLine)

    filewriter(filename,noOfLine)   