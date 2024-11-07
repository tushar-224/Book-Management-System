import sqlite3

conn = sqlite3.connect('library.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL
)
''')

conn.commit()
conn.close()

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to add a new book to the database
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    
    if title and author and genre:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", (title, author, genre))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book added successfully")
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "All fields are required")

# Function to search for a book in the database
def search_book():
    search_query = entry_search.get()
    if search_query:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (f"%{search_query}%", f"%{search_query}%"))
        results = cursor.fetchall()
        conn.close()
        
        listbox_books.delete(0, tk.END)
        for row in results:
            listbox_books.insert(tk.END, f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}")
    else:
        messagebox.showerror("Error", "Search query is required")

# Function to display all books in the database
def display_all_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    conn.close()
    
    listbox_books.delete(0, tk.END)
    for row in results:
        listbox_books.insert(tk.END, f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Book Management System")

# Add Book Section
frame_add = tk.Frame(root)
frame_add.pack(pady=10)

label_title = tk.Label(frame_add, text="Title")
label_title.grid(row=0, column=0, padx=5, pady=5)
entry_title = tk.Entry(frame_add)
entry_title.grid(row=0, column=1, padx=5, pady=5)

label_author = tk.Label(frame_add, text="Author")
label_author.grid(row=1, column=0, padx=5, pady=5)
entry_author = tk.Entry(frame_add)
entry_author.grid(row=1, column=1, padx=5, pady=5)

label_genre = tk.Label(frame_add, text="Genre")
label_genre.grid(row=2, column=0, padx=5, pady=5)
entry_genre = tk.Entry(frame_add)
entry_genre.grid(row=2, column=1, padx=5, pady=5)

button_add = tk.Button(frame_add, text="Add Book", command=add_book)
button_add.grid(row=3, columnspan=2, pady=10)

# Search Book Section
frame_search = tk.Frame(root)
frame_search.pack(pady=10)

label_search = tk.Label(frame_search, text="Search")
label_search.grid(row=0, column=0, padx=5, pady=5)
entry_search = tk.Entry(frame_search)
entry_search.grid(row=0, column=1, padx=5, pady=5)

button_search = tk.Button(frame_search, text="Search Book", command=search_book)
button_search.grid(row=1, columnspan=2, pady=10)

# Display All Books Section
button_display_all = tk.Button(root, text="Display All Books", command=display_all_books)
button_display_all.pack(pady=10)

listbox_books = tk.Listbox(root, width=80)
listbox_books.pack(pady=10)

# Run the main Tkinter event loop
root.mainloop()
