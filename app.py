from re import sub
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from extra.functions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import logging
import platform

logging.basicConfig(filename='extra\Progress.log', format='%(asctime)s %(levelname)-8s %(message)s',
                    encoding='utf-8', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

logging.info('NEW DAY')

platform_name = str(platform.system())
dirname = os.path.dirname(__file__)

# CROSS OS INTIGRATION PROVIDED SAME VERSION OF CHORME
if platform_name == 'Windows':
    filename = os.path.join(dirname, 'extra\chromedriver.exe')
else:
    filename = os.path.join(dirname, 'extra\chromedriver')


# GET ID PASSWORD AND PATH TO DRIVER AND STORE IT IN A TXT FILE
login_info = cred()
AUID = login_info[:12]
PASSWORD = login_info[12:]

driver = webdriver.Chrome(executable_path=filename)
driver.get("https://alive.university/")

ID = driver.find_element_by_name("user_email")
ID.send_keys(AUID)
PASS = driver.find_element_by_name("user_password")
PASS.send_keys(PASSWORD)

driver.find_element_by_class_name("MuiButton-label").click()


class_panels_path = "//div[@class='MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded']"
class_times_path = ".//p[@class='MuiTypography-root mb-1 MuiTypography-body2 MuiTypography-colorTextSecondary']"
class_names_path = ".//h2[@class='MuiTypography-root MuiTypography-h5']"
join_button_path_1 = ".//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-textSizeSmall MuiButton-sizeSmall']"
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

    # START TIME LIST
    a = class_start_time_format(full_time)
    class_start_time.append(a)

    # END TIME LIST
    b = class_end_time_format(full_time)
    class_end_time.append(b)

    # SUBJECT NAME LIST
    c = class_name_format(full_subject_name)
    subject_name.append(c)


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


wait = WebDriverWait(driver, 10)
zero_time = zero_time_clock()

for i in range(number_of_classes):

    logging.info("Current Class"+str(subject_name[i]))

    sleep(10)

    class_duration = time_difference(class_end_time[i])
    if class_duration <= zero_time:
        continue
    sleeptime = class_duration.total_seconds()

    # join button finding
    re_class_list = driver.find_elements_by_xpath(class_panels_path)
    for j in range(len(re_class_list)):

        cur_subject_name = class_name_format(re_class_list[j].find_element_by_xpath(
            class_names_path).get_attribute("innerHTML"))

        cur_subject_time = class_start_time_format(
            re_class_list[j].find_element_by_xpath(class_times_path).get_attribute("innerHTML"))

        if subject_name[i] == cur_subject_name and class_start_time[i] == cur_subject_time:
            join_button = re_class_list[j].find_element_by_xpath(
                join_button_path_1).find_element_by_xpath(join_button_path_2)

    # JOINING CLASS
    while time_difference(class_end_time[i]) > zero_time:
        pop_up_message = ""
        join_button.click()
        try:
            pop_up = wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "MuiSnackbarContent-message")))

            pop_up_message = pop_up.get_attribute("innerHTML")
        except:
            pass

        if pop_up_message == "Session has not started!":
            logging.info('Class Joining Failed!! Trying again in 600 seconds')
            sleep(600)
        else:
            logging.info('Class Joined')
            sleep(10)
            sleep(sleeptime)
            driver.back()
            logging.info('Class Left')
            break

class_start_time.clear()
class_end_time.clear()
subject_name.clear()
join_button_list.clear()
delete_list.clear()
driver.close()
logging.info("END DAY")
# END
