#패키지 임폴트
from selenium import webdriver
import telegram
import time
import requests
from bs4 import BeautifulSoup
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
chrome_options.add_argument("lang=ko")



#driver 실행
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
driver.implicitly_wait(6)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

text1=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/p').text
"""


driver.find_element_by_name('user_id').send_keys('asd12')
driver.find_element_by_name('password').send_keys('asd1234')
driver.find_element_by_xpath('//*[@id="message_login_form"]/p/button').click()

post_Num=[]
"""
#텔레그램 환경변수
github_T = os.environ.get('GIT_TOKEN')
testbot = telegram.Bot(token=github_T)
testbot.sendMessage(1840767554, text1)

def ppompp():
    print('')

"""
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    post = soup.select_one('tbody')
    post_list = post.select('tr')

    for i in post_list:
        postNum = i.select_one(".no").text.lstrip()
        post_Num.append(postNum)

    print(post_Num[0])
    testbot.sendMessage(1840767554, 'twewer')
"""

if __name__ == '__main__':

    try:
        ppompp()
    except AttributeError as e:
        print(e)