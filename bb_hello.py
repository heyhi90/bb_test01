#패키지 임폴트
from selenium import webdriver
import telegram
import time
import requests
from bs4 import BeautifulSoup
import os

github_T = os.environ.get('GIT_TOKEN')

def ppompp():
    testbot = telegram.Bot(token=github_T)
    testbot.sendMessage(1840767554, 'test2')

if __name__ == '__main__':

    try:
        ppompp()
    except AttributeError as e:
        print(e)