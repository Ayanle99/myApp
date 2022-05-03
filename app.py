from flask import Flask, render_template
from flask_moment import Moment


app = Flask(__name__)
moment = Moment(app)



@app.route("/")
def home():
   return render_template('home.html')

@app.route("/java")
def java():
   return render_template('java.html')


@app.route("/python")
def python():
   return render_template('python.html')



@app.route("/about")
def about():
   return render_template('about.html')


@app.route("/videos")
def videos():
   return render_template('videos.html')



@app.route("/contact")
def contact():
   return render_template('contact.html')



if __name__ == "__main__":
   app.run()
