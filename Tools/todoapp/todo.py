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
        td = db.getTodoByfinished("true")
        for i in range(len(td)):
            output =''
            for j in td[i]:
                output += f" {j} "
    
            print(output)


    if cmd=="list" and flag =="unfinished":

        print("listing unfinished")

        td = db.getTodoByfinished("false")
        for i in range(len(td)):
            output =''
            for j in td[i]:
                output += f" {j} "
    
            print(output)


    if cmd=="add":
        print("adding")

        pk =input(" ENTER PK: ")
        td = input(" ENTER TODO: ")
        fin = "false"
        dt ="21 june 2022"
        pr =input(" ENTER PRIORITY: ")
        pr =int(pr)
        dtFin = " not yet "


        MyTodo =db.Todo(pk,td,fin,pr,dt,dtFin)
        db.insertTodo(MyTodo)

        
    if cmd=="update":
        print("updating")

    if cmd=="markdone":
        print("marking Done")
        pk = input(" ENTER KEY ")
        pk =int(pk)
        db.updatefinished(pk,"true")

    if cmd =="remove":
        pk =input("ENTER KEY ")
        db.removeTodo(int(pk))


else :
    pass
