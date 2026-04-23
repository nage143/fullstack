import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rao@1234",   
        database="university_db"
    )

    return conn