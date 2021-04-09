import webbrowser
import datetime
import time
from datetime import datetime
from dateutil import parser
#add her your time and day of the week your zoom meeting is on 
#0 = Monday
#1= Tuesday
#2 = Wednesday
#3 = Thursday 
#4 = Friday

#Where you see ZoomUrl you need to add in your ZoomUrl link
# you also need to add in the time and day of week for you classes
ZoomClasss = {
    "classes": [
        {
            "Time": "9:30",
            "Day of week": [0, 2, 4],
            "ZoomUrl": ""
        },
        {
            "Time": "17:10",
            "Day of week": [0, 2, 4],
            "ZoomUrl": "
        },
        {
            "Time": "16:20",
            "Day of week": [0, 2, 4],
            "ZoomUrl": ""
        },
        {
            "Time": "9:45",
            "Day of week": [1, 3],
            "ZoomUrl": ""
        },
        {
            "Time": "11:50",
            "Day of week": [1, 3],
            "ZoomUrl": ""
        }


    ]

}


#used to check what day it is of the week 0-6
#monday = 0
weekday = datetime.today().weekday()
t = time.localtime()
#gets the current time at your location
current_time = time.strftime("%H:%M", t)
#used to only have hours and min format
FMT = '%H:%M'
#23 hours is used since you dont usualyy open zoom 23 hours before class
closestClass = "23:00:00"

for c in ZoomClasss.values():
    #used to go through every class in dic
    for clas in c:
        #goes through the days of the week your class is on
        for day in clas["Day of week"]:
            #check to see what classes you have today
            if weekday == day:
                #gets the time of todays classes
                ClassTime = clas["Time"]
                #checks to see how much time you hvae left before your classes for today start
                tdelta = datetime.strptime(ClassTime, FMT) - datetime.strptime(current_time, FMT)
                #makes sure your next class is not a day away
                if str(tdelta).find("day") == -1:
                    #parser helps compare the times
                    tdelta = parser.parse(str(tdelta))
                    closestClass = parser.parse(str(closestClass))
                    #used to see which class is happening sooner
                    if tdelta < closestClass:
                        closestClass = tdelta
                        #keeps track of the url of the class with closer time
                        ZoomUrl = clas["ZoomUrl"]
                else:
                    break



#Used to open up the url in the chrome browser
#if you brefer a diffrent browser just change the 'chrome' in code bellow to desired code
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open_new(ZoomUrl)
