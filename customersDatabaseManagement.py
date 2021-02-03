import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
)

mycursor = mydb.cursor()

def addCustomers():
    name = input("Enter new name: ")
    address = input("Enter new address: ")
    query = "SELECT count(*) FROM customers where address = '{}' and name = '{}'".format(address, name)
    print(query)
    mycursor.execute(query)
    
    myresult = mycursor.fetchall()
    
    count = myresult[0][0]
    print(count)
    
    if count == 0:
        sql = "INSERT INTO customers (name, address) VALUE (%s, %s)"
        val = (name, address)
        mycursor.execute(sql, val)
    
        mydb.commit()
    
        print(mycursor.rowcount, "records inserted.")
        customersMenu()
    else:
        print("Dup")
        customersMenu()
    
        
def updateCustomers():
    idee = int(input("What id would you like to update?: "))
    if (idee != 0):
        mycursor.execute("select * from customers where id = {};".format(idee))
        myresult = mycursor.fetchall()
        print(myresult)
        name = input("Enter new name: ")
        address = input("Enter new address: ")
        sure = input("Are you sure? Y/N: ")
        if (sure == "Y"):
            query = "UPDATE customers SET name = '{}', address = '{}' WHERE id = {}".format(name, address, idee)
            mycursor.execute(query)
            mydb.commit()
            updateCustomers()
        elif (sure == "N"):
            updateCustomers()
    elif (idee == 0):
        customersMenu()


def removeCustomers():
    idee = int(input("What id would you like to remove?: "))
    if (idee != 0):
        mycursor.execute("select * from customers where id = {};".format(idee))
        myresult = mycursor.fetchall()
        print(myresult)
        sure = input("Are you sure? Y/N: ")
        if (sure == "Y"):
            query = "DELETE FROM customers WHERE id = {}".format(idee)
            mycursor.execute(query)
            mydb.commit()
            removeCustomers()
        elif (sure == "N"):
            removeCustomers()
    elif (idee == 0):
        customersMenu()
    
def customersMenu():
    key = input("Add, Update, Remove, Show or Stop running Customers?: ")
    if (key == "Add"):
        addCustomers()
    elif (key == "Update"):
        updateCustomers()
    elif (key == "Remove"):
        removeCustomers()
    elif (key == "Show"):
        query = "SELECT * FROM customers;"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for row in myresult:
            print(row)
        customersMenu()
    elif (key == "Stop"):
        print("Stopping")
    else:
        customersMenu()
    
    
customersMenu()