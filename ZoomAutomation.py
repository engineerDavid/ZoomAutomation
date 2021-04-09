import webbrowser
import datetime
import time
from datetime import datetime
#add her your time and day of the week your zoom meeting is on 
#0 = Monday
#1= Tuesday
#2 = Wednesday
#3 = Thursday 
#4 = Friday
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
weekday = datetime.today().weekday()
t = time.localtime()
current_time = time.strftime("%H:%M", t)
FMT = '%H:%M'
ComingUpClasses =[]
#print(c[1]["Day of week"][1])
from dateutil import parser
closestClass = "23:00:00"
for c in ZoomClasss.values():
    for clas in c:
        for day in clas["Day of week"]:
            if weekday == day:
                ClassTime = clas["Time"]
                #FMT = '%H:%M'
                
                tdelta = datetime.strptime(ClassTime, FMT) - datetime.strptime(current_time, FMT)
                #time = datetime.strptime(tdelta, FMT)
                
                if str(tdelta).find("day") == -1:
                    tdelta = parser.parse(str(tdelta))
                    closestClass = parser.parse(str(closestClass))
                    
                    if tdelta < closestClass:
                        print(tdelta)
                        closestClass = tdelta
                        ZoomUrl = clas["ZoomUrl"]
                else:
                    break
print(ZoomUrl)


webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open_new(ZoomUrl)