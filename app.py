from flask import Flask, render_template
import AllEvents

app = Flask(__name__, template_folder='uitemplates',static_folder='uitemplates')

@app.route("/")
def index():
    tech_events = AllEvents.get_all()
    return render_template("index.html", events=tech_events)

@app.route("/tech")
def tech():
    tech_events = AllEvents.get_all_techs()
    return render_template("tech.html", events=tech_events)

@app.route("/sports")
def sports():
    sports_events = AllEvents.get_all_sports()
    return render_template("sports.html", events=sports_events)

if __name__ == "__main__":
    app.run()
