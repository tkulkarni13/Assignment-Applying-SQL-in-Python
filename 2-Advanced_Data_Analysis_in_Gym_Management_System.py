from connect_mysql import connect_database

# Task 1: SQL BETWEEN Usage
def get_members_in_age_range(low, high):
    query = "SELECT * FROM Members WHERE age BETWEEN %s and %s"
    cursor.execute(query, (low, high))

    # Display all members in range
    for member in cursor.fetchall():
        print(member)

# Establishing connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Parameters
        low = 25
        high = 30
        get_members_in_age_range(low, high)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()