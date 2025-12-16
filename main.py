from database import get_products, get_sales, get_stock, get_users, insert_products, insert_sales, available_stock, insert_users
from flask import Flask, render_template, request, redirect, url_for, flash


#flask instance
app = Flask(__name__)

#secret key signs sessions data
app.secret_key = 'fedele'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stock")
def fetch_stock():
    stock = get_stock()
    return render_template("stock.html", stock=stock)


@app.route("/products")
def fetch_products():
    products = get_products()
    return render_template("products.html", products=products)


@app.route("/sales")
def fetch_sales():
    sales = get_sales()
    products =get_products()
    return render_template("sales.html", sales=sales, products = products)


@app.route("/add_sales", methods=['GET', 'POST'])
def add_sales():
    pid = request.form['pid']
    quantity = request.form['quantity']
    new_sale = ( pid, quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        flash("insufficient stock", 'danger')
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    flash("Sale made successfully", 'success')
    return redirect(url_for('fetch_sales'))

@app.route("/add_products", methods=['GET', 'POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    new_product = (product_name, buying_price, selling_price)
    insert_products(new_product)
    flash("product added successfully", 'success')
    return redirect(url_for('fetch_products'))

@app.route("/dashboard")
def dashboard():
    dashboard = "This is my dashboard"
    return render_template("dashboard.html")

@app.route("/login")
def login():
    login = "This is my login page"
    return render_template("login.html")

@app.route("/users", methods=['GET', 'POST'])
def fetch_users():
    users = get_users()
    full_name = request.form["full_name"]
    email = request.form["email"]
    phone_number = request.form["phone_number"]
    password = request.form["password"]
    new_users = (full_name, email, phone_number, password)
    insert_users(new_users)
    return render_template("user.html", users=users)

    

@app.route("/register")
def register():
    register = "This is my register"
    return render_template("register.html")





app.run(debug=True)