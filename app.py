
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form["nama"]
        umur = request.form["umur"]
        asal = request.form["asal"]

        return render_template(
            "index.html",
            nama=nama,
            umur=umur,
            asal=asal,
            hasil=True
        )

    return render_template("index.html", hasil=False)

if __name__ == "__main__":
    app.run(debug=True)