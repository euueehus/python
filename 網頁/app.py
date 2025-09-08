from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/list")
def liste():
    return render_template("list.html")


@app.route("/Kards")
def Kards_main():
    return render_template("Kards.html")


@app.route("/Kards_us")
def Kards_us():
    return render_template("Kards_us.html")


@app.route("/Kards_uk")
def Kards_uk():
    return render_template("Kards_uk.html")


@app.route("/Kards_us_many")
def Kards_us_many():
    return render_template("Kards_us_many.html")


@app.route("/Kards_us_high")
def Kards_us_high():
    return render_template("Kards_us_high.html")


@app.route("/intro")
def intro():
    return render_template("intro.html")


@app.route("/minecraft")
def minecraft():
    return render_template("minecraft.html")


@app.route("/delta")
def delta():
    return render_template("delta.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
