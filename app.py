from flask import Flask, render_template

app = Flask(__name__, template_folder='uitemplates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tech")
def tech():
    tech_events = [
        {"name": "Tech Conference 2023", "date": "2023-03-01"},
        {"name": "AI Summit 2022", "date": "2022-10-01"},
        {"name": "Cybersecurity Symposium 2022", "date": "2022-06-01"},
    ]
    return render_template("tech.html", events=tech_events)

@app.route("/sports")
def sports():
    sports_events = [
        {"name": "World Cup 2022", "date": "2022-06-01"},
        {"name": "Summer Olympics 2023", "date": "2023-08-01"},
        {"name": "Super Bowl 2024", "date": "2024-02-01"},
    ]
    return render_template("sports.html", events=sports_events)

if __name__ == "__main__":
    app.run()
