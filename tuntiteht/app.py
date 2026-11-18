from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Додайте число в адресний рядок, наприклад: /5"


@app.route("/<count>")
def hello(count):
    try:
        n = int(count)
        if n < 0:
            raise ValueError("Число не може бути від'ємним")
        if n > 1000:
            raise ValueError("Забагато повторів (максимум 1000)")
        return "<br>".join(["Hello world!"] * n)
    except ValueError as e:
        return f"Помилка: введіть ціле число від 0 до 1000. ({e})", 400


if __name__ == "__main__":
    app.run(debug=True)