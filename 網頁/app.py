from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("主頁.html")


@app.route("/目錄")
def liste():
    return render_template("目錄.html")


@app.route("/Kards")
def Kards_main():
    return render_template("Kards.html")


@app.route("/Kards 美國")
def Kards_us():
    return render_template("Kards 美國.html")


@app.route("/Kards 英國")
def Kards_uk():
    return render_template("Kards 英國.html")


@app.route("/Kards 美國 很多解牌")
def Kards_us_many():
    return render_template("Kards 美國 很多解牌.html")


@app.route("/Kards 美國 高油")
def Kards_us_high():
    return render_template("Kards 美國 高油.html")


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
