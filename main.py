from flask import Flask, render_template, request, redirect, url_for,flash
from database import get_products,get_sales,insert_products,insert_sales,available_stock,get_stock,insert_stock


#Flask instance
app = Flask(__name__)

#secret key - signs session data
app.secret_key ='98900309chhe88dhnwjwkixsiixk'


#index route
@app.route("/")
def home():
    return render_template("index.html") 


#getting products
@app.route('/products')
def fetch_products():
    products = get_products()
    return render_template("products.html",products=products)


#posting products
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price =request.form["selling_price"]
    new_product = (product_name,buying_price,selling_price)
    insert_products(new_product)
    flash("Product added successfully",'success')
    return redirect(url_for('fetch_products'))


#getting sales
@app.route('/sales')
def fetch_sales():
    sales = get_sales()
    products = get_products()
    return render_template("sales.html",sales=sales,products = products)


#posting sales
@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_sale = (pid,quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        flash("Insufficient stock",'danger')
        return url_for('fetch_sales')
    insert_sales(new_sale)
    flash("Sale made successfully",'success')
    return redirect(url_for('fetch_sales'))


#fetching stock
@app.route('/stock')
def get_stock():
    stock = get_stock()
    products = get_products()
    return render_template("stock.html",stock=stock,products=products)


#adding stock
@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    pid = request.form['pid']
    stock_quantity = request.form['s_quantity']
    new_stock = (pid,stock_quantity)
    insert_stock(new_stock)
    return redirect(url_for('get_stock'))


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html") 



app.run(debug=True)