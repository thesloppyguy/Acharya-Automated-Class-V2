from datetime import timedelta, datetime, date
from calendar import day_name
from re import sub


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


def click_home():
    homebutton = driver.find_element_by_class_name("jss10").find_elements_by_xpath(
        "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-colorInherit MuiButton-textSizeLarge MuiButton-sizeLarge']")
    homebutton[0].find_element_by_class_name("MuiButton-label").click()
    return


''''''
