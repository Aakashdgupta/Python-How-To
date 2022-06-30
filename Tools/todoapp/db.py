import sqlite3



class Todo:

    def __init__(self,objective,finished,priority,addedon,finishedon) -> None:
        self.objective =objective
        self.finished = finished
        self.priority =priority
        self.addedon = addedon
        self.finishedon =finishedon
        
    






conn = sqlite3.connect("todo.db")
c = conn.cursor()

# Create table if it doesnt exists already
c.execute('''
SELECT count(name) FROM sqlite_master WHERE type='table' AND name='todos';
''')

if c.fetchone()[0]==1:
    # print("TABLE EXISTS ")
    pass
else:

    c.execute(''' CREATE TABLE todos (
        no INTEGER PRIMARY KEY ,
        objective text,
        finished text,
        priority integer,
        addedon text,
        finishedon text
    )
    ''')

def insertTodo(td):
    with conn:
        c.execute("INSERT INTO todos(objective,finished,priority,addedon,finishedon) VALUES(?,?,?,?,?)",(td.objective,td.finished,td.priority,td.addedon,td.finishedon))
        # c.execute("INSERT INTO todos VALUES (:no,:objective,:finished,:priority,:addedon,:finishedon)",
        # {"no":td.no,objective":td.objective,"finished":td.finished,"priority":td.priority,"addedon":td.addedon,"finishedon":td.finishedon})
    

def getTodoByfinished(finished):
    c.execute("SELECT * FROM todos WHERE finished=:finished",{"finished":finished})
    return c.fetchall()

def updatefinished(no,finished,dt):
    with conn:
        c.execute('''UPDATE todos SET finished =:finished ,finishedon =:dt
        WHERE no =:no''',
        {"finished":finished,"no":no,"dt":dt})

def removeTodo(no):
    with conn:
        c.execute("DELETE FROM todos WHERE no=:no",{"no":no})
    



