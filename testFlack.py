import mysql.connector
from flask import Flask

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
)

mycursor = mydb.cursor()
query = "SELECT * FROM customers"
mycursor.execute(query)


@app.route("/")
 
def getDatabase():
    
    myresults = mycursor.fetchone()
    showDatabase = "<h1>" + myresults[1] + " " + myresults[2]
    myresults = mycursor.fetchone()
    showDatabase = showDatabase + " " + myresults[1] + " " + myresults[2]
    myresults = mycursor.fetchone()
    showDatabase = showDatabase + " " + myresults[1] + " " + myresults[2] 
    myresults = mycursor.fetchone()
    showDatabase = showDatabase + " " + myresults[1] + " " + myresults[2] + "<h1>"
    return showDatabase



if __name__ == "__main__":
    app.run()