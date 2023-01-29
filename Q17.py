
# read answer key from keys.txt
with open('keys.txt', 'r') as file:
    answer_key = file.readline().strip().split(' ')#Each line after space has the answer so we are storing seperately

# read answers from marks.txt
student_answers=[]
with open('marks.txt', 'r') as file:
    for line in file:
        student_answers.append(line.strip().split(' '))#similarly each line has each students info and asnwers so storing in a list format

file.close()

# calculate score for each student
scores = []
for answers in student_answers:#for each student 
    score = 0
    for i in range(len(answer_key)):#for each question if answer is true we assign marks (score+=1)
        if answers[i] == answer_key[i]:
            score += 1
    scores.append(score)#appending total marks to the marks list in order

    # display total marks scored by each student
for i in range(len(scores)):#optional if u want u can print all students marks
    print(f'Student{i}: {scores[i]}')

# find the index of top scorer
max_index = scores.index(max(scores))

# display top scorer and the top score
print(f'Top Scorer: Student{max_index} with marks = {max(scores)}')

