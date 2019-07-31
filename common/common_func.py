# -*- coding: utf-8 -*-
import os, time, csv
import logging


def getScreenShot(driver, module=os.path.basename(__file__)):
    time=getTime()
    image_file = os.path.dirname(os.getcwd()) + '\screenshots\%s_%s.png' %(module, time)
    logging.info('=====< get %s screenshot >' %module+' =====')
    driver.get_screenshot_as_file(image_file)

"""
driver = webdriver.Chrome()
module = "login.py"
getScreenShot(driver)
"""


def getTime():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    return now


def WriteToCsv(csvfile, titles, csv_data):
  '''写CSV文件'''
  with open(csvfile, 'w', encoding='utf-8', newline='') as f:
    #f.write(codecs.BOM_UTF8)
    writer = csv.writer(f)
    writer.writerow(titles)
    writer.writerows(csv_data)

"""
csv_path = os.path.join(os.getcwd(), 'data')
login_csvfile = csv_path + '/login_data.csv'
title = ['username', 'password']
data = [
  ['admin', 'lorda7900'],
  ['admin', '123456']
]
WriteToCsv(login_csvfile, title, data)
"""


def ReadCSV(csvfile, line):
  '''读取CSV文件指定行数据'''
  if os.path.exists(csvfile):
    with open(csvfile, 'r', encoding='UTF-8') as f:
      reader = csv.reader(f)
      for index, row_data in enumerate(reader):
        if index == line:
          return row_data


"""
csv_path = os.path.join(os.getcwd(), 'data')
csvfile = csv_path + '/login_data.csv'
ReadCSV(csvfile, 1) #读取csv第二行，index=1
"""
