from flask import Flask
import mysql.connector

app = Flask(__name__)




@app.route('/')
def showCustomers():
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
    )
    
    mycursor = mydb.cursor()

    query = "SELECT * FROM customers;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    
    output = "<h1>" + myresult + "</h1>"
    
    
    return output
    

if __name__ == "__main__":
    app.run()