import pgzrun
WIDTH = 870
HEIGHT = 650
TITLE = "Quiz Master"
Marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
Skip_box = Rect(0,0,150,330)
Timer_box = Rect(0,0, 150,150 )
Answer_box1 = Rect(0,0,300,150 )
Answer_box2 = Rect(0,0,300,150 )
Answer_box3 = Rect(0,0,300,150 )
Answer_box4 = Rect(0,0,300,150 )
score = 0
Time_left = 10
question_filename = "Questions.txt"
Marquee_message = ""
is_gameover = False
Answer_boxes = [Answer_box1, Answer_box2, Answer_box3, Answer_box4]
questions = []
question_count = 0
question_index = 0
Marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
Skip_box.move_ip(700,270)
Timer_box.move_ip(700,100)
Answer_box1.move_ip(20,270)
Answer_box2.move_ip(370,270)
Answer_box3.move_ip(20,450)
Answer_box4.move_ip(370,450)

def draw():
    global Marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(Marquee_box,"black")
    screen.draw.filled_rect(question_box,"purple")
    screen.draw.filled_rect(Skip_box,"cyan")
    screen.draw.filled_rect(Timer_box,"orange")
    screen.draw.filled_rect(Answer_box1,"red")
    screen.draw.filled_rect(Answer_box2,"blue")
    screen.draw.filled_rect(Answer_box3,"yellow") 
    screen.draw.filled_rect(Answer_box4,"green")
    Marquee_message = "Welcome to Quiz Master" 
    Marquee_message = Marquee_message + f"Q:{question_index} of {question_count}"
    screen.draw.textbox(Marquee_message, Marquee_box, color = "white")
    screen.draw.textbox(str(Time_left), Timer_box, color = "white")
    screen.draw.textbox("skip", Skip_box, color = "Black", angle = -90)
    screen.draw.textbox(question[0].strip(), question_box, color = "white")
    index = 1
    for Answer_box in Answer_boxes:
        screen.draw.textbox(question[index].strip(), Answer_box, color = "black")
        index = index + 1

def update():
    move_Marquee()

def move_Marquee():
    Marquee_box.x = Marquee_box.x - 2
    if Marquee_box.right < 0:
        Marquee_box.left = WIDTH

def read_questionfile():
    global question_count, questions
    q_file = open(question_filename, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count + 1
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in Answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index += 1
    if Skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score,question,Time_left,questions 
    score = score + 1
    if questions:
        question = read_next_question()
        Time_left = 10 
    else:
        game_over()

def game_over():
    global question,Time_left,is_gameover
    message = f"gameover you got {score} questions correct"
    question = [message,"-","-","-","-",5]
    Time_left = 0
    is_gameover = True

def skip_question():
    global question,Time_left
    if questions and not is_gameover:
        question = read_next_question()
        Time_left = 10
    else:
        game_over()

def update_timeleft():
    global Time_left
    if Time_left:
        Time_left -= 1
    else:
        game_over()

read_questionfile()
question = read_next_question()
clock.schedule_interval(update_timeleft,1)
pgzrun.go()
