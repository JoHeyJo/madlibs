from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

WORDS = silly_story.return_prompts()
print(WORDS)

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def index():
  """Show homepage"""
  return render_template("questions.html", words_jinja=WORDS)

@app.post("/story")
def make_story():

# request.for[""]




  return render_template("story.html", story_jinja=STORY)