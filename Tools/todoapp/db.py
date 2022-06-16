import sqlite3



class Todo:

    def __init__(self,no,objective,finished,priority,addedon,finishedon) -> None:
        self.no = no
        self.objective =objective
        self.finished = finished
        self.priority =priority
        self.addedon = addedon
        self.finishedon =finishedon
        
    






conn = sqlite3.connect("todo.db")
c = conn.cursor()

# c.execute(''' CREATE TABLE todos (
#     no integer,
#     objective text,
#     finished text,
#     priority integer,
#     addedon text,
#     finishedon text
# )
# ''')

def insertTodo(td):
    with conn:
        c.execute("INSERT INTO todos VALUES (:no,:objective,:finished,:priority,:addedon,:finishedon)",
        {"no":td.no,"objective":td.objective,"finished":td.finished,"priority":td.priority,"addedon":td.addedon,"finishedon":td.finishedon})
    

def getTodoByfinished(finished):
    c.execute("SELECT * FROM todos WHERE finished=:finished",{"finished":finished})
    return c.fetchall()

def updatefinished(no,finished):
    with conn:
        c.execute('''UPDATE todos SET finished =:finished 
        WHERE no =:no''',
        {"finished":finished,"no":no})

def removeTodo(no):
    with conn:
        c.execute("DELETE FROM todos WHERE no=:no",{"no":no})
    


import todo

td1 =todo.Todo(1,"test","false",10,"16 june 2022","notyetfinished")
td2 =todo.Todo(2,"test 222","false",9,"16 june 2022","notyetfinished")

# insertTodo(td1)
# insertTodo(td2)

updatefinished(1,"true")
td = getTodoByfinished("false")

removeTodo(1)

conn.close()

for i in range(len(td)):
    output =''
    for j in td[i]:
        output += f" {j} "
    
    print(output)
# for t in todo:
#     print(t)