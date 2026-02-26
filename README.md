# shopingCartFlaskApi
---

# 📚 Flask Book Store with Session-Based Cart

A minimal book store web application built with Flask, SQLite, and server-side sessions.
Users can browse books, add them to a cart, and manage their cart without authentication.

---

## 📌 Description

This project implements a simple e-commerce-style cart system using Flask and SQLite. It demonstrates:

* Server-side session management using `Flask-Session`
* Dynamic SQL queries with parameterized placeholders
* SQLite database integration
* Cart persistence across requests
* Clean separation of routes and templates

The cart is stored in the user session (filesystem-based), simulating real-world shopping cart behavior.

---

## 🚀 Features

* Display books from SQLite database
* Add books to cart
* Persist cart using server-side sessions
* View cart contents
* Clear entire cart
* Redirect-based POST handling (PRG pattern)

---

## 🛠 Tech Stack

* **Python 3**
* **Flask**
* **Flask-Session**
* **SQLite3**
* **Jinja2**
* **HTML5**

---

## 📂 Project Structure

```
flask-bookstore/
│
├── app.py
├── books.db
├── requirements.txt
├── README.md
│
└── templates/
    ├── layout.html
    ├── books.html
    └── cart.html
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/jayssSmm/shopingCartFlaskApi.git
cd flask-bookstore
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Ensure `requirements.txt` includes:

```
Flask
Flask-Session
```

### 4️⃣ Run the application

```bash
python app.py
```

The application will run at:

```
http://127.0.0.1:5000/
```

---

## ▶️ Usage

### Browse Books

* Visit the homepage (`/`)
* All books stored in the database will be displayed

### Add to Cart

* Click **Add to cart** under any book
* You will be redirected to `/cart`

### View Cart

* Displays selected books
* Items persist across page reloads due to session storage

### Clear Cart

* Click **Clear Cart**
* Session cart resets to empty list

---

## 🧠 How It Works (Technical Overview)

### 1️⃣ Book Listing

* `/` route fetches all records from `books.db`
* Renders `books.html` with database rows

### 2️⃣ Cart Storage

* Session key `session['cart']` stores book IDs
* Data stored server-side using filesystem session

### 3️⃣ Dynamic SQL Query

When viewing the cart:

```python
placeholder = ','.join(['(?)'] * len(session['cart']))
cursor.execute(
    f'SELECT * FROM books WHERE id IN ({placeholder})',
    session['cart']
)
```

This dynamically builds the correct number of parameterized placeholders, preventing SQL injection.

### 4️⃣ PRG Pattern

POST requests redirect to GET routes to prevent duplicate form submissions.

---

## 🔒 Security Notes

* Uses parameterized SQL queries to prevent SQL injection
* Cart stored server-side (not client cookies)
* No authentication implemented
* No CSRF protection (can be added with Flask-WTF)

---

## 🔮 Future Improvements

* Add user authentication
* Prevent duplicate items in cart
* Add quantity tracking
* Add remove-single-item functionality
* Add total price calculation
* Implement checkout simulation
* Use Flask-SQLAlchemy for ORM abstraction
* Deploy to cloud platform

---

## 📸 Screenshots

> Add screenshots here

```
/screenshots/books-page.png
/screenshots/cart-page.png
```

---

## 🤝 Contribution

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🏁 Portfolio Context

This project demonstrates:

* Understanding of session-based state management
* Backend cart logic similar to real e-commerce systems
* Dynamic SQL query construction
* Clean route separation
* Flask template rendering

It serves as a foundational backend project for learning full-stack web development concepts.

---