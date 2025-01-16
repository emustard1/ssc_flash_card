from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'askjdhasdkjhsa'


def is_filled(data):
    if data == '2':
        return redirect(url_for('correct'))
   


maths = [('What is 1 + 1?', '2')]
invalid = True

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')
  
@app.route('/test', methods=["GET", "POST"])
def question(maths=maths):    
    user_answer=0
    while not user_answer:
      user_answer = request.form['answer']
      if user_answer == '2':
        return redirect(url_for('/correct'))
      elif user_answer != '2':
        return redirect(url_for('/incorrect'))
      return render_template('test.html', question=maths)

@app.route('/correct', methods=["GET", "POST"])
def correct():
   return render_template('correct.html', question=maths)

@app.route('/incorrect', methods=["GET", "POST"])
def incorrect():
   return render_template('incorrect.html', question=maths)

@app.route('/score', methods=["GET", "POST"])
def display_scores():
  #wrong_answers = [(number, maths[0])]
  return render_template('score.html') 
    
  
if __name__ == "__main__":
  app.run(debug=True)
  