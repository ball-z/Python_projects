import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water Now!",
            message = "The National Academics Of Science, Engineering and Medicine determined that"
                        "an adequate daily fluid intake for men is about 3.7 litres.",
            timeout = 10)
#time.sleep(1_hour)       
time.sleep(60*60)

     