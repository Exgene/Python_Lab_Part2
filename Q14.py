class Time:
    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec

def addTime(currTime,breadTime):
    finalHour=currTime.hour+breadTime.hour
    finalMin=currTime.min+breadTime.min
    finalSec=currTime.sec+breadTime.sec

    if finalMin>=60:
        finalHour+=1
        finalMin%=60

    if finalSec>=60:
        finalMin+=1
        finalSec%=60
    
    finalTime=Time(finalHour,finalMin,finalSec)
    return finalTime

def printTime(curTime):
    print("Hours:",curTime.hour)
    print("Minutes:",curTime.min)
    print("Seconds:",curTime.sec)


print("Current Time:")
currHour=int(input("Hour:"))
currMin=int(input("Minute:"))
currSec=int(input("Seconds:"))

currTime=Time(currHour,currMin,currSec)

print("Bread Time:")
breadHour=int(input("Hour:"))
breadMin=int(input("Minute:"))
breadSec=int(input("Seconds:"))

breadTime=Time(breadHour,breadMin,breadSec)

Final=addTime(currTime,breadTime)
printTime(Final)
