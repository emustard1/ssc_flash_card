from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
  

@app.route('/create')
def create_flashcard():
   return 0

@app.route('/question')
def question():
   return 0

@app.route('/question/score')
def display_scores():
   return 0

  
if __name__ == "__main__":
  app.run(debug=True)
  