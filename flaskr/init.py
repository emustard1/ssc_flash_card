from flask import Flask, request, render_template, redirect, url_for
from 

app = Flask(__name__)

maths = [('What is 1 + 1?', '2')]
invalid = True

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/test', methods =["GET", "POST"])
def question(maths=maths):    
    
    #still need to fix this bit
    user_answer = None
    if request.method == "POST":
      user_answer = request.form.get('user_answer')

    if user_answer == maths[0][1]:
       return redirect(url_for('correct'))


    #original question template
    return render_template('test.html', form='question_response')

@app.route('/score')
def display_scores():
  #wrong_answers = [(number, maths[0])]
  return render_template('score.html') 
    
  
if __name__ == "__main__":
  app.run(debug=True)
  