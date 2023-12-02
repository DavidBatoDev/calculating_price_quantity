from flask import Flask, request, render_template

app = Flask(__name__)


def get_max_apples(money, apple_price):
    return int(money / apple_price)


def calculate_remaining_money(money, apple_price):
    return money % apple_price


@app.route("/", methods=["GET", "POST"])
def index():
    max_apples = 0
    remaining_money = 0
    if request.method == "POST":
        money = float(request.form.get("money"))
        apple_price = float(request.form.get("apple_price"))
        max_apples = get_max_apples(money, apple_price)
        error_message = "Your money is not enough to buy an apple."
        if max_apples == 0:
            remaining_money = error_message
        else:
            remaining_money = calculate_remaining_money(money, apple_price)
            remaining_money = (
                format(remaining_money, ".2f") if remaining_money is not None else "0"
            )
    return render_template(
        "index.html", max_apples=max_apples, remaining_money="P" + str(remaining_money)
    )


if __name__ == "__main__":
    app.run(debug=True)

# PROGRAM 2 END
