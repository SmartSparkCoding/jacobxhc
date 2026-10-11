from flask import Flask, render_template 

app = Flask(__name__)

projects = [
    {
        "name": "Bento YSWS Organiser",
        "description": "I am the organiser (along with @freddie) of the YSWS Bento - where you ship a project with bento style requirements, and get free sushi in return! It is both an individual YSWS and a Club Workshop! Fun Fact - this was submitted to Bento!",
        "url": "https://bento.hackclub.com/"
    },
    {
        "name": "Hackanomous YSWS",
        "description": "Similar to Bento, I am the organiser for the Hackanomous YSWS - and upcoming YSWS! To ship, you would make a project that implements AI/ML and get free prizes from our shop!",
        "url": "https://hackanomous.vercel.app/"
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