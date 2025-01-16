from flask import Flask, render_template

app = Flask(__name__)

maths = [('What is 1 + 1?', '2')]

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/test')
def question():
   return render_template('test.html', question=maths)

@app.route('/score')
def display_scores():
   return render_template('score.html')

  
if __name__ == "__main__":
  app.run(debug=True)
  