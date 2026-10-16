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
timer=None
flag=0
count_min=0
count_sec=0

# ---------------------------- STOP SETTING ------------------------------- # 
def stop_time():
    global flag,count_sec,count_min
    flag=1
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps,flag
    reps=flag=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps=0
def start_timer():
    global reps,count_min,count_sec,flag
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    # to count 5 minutes in countdown we need to multiply with 60 to convert into seconds as after method only tells about milli seconds
    if flag==1:
        flag=0
        count_down(((count_min)*60)+count_sec)
    elif reps%8==0:
        count_down(long_break_sec)
        title.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        title.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer,count_min,count_sec
    count_min=count//60
    count_sec=count%60
    if flag!=1:
        if count_sec<10:
            count_sec=f"0{count_sec}"
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        if count>0:
            timer=window.after(1000, count_down, count-1)
        else:
            start_timer()
            marks=""
            work_sessions=reps//2
            for i in range (work_sessions):
                marks+="✔"
            check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# window
window=Tk()

window.title("Pomodoro")
window.config(padx=100,pady=50,background=YELLOW)

# Canvas
canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="Tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

# Title
title=Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,background=YELLOW)
title.grid(row=0,column=1)

# Start and reset button
start=Button(text="Start",highlightthickness=0,command=start_timer)
reset=Button(text="reset",highlightthickness=0,command=reset_timer)
start.grid(row=2,column=0)
reset.grid(row=2,column=2)

# Check mark
check_mark=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
check_mark.grid(row=3,column=1)


# Stop button
stop=Button(text="Stop",highlightthickness=0,command=stop_time)
stop.grid(row=3,column=1)

window.mainloop()