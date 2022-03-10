from selenium import webdriver
import time

browser = webdriver.Edge('D:/user/Desktop/MyPandas/msedgedriver.exe')
url = 'https://bill.ntt-finance.co.jp/mem-view'
browser.get(url)
browser.maximize_window()

elem_id = browser.find_element_by_id('txtLoginId')
elem_id.send_keys('✕✕✕✕✕')

elem_pw = browser.find_element_by_id('pwdLoginPsw')
elem_pw.send_keys('〇〇〇〇〇')

elem_login_btn = browser.find_element_by_id('btnLogin')
elem_login_btn.click()

from selenium.webdriver.support.ui import Select

cmpny = browser.find_element_by_name('jigyoCmpnySlctKbn')
cmpny_select = Select(cmpny)
cmpny_select.select_by_value("2")

elem_no = browser.find_element_by_name('txtTelNoOrMltprpsBillNo')
elem_no.send_keys('0123456789')

elem_sousin_btn = browser.find_element_by_id('btnSnd')
elem_sousin_btn.click()

elem_syousai_btn = browser.find_element_by_xpath('//*[@id="init"]/div[1]/dl/dd[2]/div[2]/section[1]/section/dl/dd/div/div[1]/div/div[1]/button')
elem_syousai_btn.click()

time.sleep(2)
elem_dwnload_btn = browser.find_element_by_xpath('//*[@id="detail0"]/section/div[4]/div[1]/a')
browser.execute_script("arguments[0].scrollIntoView(true);", elem_dwnload_btn)
elem_dwnload_btn.click()

time.sleep(2)
elem_doui_btn = browser.find_element_by_xpath('/html/body/main/div/div[2]/section/div[3]/div/label/span')
browser.execute_script("arguments[0].scrollIntoView(true);", elem_doui_btn)
elem_doui_btn.click()

import glob
import os

for file1 in glob.glob('D:/user/Downloads/*.pdf'):
    os.remove(file1)
for file1 in glob.glob('D:/user/Downloads/*.xlsx'):
    os.remove(file1)
for file1 in glob.glob('D:/user/Downloads/*.csv'):
    os.remove(file1)

elem_dwnload_btn = browser.find_element_by_xpath('//*[@id="command"]/div[1]/div[1]/a')
elem_dwnload_btn.click()

elem_dwnload_btn = browser.find_element_by_xpath('/html/body/div[2]/div/div/a')
elem_dwnload_btn.click()

time.sleep(3)
for file1 in glob.glob('D:/user/Downloads/*.pdf'):
    print(file1)

file2 = 'D:/user/Downloads/NTT西日本(01-2345-6789).pdf'

os.rename(file1, file2)

import tabula

pdf_path = 'D:/user/Downloads/NTT西日本(00-0000-0000).pdf'

dfs = tabula.read_pdf(pdf_path, stream=True)
df = dfs[0]
kingaku = df['Unnamed: 0'][9]

import datetime
import jpholiday

dt_now = datetime.date.today()
d = datetime.date(dt_now.year, dt_now.month, 24)
holiday = jpholiday.is_holiday(d)

while holiday == True or d.weekday() >= 5:
    d = d + datetime.timedelta(days=1)
    holiday = jpholiday.is_holiday(d)

siharaibi = d.strftime('%Y.%m.%d')
x = siharaibi + 'NTT西日本(00-7859-4347)' + kingaku + '円.pdf'

file3 = 'D:/user/Downloads/' + x

os.rename(file2, file3)

from tkinter import messagebox

messagebox.showinfo('確認', 'PDF保存完了しました！')