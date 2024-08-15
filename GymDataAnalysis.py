import mysql.connector


con = mysql.connector.connect(
    user='root', 
    password='evangelista4ever',
    host='localhost', 
    database='new_schema')


cursor = con.cursor()

def get_members_in_age_range(start_age, end_age):
    try:
        query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))
        results = cursor.fetchall()
        
        if len(results) == 0:
            print("No members found in the age range {} - {}.".format(start_age, end_age))
            return
        
        print("Members in the age range {} - {}:".format(start_age, end_age))
        for member in results:
            print("Name: {}, Age: {}".format(member[1], member[2]))
    except mysql.connector.Error as err:
        print("Error retrieving members: {}".format(err))
    finally:
        cursor.close()

get_members_in_age_range(25, 30)

con.close