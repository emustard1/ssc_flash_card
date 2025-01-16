from flask import Flask

app = Flask(__name__)

@app.route('/home')
def hello():
    return "Hello, world"
  

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
  