from flask import Flask, render_template, request

app = Flask(__name__)

# Mengizinkan method GET (membuka halaman) dan POST (mengirim data form)
@app.route("/", methods=["GET", "POST"])
def index():
    nama = None
    if request.method == "POST":
        # Mengambil parameter 'nama_user' yang dikirim dari form HTML
        nama = request.form.get("nama_user")
    
    # Menampilkan index.html sambil mengirim variabel 'nama'
    return render_template("index.html", nama=nama)

if __name__ == "__main__":
    app.run(debug=True)