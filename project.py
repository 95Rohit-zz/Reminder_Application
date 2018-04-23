# Reminder Application:-
import time
import datetime
import credentials

while(1):
    day =datetime.datetime.today().weekday()
    now = datetime.datetime.now()
    start = now.replace(hour=14,minute=1,second=0)
    end = now.replace(hour=22,minute=49,second=0)
    if day == 0:
        print("nothing")
    elif day ==1:
        if start < now < end:
            print("Rohit")
            credentials.pg1()
            time.sleep(3400)
    elif day ==2:
        if start < now < end:
            print("Rohan")
            credentials.pg2()
            time.sleep(3400)
    elif day ==3:
        if start < now < end:
            print("Karan")
            credentials.hello()
            time.pg5(3400)
    elif day ==4:
        if start < now < end:
            print("Rohan")
            credentials.pg2()
            time.sleep(3400)
    elif day ==5:
        print("Hello")
    else:
        if start < now < end:
            print("Karma")
            credentials.pg3()
            time.sleep(3400)
