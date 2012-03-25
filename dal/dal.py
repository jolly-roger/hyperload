import constants
import psycopg2


def addtodo(userid, name):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    inserttodo = "select addtodo(%s, %s);" 
    cur.execute(inserttodo, (name, userid))
    conn.commit()
    cur.close()
    conn.close()

def getmytodos(userid):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    getmytodos = "select * from getmytodos(%s);"
    cur.execute(getmytodos, (userid,))
    todos = cur.fetchall()
    cur.close()
    conn.close()
    
    return todos

def getsharedwithmetodos(userid):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    getsharedwithmetodos = "select * from getsharedwithmetodos(%s);"
    cur.execute(getsharedwithmetodos, (userid,))
    todos = cur.fetchall()
    cur.close()
    conn.close()
    
    return todos
    
def gettodos(userid, statusid):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    getusertodos = "select * from getusertodos(%s, %s);"
    cur.execute(getusertodos, (userid, statusid))
    todos = cur.fetchall()
    cur.close()
    conn.close()
    
    return todos

def insertbefore(todoid, beforeid):
    pass

def setdonestatus(todoid):
    conn = psycopg2.connect(constants.DB_CONNECTION)
    cur = conn.cursor()
    setdone = "update todo set status_id = 1 where id_todo = %s;" 
    cur.execute(setdone, (todoid,))
    conn.commit()
    cur.close()
    conn.close()

#def addcomment(todoid, name):
#    conn = psycopg2.connect(constants.DB_CONNECTION)
#    cur = conn.cursor()
#    cur.execute("insert into comments (todo_id, name) values ('" + todoid + "', " + name + ");")
#    conn.commit()
#    cur.close()
#    conn.close()
#    
#def getlistcomments(todoid):
#    conn = psycopg2.connect(constants.DB_CONNECTION)
#    cur = conn.cursor()
#    cur.execute("select * from comments where todo_id = " + todoid + ";")
#    comments = cur.fetchall()
#    cur.close()
#    conn.close()
#    
#    return comments