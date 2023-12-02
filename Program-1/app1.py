from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "secret_key"

products = [
    {
        "product_id": "1",
        "product_name": "Apple",
        "product_price": "20",
        "product_image": "../static/8d08605efc68a981f4042d80ac1676e5_large.png",
    },
    {
        "product_id": "2",
        "product_name": "Orange",
        "product_price": "25",
        "product_image": "../static/orangelargerevised_1600x.webp",
    },
]


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/cart")
def show_cart():
    return render_template("cart.html")


if __name__ == "__main__":
    app.run(debug=True)