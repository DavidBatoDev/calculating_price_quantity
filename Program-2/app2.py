from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    max_apple = 0
    remaining_money = 0
    if request.method == "POST":
        money = float(request.form.get("money"))
        apple_price = float(request.form.get("apple_price"))
        print(money, apple_price)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)