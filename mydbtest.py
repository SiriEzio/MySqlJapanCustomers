import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
)

mycursor = mydb.cursor()

platform = '';
while (platform != 'None'):
    platform = input("Enter the Platform: ")

    query = "select score, title, platform from gamz where platform = '{}' order by score desc, title limit 5;".format(platform)
    
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    
