#!/usr/bin/python3
# vim: set fileencoding=utf-8 :
# vim: set et ts=4 sw=4:
# -*- coding:utf-8 -*-
# by 'hollowman6' from Lanzhou University(兰州大学)

'''
警告：
仅供测试使用，不可用于任何非法用途！
对于使用本代码所造成的一切不良后果，本人将不负任何责任！

Warning:
For TESTING ONLY, not for any ILLEGAL USE!
I will not be responsible for any adverse consequences caused by using this code.

'''

from copy import Error
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

titles = []
credits = []
grades = []

format = '''
The grade file is in csv format without header like:

    title, credit, grade
    ...

make sure that the grade is ranged between 0 and 100.
'''

print(format)
filename = input("grade file (empty to be `grade.csv`):")
if not filename:
    filename = 'grade.csv'

with open(filename, encoding="utf-8") as f:
    line = f.readline()
    while line:
        title, credit, grade = line.strip().split(',')
        if credit.isnumeric() and grade.isnumeric() and int(credit) > 0:
            titles.append(title)
            credits.append(credit)
            grades.append(grade)
        line = f.readline()

driver = webdriver.Chrome()

print("Please input and submit relevant information in the opened browser (WES iGPA Calculator) first,")
print("the programme will automatically fill the marks when needed.")

driver.get("https://applications.wes.org/igpa-calculator/igpa.asp")
wait = WebDriverWait(driver, 6000)

NetworkErr = False
while True:
    if driver.find_element_by_xpath('/html').get_attribute('dir') == "ltr":
        if not NetworkErr:
            print("Network error, please check your network!")
            NetworkErr = True
        driver.get(
            "https://applications.wes.org/igpa-calculator/igpa.asp")
        time.sleep(3)
    else:
        NetworkErr = False
        break

for i in range(1, len(titles)+1):
    title = wait.until(EC.presence_of_element_located((By.ID, "title"+str(i))))
    credit = wait.until(
        EC.presence_of_element_located((By.ID, "credit"+str(i))))
    grade = wait.until(EC.presence_of_element_located((By.ID, "grade"+str(i))))
    title.send_keys(titles[i-1])
    credit.send_keys(credits[i-1])
    grade.send_keys(grades[i-1])
    if i != len(titles):
        driver.execute_script("ShowRow();")

submit = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="main-wrapper"]/div[3]/div/div/form/div[7]/input')))
submit.click()
raise Error("Done! Please close the browser manually after reviewing your GPA.")
