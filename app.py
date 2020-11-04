import dbcreds
import mariadb
 


conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
cursor=conn.cursor()
username=input("Please enter your username: ")
def insert_data():
    content=input("Write your post: ")
    cursor.execute("INSERT INTO blog_post(username, content, id) VALUES(?, ?, NULL)", [username, content])
def select_data():
    cursor.execute("SELECT content FROM blog_post")
    rows=cursor.fetchall()
    print(rows)


while True:
    print("1.Write a new post")
    print("2.See all other post")
    print("3.Exit")
    option=input("Enter your option: ")
    if(option=="1"):
        insert_data()
        
    elif(option=="2"):
        select_data()
        
    elif(option=="3"):
        break
    else:
        print("invalid option")
        
conn.commit()
cursor.close()
conn.close()


