from flask import Flask, render_template
from src.data.load_data import load_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dataset")
def dataset():

    df = load_data()

    return render_template(
        "load_dataset.html",
        tables=[df.head().to_html(classes='data', index=False)]
    )
@app.route("/eda")
def eda():
    return render_template("eda.html")


if __name__ == "__main__":
    app.run(debug=True)