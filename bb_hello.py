#패키지 임폴트
from selenium import webdriver
import telegram
import time
import requests
from bs4 import BeautifulSoup
import os

chrome_options1 = Options()
chrome_options1.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options1.add_argument('--disable-gpu')
chrome_options1.add_argument('--no-sandbox')

#텔레그램 환경변수
github_T = os.environ.get('GIT_TOKEN')

#driver 실행
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options1)
driver.implicitly_wait(3)

driver.get('https://bunker.blue/diary')
driver.find_element_by_name('user_id').send_keys('asd12')
driver.find_element_by_name('password').send_keys('asd1234')
driver.find_element_by_xpath('//*[@id="message_login_form"]/p/button').click()

post_Num=[]


def ppompp():
    testbot = telegram.Bot(token=github_T)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    post = soup.select_one('tbody')
    post_list = post.select('tr')

    for i in post_list:
        postNum = i.select_one(".no").text.lstrip()
        post_Num.append(postNum)

    print(post_Num[0])
    testbot.sendMessage(1840767554, 'a')

if __name__ == '__main__':

    try:
        ppompp()
    except AttributeError as e:
        print(e)