import streamlit as st
import mysql.connector
from mysql.connector import Error

# Function to connect to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Change if your MySQL is hosted remotely
            database='student_info',
            user='root',  # Replace with your MySQL username
            password='Govar@768'  # Replace with your MySQL password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error while connecting to MySQL: {e}")
        return None

# Function to insert data into MySQL database
def insert_data(name, grade, school_name, roll_number):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """INSERT INTO students (name, grade, school_name, roll_number) 
                       VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (name, grade, school_name, roll_number))
            connection.commit()
            cursor.close()
            st.success("Data has been successfully inserted into the database!")
        except Error as e:
            st.error(f"Error while inserting data: {e}")
        finally:
            if connection.is_connected():
                connection.close()

# Streamlit UI
st.title("Student Information Form")

name = st.text_input("Enter your name:")
grade = st.text_input("Enter your grade:")
school_name = st.text_input("Enter your school name:")
roll_number = st.text_input("Enter your roll number:")

if st.button("Submit"):
    if name and grade and school_name and roll_number:
        insert_data(name, grade, school_name, roll_number)
    else:
        st.error("Please fill out all fields!")
