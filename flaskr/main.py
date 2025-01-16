questions = []

asking = 5
i=1


#basic idea for site
while(i < asking):
    question = input("Please write a question: ")
    answer = input("Please write the answer: ")
    
    questions.append((i,question,answer))
    i += 1

print(questions)

#question testing

[(id, question, answer)]