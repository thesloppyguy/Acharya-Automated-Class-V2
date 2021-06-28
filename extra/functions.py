from datetime import timedelta, datetime, date
from calendar import day_name
from re import sub
from os import path
import tkinter as tk

read = ''
data = []


def cred():
    def get_data():

        def get_entry_fields():
            data.append(e1.get())
            data.append(e2.get())
            window.destroy()

        window = tk.Tk()
        window.geometry("420x100")
        window.title("Acharya Automated Attendence - Sahil")

        tk.Label(window, text="This program is not idiot proof so ").grid(
            row=0, column=0)
        tk.Label(window, text="please write and submit everything properly").grid(
            row=0, column=1)

        tk.Label(window, text="Username").grid(row=1)
        tk.Label(window, text="Password").grid(row=2)

        e1 = tk.Entry(window)
        e2 = tk.Entry(window)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)

        tk.Button(window, text='Quit', command=window.destroy).grid(
            row=5, column=0, pady=4)
        tk.Button(window, text='Submit', command=get_entry_fields).grid(
            row=5, column=1, pady=4)

        window.mainloop()

    if not path.exists("extra\cred.txt"):
        my_file = open('extra\cred.txt', 'w')
        get_data()
        my_file.writelines(data)

    my_file = open('extra\cred.txt', 'r')
    read = my_file.readline()
    my_file.close()
    return read


def time_difference(giventime):
    enter = str(datetime.now().time().strftime('%H:%M:%S'))
    enter = datetime.strptime(enter, '%H:%M:%S')
    exit = giventime
    enter_delta = timedelta(
        hours=enter.hour, minutes=enter.minute, seconds=enter.second)
    exit_delta = timedelta(
        hours=exit.hour, minutes=exit.minute, seconds=exit.second)
    difference_delta = exit_delta - enter_delta
    return difference_delta


def retun_day():
    dum = date.today()
    dum = dum.strftime("%d %m %Y")
    born = datetime.strptime(dum, '%d %m %Y').weekday()
    bob = day_name[born]
    return bob


def zero_time_clock():
    return timedelta(hours=00, minutes=00, seconds=00)


def format_time(ll):
    return datetime.strptime(ll, "%I:%M %p")


def class_start_time_format(a):
    k = a[14:22]
    if k[len(k) - 1] == "-":
        k = sub("-", "", k)
    starttime = format_time(k)
    starttime = starttime.time()

    return starttime


def class_end_time_format(a):
    k = a[22:len(a)]
    if k[0] == "-":
        k = sub("-", "", k)

    endtime = format_time(k)
    endtime = endtime.time()

    return endtime


def class_name_format(a):
    ll = a[10:len(a)]

    return str(ll)


''''''
