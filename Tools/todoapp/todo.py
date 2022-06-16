import sys
import db


if len(sys.argv)>1:
    cmd =sys.argv[1]

    if len(sys.argv)>2:
        flag =  sys.argv[2]

    if cmd=="list" and flag =="all":
        print("listing All")
    if cmd=="list" and flag=="finished":
        print("listing Finished")
    if cmd=="list" and flag =="unfinished":
        print("listing unfinished")
    if cmd=="add":
        print("adding")
    if cmd=="update":
        print("updating")
    if cmd=="markdone":
        print("marking Done")


else :
    pass
