from flask import Flask
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
)
    
mycursor = mydb.cursor()

query = "SELECT * FROM customers;"
mycursor.execute(query)


@app.route('/')
def showCustomers():
    
    myresult = mycursor.fetchone()
    output = "<h1><table><tr><td>" + myresult[1] + "</td><td>" + myresult[2] + "</td><tr/>"
    
    myresult = mycursor.fetchone()
    output = output + "<tr><td>" + myresult[1] + "</td><td>" + myresult[2] + "</td><tr/>"
    
    myresult = mycursor.fetchone()
    output = output + "<tr><td>" + myresult[1] + "</td><td>" + myresult[2] + "</td><tr/>"

    myresult = mycursor.fetchone()
    output = output + "<tr><td>" + myresult[1] + "</td><td>" + myresult[2] + "</td><tr/></table></h1>"
    
    return output
    

if __name__ == "__main__":
    app.run()