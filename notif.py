import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="YOU ARE THE BEST!!",
            message="Universe is giving you everything you need!FEEL THE ABUNDANCE WITHIN YOURSELF!!",
            app_icon=r"C:\Users\Pragya Nainwal\PycharmProjects\FIRST\icon.ico",
            timeout=1
        )
        time.sleep(2)

