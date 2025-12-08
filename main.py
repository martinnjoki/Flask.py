from flask import Flask, render_template
from database import get_products, get_sales


#flask instance
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def fetch_products():
    products = get_products()
    return render_template("products.html", products=products)

@app.route("/sales")
def fetch_sales():
    sales = get_sales()
    return render_template("sales.html", sales=sales)

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