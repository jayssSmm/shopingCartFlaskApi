import sqlite3
from flask import Flask, request,session,redirect,render_template
from flask_session import Session

app=Flask(__name__)

app.config['SESSION_PERMANENT']=False
app.config['SESSION_TYPE']='filesystem'
Session(app)

@app.route('/')
def index():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM books;')
    row=cursor.fetchall()
    conn.close()

    return render_template('books.html',books=row)

@app.route('/cart', methods=['GET','POST'])
def cart():

    if 'cart' not in session:
        session['cart']=[]

    if request.method=='POST':
        book_id=request.form.get('id')
        if book_id:
            session['cart'].append(int(book_id)) 
        return redirect('/cart')
    
    if session['cart']==[]:
        rows=[]
    else:
        conn = sqlite3.connect('books.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        placeholder= ','.join(['?']*len(session['cart']))
        cursor.execute(f'SELECT * FROM books WHERE id IN ({placeholder})',session['cart'])
        rows=cursor.fetchall()
        conn.close()

    return render_template('cart.html',books=rows)

@app.route('/clearCart', methods=['POST'])
def clearCart():
    session['cart']=[]
    print("Cart contents:", session['cart'])
    print("Length:", len(session['cart']))
    return redirect('/cart')