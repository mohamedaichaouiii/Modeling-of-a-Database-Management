
import sqlite3
import tkinter as tk

import mysql.connector
from tkinter import messagebox
from tkinter import ttk

def insert_dept():
    new_window = tk.Toplevel(root)
    new_window.title("Insert Dept")

    num_label = tk.Label(new_window, text="Num:")
    num_label.grid(row=0, column=0)
    num_text = tk.Text(new_window, height=1, width=30)
    num_text.grid(row=0, column=1)

    nom_label = tk.Label(new_window, text="Nom:")
    nom_label.grid(row=1, column=0)
    nom_text = tk.Text(new_window, height=1, width=30)
    nom_text.grid(row=1, column=1)

    numChef_label = tk.Label(new_window, text="NumChef:")
    numChef_label.grid(row=2, column=0)
    numChef_text = tk.Text(new_window, height=1, width=30)
    numChef_text.grid(row=2, column=1)

    numAgendaDept_label = tk.Label(new_window, text="NumAgendaDept:")
    numAgendaDept_label.grid(row=3, column=0)
    numAgendaDept_text = tk.Text(new_window, height=1, width=30)
    numAgendaDept_text.grid(row=3, column=1)

   
    def insert_data():
        num = num_text.get("1.0", "end-1c")
        nom = nom_text.get("1.0", "end-1c")
        numChef = numChef_text.get("1.0", "end-1c")
        numAgendaDept = numAgendaDept_text.get("1.0", "end-1c")
       
        
        query = f"INSERT INTO departement (num, nom, numChef, numAgendaDept) VALUES ({num}, '{nom}', '{numChef}', {numAgendaDept})"
        
        try:
            c.execute(query)
            conn.commit()
            messagebox.showinfo("Done")
            new_window.destroy()

            
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error executing query: " + str(e))
            

    insert_button = tk.Button(new_window, text="Insert", command=insert_data)
    insert_button.grid(row=4, column=0, columnspan=2, pady=10)

def insert_emp():
    new_window = tk.Toplevel(root)
    new_window.title("Insert Emp")

    numEmploye_label = tk.Label(new_window, text="numEmploye:")
    numEmploye_label.grid(row=0, column=0)
    numEmploye_text = tk.Text(new_window, height=1, width=30)
    numEmploye_text.grid(row=0, column=1)

    nom_label = tk.Label(new_window, text="Nom:")
    nom_label.grid(row=1, column=0)
    nom_text = tk.Text(new_window, height=1, width=30)
    nom_text.grid(row=1, column=1)

    prenom_label = tk.Label(new_window, text="prenom:")
    prenom_label.grid(row=2, column=0)
    prenom_text = tk.Text(new_window, height=1, width=30)
    prenom_text.grid(row=2, column=1)

    telIntern_label = tk.Label(new_window, text="telIntern:")
    telIntern_label.grid(row=3, column=0)
    telIntern_text = tk.Text(new_window, height=1, width=30)
    telIntern_text.grid(row=3, column=1)

    email_label = tk.Label(new_window, text="email:")
    email_label.grid(row=4, column=0)
    email_text = tk.Text(new_window, height=1, width=30)
    email_text.grid(row=4, column=1)

    niveau_label = tk.Label(new_window, text="niveau:")
    niveau_label.grid(row=5, column=0)
    niveau_text = tk.Text(new_window, height=1, width=30)
    niveau_text.grid(row=5, column=1)

    numDept_label = tk.Label(new_window, text="numDept:")
    numDept_label.grid(row=6, column=0)
    numDept_text = tk.Text(new_window, height=1, width=30)
    numDept_text.grid(row=6, column=1)

   
    def insert_data():
        numEmploye = numEmploye_text.get("1.0", "end-1c")
        nom = nom_text.get("1.0", "end-1c")
        prenom = prenom_text.get("1.0", "end-1c")
        telIntern = telIntern_text.get("1.0", "end-1c")
        email = email_text.get("1.0", "end-1c")
        niveau= niveau_text.get("1.0", "end-1c")
        numDept= numDept_text.get("1.0", "end-1c")
        
        query = f"INSERT INTO employe (numEmploye,nom,prenom,telIntern,email,niveau,numdept) VALUES ({numEmploye}, '{nom}', '{prenom}', {telIntern} , '{email}' , {niveau} , {numDept})"
        
        try:
            c.execute(query)
            conn.commit()
            messagebox.showinfo("Done")
            new_window.destroy()

            
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error executing query: " + str(e))
            

    insert_button = tk.Button(new_window, text="Insert", command=insert_data)
    insert_button.grid(row=7, column=0, columnspan=2, pady=10)

def show_query():
    query_text.delete('1.0', tk.END)  # clear previous text
    query = 'select * from table_name'
    query_text.insert(tk.END, query)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="gl"
)
c = conn.cursor()


root = tk.Tk()
root.title("Mini_Projet")

show_message_box_button = tk.Button(root, text="Insert Dept", command=insert_dept)
show_message_box_button.pack(padx=10, pady=10)
show_message_box_button = tk.Button(root, text="Insert Emp", command=insert_emp)
show_message_box_button.pack(padx=10, pady=10)
button = tk.Button(root, text='Show Table', command=show_query)
button.pack(padx=10, pady=10)
query_label = tk.Label(root, text="Enter your SQL query:")
query_label.pack()


query_text = tk.Text(root, height=5)
query_text.pack()


execute_button = tk.Button(root, text="Execute Query", command=lambda: execute_query(query_text.get("1.0", "end-1c")))
execute_button.pack()


tree = ttk.Treeview(root)
tree.pack()


def execute_query(query):
    try:
        
        c.execute(query)

        
        
        column_names = [description[0] for description in c.description]
        data = c.fetchall()

            
        tree.delete(*tree.get_children())

            
        tree["columns"] = column_names
        for column in column_names:
            tree.column(column, width=100)
            tree.heading(column, text=column)

           
        for row in data:
            tree.insert("", "end", values=row)
        root.geometry('{}x{}'.format(root.winfo_width(), root.winfo_height()))

        

    except sqlite3.Error as e:
        messagebox.showerror("Error", "Error executing query: " + str(e))


root.mainloop()
