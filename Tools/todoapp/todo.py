import sys
import db
import datetime

from colorama import Fore,Back,Style
def coloredTodoText(no,todo,status,added,finished):
    td = f"  {no} : {todo} "
    meta = f"  adeed on : {added} finished on {finished}  "
    if status =="false":
        print("\t" + Back.WHITE + Fore.RED + td.upper())
        print(Style.RESET_ALL,end="")
        print("\t" + Back.WHITE + Fore.BLACK + meta)
        print(Style.RESET_ALL)
    if status =="true":
        print("\t" + Back.WHITE + Fore.GREEN + td.upper())
        print(Style.RESET_ALL,end="")
        print("\t" + Back.WHITE + Fore.BLACK + meta)
        print(Style.RESET_ALL)



if len(sys.argv)>1:
    cmd =sys.argv[1]

    if len(sys.argv)>2:
        flag =  sys.argv[2]

    if cmd=="list" and flag =="all":
        print("\t ALL TASKS ")

        td = db.getTodoByfinished("false")
        for i in range(len(td)):
            coloredTodoText(td[i][0],td[i][1], td[i][2], td[i][4], td[i][-1])


        td = db.getTodoByfinished("true")
        for i in range(len(td)):
            coloredTodoText(td[i][0],td[i][1], td[i][2], td[i][4], td[i][-1])
           

    if cmd=="list" and flag=="finished":

        print("\t ALL FINISHED TASKS ")
        td = db.getTodoByfinished("true")
        for i in range(len(td)):
            coloredTodoText(td[i][0],td[i][1], td[i][2], td[i][4], td[i][-1])



    if cmd=="list" and flag =="unfinished":

        print("\t ALL UNFINISAHED TASKS ")

        td = db.getTodoByfinished("false")
        for i in range(len(td)):
            coloredTodoText(td[i][0],td[i][1], td[i][2], td[i][4], td[i][-1])


    if cmd=="add":
        print("adding")

        pk =input(" ENTER PK: ")
        td = input(" ENTER TODO: ")
        fin = "false"
        dt =str(datetime.datetime.now().date())
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
        dt = str(datetime.datetime.now().date())
        db.updatefinished(pk,"true",dt)

    if cmd =="remove":
        pk =input("ENTER KEY ")
        db.removeTodo(int(pk))


else :
    pass
