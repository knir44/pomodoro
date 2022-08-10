from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer) #how to stop the after method
    canvas.itemconfig(timer_text, text="00:00")
    Timer.config(text= "Timer",fg = GREEN)
    Check_mark.config(text ="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 2 ==1:
        Timer.config(text= "Work",fg = GREEN)
        count_down(work_sec)

    elif reps % 8 == 0:
        Timer.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
         Timer.config(text="Break", fg=PINK)
         count_down(short_break_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count>0:
        global  timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            marks +="✔"
        Check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100,pady=50,bg = YELLOW)


canvas = Canvas(width=200,height=224,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(row = 1,column=1)



Timer = Label(text ="Timer", font = (FONT_NAME,50),fg = GREEN,bg = YELLOW)
Timer.grid(row = 0,column=1)

Check_mark = Label(font = (FONT_NAME,15),fg = GREEN,bg = YELLOW)
Check_mark.grid(row = 3,column=1)

start = Button(text="Start",font = (FONT_NAME,12),highlightthickness=0,command=start_timer)
start.grid(row = 2,column=0)

reset = Button(text="Reset",font = (FONT_NAME,12),highlightthickness=0,command= reset_timer)
reset.grid(row = 2,column=2)

window.mainloop()