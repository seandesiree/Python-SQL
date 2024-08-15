import mysql.connector


con = mysql.connector.connect(
    user='root', 
    password='evangelista4ever',
    host='localhost', 
    database='new_schema'
    )


cursor = con.cursor()


def add_member(id, name, age):
    try:
        query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query, (id,))
        if cursor.fetchone():
            print("Member with ID {} already exists.".format(id))
            return
        
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (id, name, age))
        con.commit()
        print("New member added successfully.")
    except mysql.connector.Error as err:
        print("Error adding member: {}".format(err))
    finally:
        cursor.close()


def add_workout_session(session_id, member_id, session_date, session_time, activity):
    try:
        query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query, (member_id,))
        if not cursor.fetchone():
            print("Member with ID {} does not exist.".format(member_id))
            return
        
        query = "INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (session_id, member_id, session_date, session_time, activity))
        con.commit()
        print("Workout Session added successfully.")
    except mysql.connector.Error as err:
        print("Error adding member: {}".format(err))
    finally:
        cursor.close()


def update_member_age(id, age):
    try:
        query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query, (id,))
        if not cursor.fetchone():
            print("Member with ID {} does not exist.".format(id))
            return
        
        query = "UPDATE Members set age = %s WHERE id = %s"
        cursor.execute(query, (id, age))
        con.commit()
        print("Members age successfully updated.")
    except mysql.connector.Error as err:
        print("Error adding member: {}".format(err))
    finally:
        cursor.close()


def delete_session_id(session_id):
    try:
        query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query, (session_id,))
        if not cursor.fetchone():
            print("Session ID does not exist.".format(session_id))
            return
        
        query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query, (session_id, ))
        con.commit()
        print("Members age successfully updated.")
    except mysql.connector.Error as err:
        print("Error adding member: {}".format(err))
    finally:
        cursor.close()

#add_member(4, "Tiffany", 55)

#add_workout_session(412, 4, "2024-02-28", "15:00", "Fencing")

#update_member_age(4, 45)

#delete_session_id(112, )