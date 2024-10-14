from connect_mysql import connect_database

# Task 1: Add a member
def add_member(name, age):
    query = "INSERT INTO Members (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    print("New member added.")

# Task 2: Add a workout session
def add_workout_session(member_id, session_date, session_time, activity):
    query = "INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity)\
    VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (member_id, session_date, session_time, activity))
    print("New workout session added.")

# Task 3: Updating member information
def update_member_age(member_id, new_age):
    query = "UPDATE Members SET age = %s WHERE id = %s"
    cursor.execute(query, (new_age, member_id))
    print("Member age updated.")

# Task 4: Delete a workout session
def delete_workout_session(session_id):
    query = "SELECT session_id FROM WorkoutSessions WHERE session_id = %s"
    cursor.execute(query, (session_id,))
    session = cursor.fetchone()

    if session:
        delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(delete_query, (session_id,))
        print("Session deleted.")
    else:
        print("Session not found.")

# Displays member and workout session data together
def display_data ():
    query = """
            select w.session_id, m.id as member_id, m.name, m.age, w.session_date, w.session_time, w.activity
            from Workoutsessions as w, Members as m
            where m.id = w.member_id
            order by w.session_id asc;
            """
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)


# Establishing connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Add member
        # add_member("Jonathan Smith", 29)

        # Add workout session
        # add_workout_session(cursor.lastrowid, "2023-01-01", "14:00 - 16:00", "punching bag")

        # Update member age
        # update_member_age(6, 28)

        # Delete workout session
        delete_workout_session(10)
        

        conn.commit()

        # Display complete database
        display_data()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()