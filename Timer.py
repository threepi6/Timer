from tkinter import *
from tkinter import messagebox
win = Tk()
#property
win.geometry("500x200")
win.resizable(False,False)
win.title('Timer')
#function
timer = None
hour = 0
min = 0
sec = 0
def fun_up_h():
    global hour
    hour +=1
    lbl_h.config(text =hour)

def fun_down_h():
    global hour
    if hour > 0:
        hour -=1
        lbl_h.config(text =hour)

def fun_up_min():
    global min 
    if min < 60:
        min +=1
        if min <=9:
            lbl_min.config(text = f'0{min}')
        else:
            lbl_min.config(text = min)

def fun_down_min():
    global min
    if min > 0:
        min -= 1
        if min <= 9:
             lbl_min.config(text = f'0{min}')
        else:
            lbl_min.config(text = min)

def fun_up_sec():
    global sec
    if sec < 60:
        sec +=1
        if sec < 10:
            lbl_sec.config(text = f'0{sec}')
        else:
            lbl_sec.config(text = sec) 

def fun_down_sec():
    global sec
    if sec > 0:
        sec -= 1
        if sec <= 9:
            lbl_sec.config(text = f'0{sec}')
        else:
            lbl_sec.config(text = sec)

def countdown():
    global timer
    global sec
    global min 
    global hour
    if sec == 0 and min == 0 and hour == 0:
        messagebox.showinfo('Time','Time is up')
        but_reset.config(state = DISABLED)
        but_stop.config(state = DISABLED)
    else:
        but_stop.config(state = NORMAL)
        but_reset.config(state = DISABLED)
        if sec == 0:
            if min == 0:
                min = 59
                sec = 59
                hour -= 1
                lbl_h.config(text = hour)
                lbl_min.config(text = min)
                lbl_sec.config(text = sec)
                timer = lbl_sec.after(1000,countdown)
            else:
                min -= 1
                sec = 59 
                if min <= 9:
                    lbl_min.config(text = f'0{min}')
                    lbl_sec.config(text = sec)
                else:
                    lbl_min.config(text = min)
                    lbl_sec.config(text = sec)
            timer = lbl_sec.after(1000,countdown)
        else:
            sec-=1
            if sec <= 9:
                lbl_sec.config(text = f'0{sec}')
            else:
                lbl_sec.config(text = sec)
            timer = lbl_sec.after(1000,countdown)

def stop():
    global timer
    if timer :
        but_reset.config(state = NORMAL)
        lbl_sec.after_cancel(timer)
        timer = None

def reset():
    global sec
    global min 
    global hour
    global tof
    sec = 0
    min = 0
    hour = 0
    lbl_h.config(text = hour)
    lbl_min.config(text = f'0{min}')
    lbl_sec.config(text = f'0{sec}')
    but_start.config(state = NORMAL)
    but_reset.config(state = DISABLED)
    but_stop.config(state = DISABLED)


#Widget
lbl_hshow = Label(text = 'h',font = 'ariyal 15 bold') 
lbl_hshow.place(x = 175, y = 10)

but_up_h = Button(text = "^", font = 'ariyal 20 ', command = fun_up_h)
but_up_h.place(x = 170, y = 40 , width = 30 , height = 30)

lbl_h = Label(text = '0',font = 'ariyal 25 bold') 
lbl_h.place(x = 175, y = 70)

but_down_h = Button(text = "\/", font = 'ariyal 13 bold', command = fun_down_h)
but_down_h.place(x = 170, y = 110 , width = 30 , height = 30)

label1 = Label(text = ':',font = 'ariyal 25 bold')
label1.place(x = 197, y = 68)

lbl_minshow = Label(text = 'min',font = 'ariyal 15 bold') 
lbl_minshow.place(x = 210, y = 10)

but_up_min = Button(text = "^", font = 'ariyal 20 ' , command = fun_up_min)
but_up_min.place(x = 210, y = 40 , width = 40 , height = 30)

lbl_min = Label(text = '00',font = 'ariyal 25 bold') 
lbl_min.place(x = 210, y = 70)

but_down_min = Button(text = "\/", font = 'ariyal 13 bold', command = fun_down_min)
but_down_min.place(x = 210, y = 110 , width = 40 , height = 30)

label2 = Label(text = ':',font = 'ariyal 25 bold')
label2.place(x = 252, y = 68)

lbl_secshow = Label(text = 'sec',font = 'ariyal 15 bold') 
lbl_secshow.place(x = 270, y = 10)

but_up_sec = Button(text = "^", font = 'ariyal 20 ',command = fun_up_sec)
but_up_sec.place(x = 270, y = 40 , width = 40 , height = 30)

lbl_sec = Label(text = '00',font = 'ariyal 25 bold') 
lbl_sec.place(x = 270, y = 70)

but_down_sec = Button(text = "\/", font = 'ariyal 13 bold', command = fun_down_sec)
but_down_sec.place(x = 270, y = 110 , width = 40 , height = 30)

but_start = Button(text = 'Start', font = 'ariyal 15' , command = countdown)
but_start.place(x = 100 , y = 150)


but_stop = Button(text = 'Stop', font = 'ariyal 15', state = DISABLED , command = stop)
but_stop.place(x = 190 , y = 150)

but_reset = Button(text = 'Reset', font = 'ariyal 15', state = DISABLED , command = reset)
but_reset.place(x = 290 , y = 150)
win.mainloop()