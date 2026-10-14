with open('knowledge.txt', 'r') as file,open('data.txt','w') as d:
    c=0
    for line in file:
        if line=='':
            continue
        c+=1
        if c==2:
            text=prev_line+" "+line
            d.write(text)
            # print(text)
            d.flush()
            c=0
        else:
            prev_line=line
            prev_line=prev_line.replace("\n","")
def ask_question(question):
    max_score=0
    mrc=""
    with open('data.txt', 'r') as file:
        for chunk in file:
            score=0
            for word in question.split():
                if word.lower() in chunk.lower():
                    score+=1
            if score>max_score:
                max_score=score
                mrc=chunk
    print(mrc)
ask_question(input("What is your question? "))