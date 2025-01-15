questions = []

asking = 5
i=1

while(i < asking):
    question = input("Please write a question: ")
    answer = input("Please write the answer: ")
    
    questions.append((i,question,answer))
    i += 1

print(questions)