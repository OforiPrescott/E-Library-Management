from fastapi import FastAPI, HTTPException
from database import setup  # Import the database setup module

app = FastAPI()

@app.post("/books/")
async def create_book(title: str, author: str):
    try:
        cursor = setup.conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author)
        )
        setup.conn.commit()
        book_id = cursor.lastrowid
        return {"id": book_id, "title": title, "author": author, "available": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    try:
        cursor = setup.conn.cursor()
        cursor.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )
        book = cursor.fetchone()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"id": book[0], "title": book[1], "author": book[2], "available": book[3]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
