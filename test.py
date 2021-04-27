from tkinter import *

username = ''
password = ''

my_file = open('cred.txt', 'r')

if not first_char:
    my_file = open('cred.txt', 'a')

    print("file is empty")  # add GUI here


my_file = open('cred.txt', 'r')
username = my_file.readline()
password = my_file.readline()
my_file.close()

print(username)
print(password)
