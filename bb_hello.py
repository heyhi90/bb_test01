#패키지 임폴트
import telegram
import os

github_T = os.environ.get('GIT_TOKEN')

def ppomppu():
    testbot = telegram.Bot(token=github_T)
    testbot.sendMessage(1840767554, 'a')

if __name__ == '__main__':

    try:
        ppomppu()
    except AttributeError as e:
        print(e)