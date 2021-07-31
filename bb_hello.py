#패키지 임폴트
import telegram
import os

#github_T = os.environ.get('GIT_TOKEN')

def ppomppu():
    testbot = telegram.Bot(token='1902707442:AAHcK9oumcVMWUWJMAhk0JFj-aH-Gxp6e48')
    testbot.sendMessage(1840767554, 'test1')

if __name__ == '__main__':

    try:
        ppomppu()
    except AttributeError as e:
        print(e)