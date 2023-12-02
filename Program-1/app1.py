from flask import Flask, render_template, redirect, url_for, request, flash, request

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


cart = []


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    quantity = int(request.form.get("quantity", 1))
    product = next(
        (product for product in products if product["product_id"] == str(product_id)),
        None,
    )
    if product:
        existing_product = next(
            (item for item in cart if item["product_id"] == str(product_id)),
            None,
        )
        if existing_product:
            existing_product["product_quantity"] += quantity
            flash("Product quantity updated in cart")
        else:
            cart.append(
                {
                    "product_id": product["product_id"],
                    "product_name": product["product_name"],
                    "product_price": product["product_price"],
                    "product_quantity": quantity,
                    "product_image": product["product_image"],
                }
            )
            flash("Product added to cart")
    print(cart)
    return redirect(url_for("index"))


@app.route("/cart")
def show_cart():
    total_price = 0

    for item in cart:
        product_price = int(item["product_price"])
        product_quantity = item["product_quantity"]
        total_price += product_price * product_quantity

    return render_template("cart.html", cart=cart, total=total_price)


if __name__ == "__main__":
    app.run(debug=True)
