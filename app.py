from flask import render_template 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/overview")
def overview():
    return render_template("overview.html")

if __name__ == "__main__":
    app.run(debug=True, port=2905)