from db_config import get_db_connection

def insert_student(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO students (name, email, dob, department, phone)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
