from flask import Flask, render_template 

app = Flask(__name__)

projects = [
    {
        "name": "Project 1",
        "description": "yeah yeah dodoodododo",
        "url": "https://hackclub.com/YEAHYEAH/"
    },
    {
        "name": "Project345t3 2",
        "description": "yeah yeah dodoodododo",
        "url": "https://hackclub.com/YEAHYEAH/"
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/overview")
def overview():
    return render_template("overview.html", projects=projects)

@app.route("/what")
def what():
    return render_template("what.html")

if __name__ == "__main__":
    app.run(debug=True, port=2905)