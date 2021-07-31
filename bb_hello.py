#패키지 임폴트
import telegram
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