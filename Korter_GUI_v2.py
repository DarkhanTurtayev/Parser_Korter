
import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import csv
import pandas as pd
from pandas import DataFrame
import numbers
import random
import numpy as np
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from datetime import date, datetime
import os, sys
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename



ROOT = tk.Tk()
ROOT.geometry("400x200")

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Parse Korter",
                                  prompt="Enter URL")

url = USER_INP

#PATH_CHROMEDRIVER = askopenfilename()

#pathway_chromediriver = PATH_CHROMEDRIVER
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get(url)



#pagination
compare = []


'''
for i in range(1,10):
    try: 
        xpath = '//*[@id="app"]/div[2]/div/div[3]/div[2]/ul/li[6]/a'
        page = driver.find_element(By.XPATH, xpath).text
        print(page)
    except:
        page = 1
    compare.append(page)
print(compare)

compare_2 = []
for i in compare:
    try:
        d = int(i)
        compare_2.append(d)
    except:
        d = 0
last_page = max(compare_2)

'''

links_data = []
name_data = []
link = ''
last_page = simpledialog.askinteger('Please Enter number of pages to parse ', 'Enter number')
ask_elemenents = simpledialog.askstring('Please Enter CLASS NAME', 'Enter ClassName')
#ask_class_name = simpledialog.askstring('Please Enter 2nd CLASS NAME', 'Enter ClassName')



url_split = url.split('?',1)

if len(url_split) < 2:
    url_split = url

print (url)
print(str(url_split))
for i in range(1, last_page +1):

    driver.maximize_window
    if url_split == url: 
        new_url = url + '?page=' + str(i)
    else:
        new_url = url_split[0] + '?page=' + str(i) + url_split[1]

    driver.get(new_url)

    elements = driver.find_elements(By.CLASS_NAME, ask_elemenents)
    for i in elements:
        hrefs = i.find_element(By.TAG_NAME, 'a')
 
        try:
            link = hrefs.get_attribute('href')
        except:
            link = None

        links_data.append(link)


 
  
print(len(links_data))
print(links_data)





all_data = []


link_data = []
name_data = []
company_data = []
full_address = []
city_data = []
district_data = []
street_data = []
amount_data = []
available_data = []
price_sq_data = []
status_data = []
deadline_data = []
class_data = []
otdelka_data = []
parking_data = []
floors_data = []
height_data = []
type_data = []
extra_data = []


one_data = []
two_data = []
three_data = []
four_data = []
five_data = []
six_data = []
seven_data = []
taunhause_data = []
duplex_data = []
cottage_data = []

one_data_sq = []
two_data_sq = []
three_data_sq = []
four_data_sq = []
five_data_sq = []
six_data_sq = []
seven_data_sq = []
taunhause_data_sq = []
duplex_data_sq = []
cottage_data_sq = []

one_price_sq = []
two_price_sq = []
three_price_sq = []
four_price_sq = []
five_price_sq = []
six_price_sq = []
seven_price_sq = []
taunhause_price_sq = []
duplex_price_sq = []
cottage_price_sq = []



for i in links_data:
    time.sleep(2)
    try:
        
        driver.get(i)
        driver.set_page_load_timeout(10)
        link_data.append(i)

        try: 
            data = driver.find_element(By.XPATH, "//div[contains(., 'Застройщик')]").text
        except:
            data = ''
        
        l = data.replace('\u200d','').split('\n')
        print(l)
        if 'Застройщик' in l:
            company_num = l.index('Застройщик') + 1
            company = l[company_num]
        else:
            company = None

        company_data.append(company)

        if 'Цена / м2' in l:
            sq_price_num = l.index('Цена / м2') + 1
            sq_price = l[sq_price_num]
        else:
            sq_price = None

        price_sq_data.append(sq_price)

        if 'Адрес' in l:
            street_num = l.index('Адрес') + 1
            street = l[street_num]
        else:
            street = None

        street_data.append(street)


        for i in l:
            if 'Паркинг' in i:
                parking = i.replace('Паркинг', '')
                break
            else:
                parking = None

        parking_data.append(parking)

        for i in l:
            if 'Класс' in i:
                class_ = i.replace('Класс', '')
                break
            else:
                class_ = None

        class_data.append(class_)

        for i in l:
            if 'Количество квартир' in i:
                amount = i.replace('Количество квартир', '')
                break
            else:
                amount = None

        amount_data.append(amount)

        for i in l:
            if 'Этажность' in i:
                floor = i.replace('Этажность', '')
                break
            else:
                floor = None

        floors_data.append(floor)

        for i in l:
            if 'Технология строительства' in i:
                type = i.replace('Технология строительства', '')
                break
            else:
                type = None

        type_data.append(type)

        for i in l:
            if 'сдача' in i:
                deadline = i.replace('сдача', '')
                break
            else:
                deadline = None

        deadline_data.append(deadline)

        for i in l:
            if 'Отделка квартир' in i:
                otdelka = i.replace('Отделка квартир', '')
                break
            else:
                otdelka = None

        otdelka_data.append(otdelka)

        for i in l:
            if 'Высота потолков' in i:
                height = i.replace('Высота потолков', '')
                break
            else:
                height = None

        height_data.append(height)

        for i in l:
            if 'Территория' in i:
                extra = i.replace('Территория', '')
                break
            else:
                extra = None

        extra_data.append(extra)

        for i in l:
            if 'строится' in i:
                status = i
                break
            else:
                status = 'зввершен'

        status_data.append(status)

        for i in l:
            if 'Новостройки' in i:
                adress = i.replace('Новостройки', '')
                break
            else:
                adress = ''

        district_data.append(adress)

        if '1-комнатные' in l:

             sq_m = l[l.index('1-комнатные') + 1]
             sq_price = l[l.index('1-комнатные') + 2]
             price = l[l.index('1-комнатные') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        one_data_sq.append(sq_m)
        one_price_sq.append(sq_price)
        one_data.append(price)


        if '2-комнатные' in l:

             sq_m = l[l.index('2-комнатные') + 1]
             sq_price = l[l.index('2-комнатные') + 2]
             price = l[l.index('2-комнатные') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        two_data_sq.append(sq_m)
        two_price_sq.append(sq_price)
        two_data.append(price)
    
        if '3-комнатные' in l:

             sq_m = l[l.index('3-комнатные') + 1]
             sq_price = l[l.index('3-комнатные') + 2]
             price = l[l.index('3-комнатные') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        three_data_sq.append(sq_m)
        three_price_sq.append(sq_price)
        three_data.append(price)

        if '4-комнатные' in l:

             sq_m = l[l.index('4-комнатные') + 1]
             sq_price = l[l.index('4-комнатные') + 2]
             price = l[l.index('4-комнатные') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        four_data_sq.append(sq_m)
        four_price_sq.append(sq_price)
        four_data.append(price)


        if '5-комнатные' in l:

             sq_m = l[l.index('5-комнатные') + 1]
             sq_price = l[l.index('5-комнатные') + 2]
             price = l[l.index('5-комнатные') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        five_data_sq.append(sq_m)
        five_price_sq.append(sq_price)
        five_data.append(price)

        if '6-комнатные' in l:

             sq_m = l[l.index('6-комнатные') + 1]
             sq_price = l[l.index('6-комнатные') + 2]
             price = l[l.index('6-комнатные') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        six_data_sq.append(sq_m)
        six_price_sq.append(sq_price)
        six_data.append(price)

        if '7-комнатные' in l:

             sq_m = l[l.index('7-комнатные') + 1]
             sq_price = l[l.index('7-комнатные') + 2]
             price = l[l.index('7-комнатные') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        seven_data_sq.append(sq_m)
        seven_price_sq.append(sq_price)
        seven_data.append(price)



        if 'Таунхаусы' in l:

             sq_m = l[l.index('Таунхаусы') + 1]
             sq_price = l[l.index('Таунхаусы') + 2]
             price = l[l.index('Таунхаусы') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        taunhause_data_sq.append(sq_m)
        taunhause_price_sq.append(sq_price)
        taunhause_data.append(price)

        if 'Коттеджи' in l:

             sq_m = l[l.index('Коттеджи') + 1]
             sq_price = l[l.index('Коттеджи') + 2]
             price = l[l.index('Коттеджи') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        cottage_data_sq.append(sq_m)
        cottage_price_sq.append(sq_price)
        cottage_data.append(price)

        if 'Дуплексы' in l:

             sq_m = l[l.index('Дуплексы') + 1]
             sq_price = l[l.index('Дуплексы') + 2]
             price = l[l.index('Дуплексы') + 3]

        else:
            sq_m = ''
            sq_price = ''
            price = ''

        duplex_data_sq.append(sq_m)
        duplex_price_sq.append(sq_price)
        duplex_data.append(price)



        for i in l:
            if 'Планировки и цены в' in i:
                name = i.replace('Планировки и цены в', '')
                break
            else:
                name = ''

        name_data.append(name)
    except:
        pass
    
    


df = DataFrame(
    
        {
            
        'Link': link_data,
        'Название': name_data,
        'Адрес' : district_data,
        'Улица' : street_data,
        'Застройщик': company_data,
        'Этажи' : floors_data,
        'Отделка' : otdelka_data,
        'Паркинг' : parking_data,
        'Отделка' : otdelka_data,
        'Класс' : class_data,
        'Срок сдачи' : deadline_data,
        'Цена' : price_sq_data,
        'Цена 1 - комн': one_data,
        'Цена 2 - комн': two_data,
        'Цена 3 - комн': three_data,
        'Цена 4 - комн': four_data,
        'Цена 5 - комн': five_data,
        'Цена 6 - комн': six_data,
        'Цена 7 - комн': seven_data,
        'Цена Таунхаусы' : taunhause_data,
        'Цена Коттеджи' : cottage_data,
        'Дуплекс' : duplex_data,
        '1 - комн площадь': one_data_sq,
        '2 - комн площадь': two_data_sq,
        '3 - комн площадь': three_data_sq,
        '4 - комн площадь': four_data_sq,
        '5 - комн площадь': five_data_sq,
        '6 - комн площадь': six_data_sq,
        '7 - комн площадь': seven_data_sq,
        'Таунхаус площадь': taunhause_data_sq,
        'Коттедж площадь' : cottage_data_sq,
        'Дуплекс площадь' : duplex_data_sq

    
        }
    ) 

filename = asksaveasfilename() 
df.to_excel(filename + '.xlsx')


