from flask import Flask, request, render_template

app = Flask(__name__)

maths = [('What is 1 + 1?', '2')]


@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/test', methods =["GET", "POST"])
def question():
    
    #get answer
    if request.method == "POST":
        user_answer = request.form.get("u_answer")
      
    #compare answer to original
    if user_answer == maths[0][1]:
        return render_template("correct.html")
    elif user_answer != maths[0][1]:
       return render_template("incorrect.html", user_answer)

      #we get input in a string
      #need to compare this to the correct answer
      #if 
    return render_template('test.html')

@app.route('/score')
def display_scores():
  #wrong_answers = [(number, maths[0])]
  return render_template('score.html') 
    
  
if __name__ == "__main__":
  app.run(debug=True)
  