from re import sub
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from functions import time_difference, retun_day, zero_time_clock, format_time, class_start_time_format, class_end_time_format, class_name_format, click_home
from tkinter import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# GET ID PASSWORD AND PATH TO DRIVER AND STORE IT IN A TXT FILE

driver = webdriver.Chrome(
    executable_path=r"D:\Programs\PYTHON\SOURCE\ACHARYA CLASS V2\venv\chromedriver.exe")
driver.fullscreen_window()
driver.get("https://alive.university/")


ID = driver.find_element_by_name("user_email")
ID.send_keys("AIT19BECS080")
PASS = driver.find_element_by_name("user_password")
PASS.send_keys("Sahil@123")

driver.find_element_by_class_name("MuiButton-label").click()


class_panels_path = "//div[@class='MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded']"
class_times_path = ".//p[@class='MuiTypography-root mb-1 MuiTypography-body2 MuiTypography-colorTextSecondary']"
class_names_path = ".//h2[@class='MuiTypography-root MuiTypography-h5']"
join_button_path_1 = ".//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-textSizeLarge MuiButton-sizeLarge']"
join_button_path_2 = ".//span[@class='MuiButton-label']"


# PERIOD TIME
sleep(10)
class_panel_list = driver.find_elements_by_xpath(class_panels_path)
number_of_classes = len(class_panel_list)

# LIST DECLARATION
class_start_time = []
class_end_time = []
subject_name = []
join_button_list = []
delete_list = []

# INITIALISE ALL THE LISTS

for i in range(number_of_classes):

    full_time = class_panel_list[i].find_element_by_xpath(
        class_times_path).get_attribute("innerHTML")

    full_subject_name = class_panel_list[i].find_element_by_xpath(
        class_names_path).get_attribute("innerHTML")

    join_button = class_panel_list[i].find_element_by_xpath(
        join_button_path_1).find_element_by_xpath(join_button_path_2)

    # START TIME LIST
    a = class_start_time_format(full_time)
    class_start_time.append(a)

    # END TIME LIST
    b = class_end_time_format(full_time)
    class_end_time.append(b)

    # SUBJECT NAME LIST
    c = class_name_format(full_subject_name)
    subject_name.append(c)

    # JOIN BUTTON LIST
    join_button_list.append(join_button)

# SEQUENCE OF CLASSES

for i in range(number_of_classes):
    for j in range(0, number_of_classes - i - 1):
        if class_start_time[j] > class_start_time[j + 1]:
            class_start_time[j], class_start_time[j +
                                                  1] = class_start_time[j + 1], class_start_time[j]
            class_end_time[j], class_end_time[j +
                                              1] = class_end_time[j + 1], class_end_time[j]
            class_panel_list[j], class_panel_list[j +
                                                  1] = class_panel_list[j + 1], class_panel_list[j]
            subject_name[j], subject_name[j +
                                          1] = subject_name[j + 1], subject_name[j]
            join_button_list[j], join_button_list[j +
                                                  1] = join_button_list[j + 1], join_button_list[j]

# DELETE DIPLOMA CLASS AND -1 FROM NUMBER OF CLASSES

for i in range(number_of_classes):
    if subject_name[i] == "MATDIP_II":
        delete_list.append(i)

element_in_del = len(delete_list)
number_of_classes = number_of_classes-element_in_del

for elem in range(element_in_del):
    index = delete_list[elem]
    del subject_name[index]
    del class_start_time[index]
    del class_end_time[index]
    del join_button_list[index]

    # MAKE GUI FOR ALL THE CLASSES

# print(subject_name)
# print(class_start_time)
# print(class_end_time)

wait = WebDriverWait(driver, 10)
running = True
zero_time = zero_time_clock()

for i in range(number_of_classes):

    sleep(10)

    class_duration = time_difference(class_end_time[i])
    if class_duration <= zero_time:
        continue
    sleeptime = class_duration.total_seconds()+300

    # JOINING CLASS
    while running:
        pop_up_message = ""
        join_button_list[i].click()
        try:
            pop_up = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "MuiSnackbarContent-message")))

            pop_up_message = pop_up.get_attribute("innerHTML")
        except:
            pass

        if pop_up_message == "Session has not started!":
            print("class join failed try again in 600 seconds")
            sleep(600)
            if time_difference(class_end_time[i]) < zero_time:
                break
        else:
            sleep(10)
            # click on X button
            #driver.find_elements_by_xpath("//button[@class='md--Q7ug4 buttonWrapper--x8uow dismiss--1zWwpv']").click()
            # check for polling option
            sleep(sleeptime+600)
            click_home()
            break

driver.close()
# END


# <button aria-label="Listen only" aria-disabled="false" class="jumbo--Z12Rgj4 buttonWrapper--x8uow audioBtn--1H6rCK">
# <span class="button--Z2dosza jumbo--Z12Rgj4 default--Z19H5du circle--Z2c8umk">
# <i class="icon--2q1XXw icon-bbb-listen">
# </i>
# </span>
# <span class="label--Z12LMR3">Listen only</span>
# </button>
