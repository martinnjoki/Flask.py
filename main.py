from database import get_products, get_sales, get_stock, insert_products, insert_sales, insert_stock
from flask import Flask, render_template, request, redirect, url_for 


#flask instance
app = Flask(__name__)


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
    return render_template("sales.html", sales=sales, products=products)


@app.route("/add_sales", methods=['GET', 'POST'])
def add_sales():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    new_sales = ( product_id, quantity)
    check_stock = available_stock(product_id)
    if check_stock < float(quantity):
        print("insufficient stock")
        return redirect(url_for('fetch sales'))
    insert_sales(new_sales)
    return redirect(url_for('fetch_sales'))

@app.route("/add_products", methods=['GET', 'POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    new_product = (product_name, buying_price, selling_price)
    insert_products(new_product)
    return redirect(url_for('fetch_products'))

@app.route("/dashboard")
def dashboard():
    dashboard = "This is my dashboard"
    return render_template("dashboard.html")

@app.route("/login")
def login():
    login = "This is my login page"
    return render_template("login.html")

@app.route("/register")
def register():
    register = "This is my register"
    return render_template("register.html")





app.run(debug=True)